from django.shortcuts import render
from django.views import View
from .models import CaseList,CustomUser
import spacy
nlp = spacy.load('en_core_web_lg')
from django.core import serializers
from .serializer import *
import pyotp
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.hashers import check_password



# Create your views here.
def send_otp_email(request):
    # try:
    if(request.method =='POST'):
        otp_secret = pyotp.random_base32()
        request.session['otp_secret'] = otp_secret
        otp = pyotp.TOTP(otp_secret).now()

        subject = 'Your OTP for Two-Factor Authentication'
        message = f'Your OTP is: {otp}'
        from_email = 'computeruse777@gmail.com'
        user_email = request.POST['email']
        print("user name = ",user_email)
        recipient_list = [user_email]

        send_mail(subject, message, from_email, recipient_list)
        return render(request,'verify.html')
    # except Exception as e:
    #     return render(request,'signup.html')


def login_with_2fa(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        otp_input = request.POST['otp']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check if OTP matches the one stored in the session
            if 'otp_secret' in request.session:
                otp_secret = request.session['otp_secret']
                otp = pyotp.TOTP(otp_secret).now()

                if otp == otp_input:
                    login(request, user)
                    return redirect('home')
                else:
                    # Invalid OTP
                    messages.error(request, 'Invalid OTP. Please try again.')
            else:
                # OTP not generated or session expired
                messages.error(request, 'OTP not generated. Please try again.')

        else:
            # Invalid username or password
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'registration/login_with_2fa.html')
def custom_sort_key(item):
    # First, sort by 'value' in descending order
    value = item['critical_score']

    # Next, sort by 'case_type' with 'criminal' coming first
    case_type = item['Case_type']
    if case_type == 'criminal':
        case_type_order = 1
    else:
        case_type_order = 2

    # Define a dictionary to assign sorting order for 'matter_type'
    matter_type_order = {
        'high_profile': 1,
        'non_bailable': 2,
        'bailable': 3,
    }

    # Sort by 'matter_type' using the defined order
    matter_type = item['matter']
    matter_type_order_value = matter_type_order.get(matter_type, 4)  # Default to 4 for any other value

    return (-value, case_type_order, matter_type_order_value)




def get_critical(paragraph):
    seed_words = {
    "Crime": 7,
    "Criminal": 8,
    "Investigation": 6,
    "Suspect": 6,
    "Detective": 7,
    "Evidence": 6,
    "Forensics": 6,
    "Witness": 5,
    "Prosecutor": 8,
    "Defense": 8,
    "Jury": 6,
    "Trial": 7,
    "Verdict": 8,
    "Judge": 8,
    "Lawyer": 8,
    "Alibi": 5,
    "Testimony": 6,
    "Conviction": 9,
    "Acquittal": 4,
    "Sentence": 9,
    "Prison": 9,
    "Bail": 5,
    "Parole": 4,
    "Homicide": 9,
    "Robbery": 7,
    "Burglary": 6,
    "Theft": 5,
    "Assault": 7,
    "Kidnapping": 9,
    "Arson": 8,
    "Forgery": 6,
    "Fraud": 7,
    "Embezzlement": 7,
    "Cybercrime": 8,
    "Identity theft": 8,
    "Drug trafficking": 9,
    "Money laundering": 9,
    "Racketeering": 8,
    "Organized crime": 8,
    "White-collar crime": 7,
    "Domestic violence": 7,
    "Stalking": 6,
    "Harassment": 5,
    "Child abuse": 8,
    "Sexual assault": 9,
    "Cyberbullying": 4,
    "Hate crime": 8,
    "Gang": 6,
    "Drive-by shooting": 7,
    "Carjacking": 7,
    "Terrorism": 10,
    "Extortion": 7,
    "Blackmail": 6,
    "Smuggling": 6,
    "Bribery": 6,
    "Corruption": 7,
    "Perjury": 5,
    "Witness tampering": 6,
    "Interrogation": 6,
    "Search warrant": 6,
    "Surveillance": 6,
    "Wiretap": 7,
    "Crime scene": 6,
    "Autopsy": 5,
    "Missing person": 5,
    "Cold case": 6,
    "Fugitive": 7,
    "Evidence tampering": 7,
    "Crime lab": 6,
    "Polygraph": 5,
    "Miranda rights": 6,
    "Sovereign immunity": 4,
    "Statute of limitations": 4,
    "Legal defense": 7,
    "Plea bargain": 6,
    "Grand jury": 6,
    "Indictment": 6,
    "Felony": 8,
    "Misdemeanor": 5,
    "Probation": 4,
    "Rehabilitation": 5,
    "Juvenile delinquency": 5,
    "Capital punishment": 9,
    "Hate speech": 4,
    "Forensic science": 6,
    "Criminal profiling": 7,
    "Crime prevention": 5,
    "Crime rate": 5,
    "Victim": 5,
    "Vigilante": 4,
    "Crime scene tape": 4,
    "Crime spree": 7,
    "Witness protection": 6,
    "Crime syndicate": 7,
    "Evidence locker": 5,
    "Perp walk": 4,
    "Criminal record": 7,
    "Police brutality": 8,
    "Crime fiction": 3
}


# Input paragraph
    # paragraph =  "In a high-profile criminal case that captivated the nation, John Smith stood accused of masterminding a complex bank heist. The investigation uncovered a web of evidence, including security camera footage, fingerprints at the scene, and financial transactions linking Smith to the stolen funds. During the trial, the prosecution presented a compelling case, presenting witness testimonies, forensic analysis, and bank records. The defense, however, argued that Smith was wrongly accused and presented an alibi corroborated by family members. After weeks of legal proceedings and intense deliberation, the jury reached a verdict of guilty, and John Smith was sentenced to a lengthy prison term. This criminal case underscored the importance of a thorough investigation and the adversarial nature of the legal system."
    common_words = [
        "plaintiff", "defendant", "complaint", "summons", "answer",
        "motion", "judge", "court", "attorney", "evidence",
        "testimony", "jury", "verdict", "appeal", "settlement",
        "counsel", "docket", "pleadings", "discovery", "subpoena",
        "lawsuit", "cause of action", "jurisdiction", "injunction",
        "damages", "cross-examination", "affidavit", "statute",
        "precedent", "hearing"
    ]
    words = paragraph.split()
    filtered_words = [word for word in words if word.lower() not in common_words]
    filtered_paragraph = " ".join(filtered_words)
    paragraph=filtered_paragraph
    # print(paragraph)
    # Tokenize and process the paragraph
    doc = nlp(paragraph)
    extracted_words=set()

    for token in doc:
        if token.pos_ != "PROPN":
            extracted_words.add(token.text)
    related_words = set()

# Set a similarity threshold
    similarity_threshold = 0.75

    # Iterate through the tokens and find related words
    result=dict()
    for word in extracted_words:
        for key in seed_words:
            similarity_score = nlp(word).similarity(nlp(key))
            if similarity_score > similarity_threshold:
                result[key]=seed_words[key]
                #print(key,word)
                #print(similarity_score)

    # Print the related words

    sorted_dict = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

    critical_score=0

    max_elements = min(10, len(sorted_dict))

    # Iterate through the dictionary up to a maximum of 10 elements
    for key, value in list(sorted_dict.items())[:max_elements]:
        critical_score+=value
    print("The critical score is: ")
    print(critical_score)
    return critical_score
def landing(request):
    return render(request,'landing.html')
class dashboard(View):
    def get(self,request):
        if request.session.get('is_authenticated'):
            cases = CaseList.objects.filter(user_id=request.session.get('unique_id'))
            cases=caseserializer(cases,many=True)
            cases=cases.data
            context={
                'cases':cases
            }
            return render(request, 'dashboard.html',context)
        else:
            return render(request,'login.html')
# def dashboard(request):
#     if request.session.get('is_authenticated'):
#         return render(request, 'dashboard.html')
#     else:
#         return render(request,'login.html')
class signup(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        aadhar = request.POST.get("aadhar")
        gender = request.POST.get("gender")
        password = request.POST.get("password")
        email = request.POST.get("email")
        signed_user = CustomUser(first_name=first_name,last_name=last_name,aadhar_number=aadhar,password=password,gender=gender)
        signed_user.save()
        return render(request,'login.html')
class login(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        first_name = request.POST.get("first_name")
        password = request.POST.get("password")
        users = CustomUser.objects.filter(first_name=first_name)
        user = userserializers(users,many=True)
        user=user.data
        user=user[0]
        if(len(user)>0):
            password_matches = check_password(password, user['password'])
            if password_matches:
                request.session['is_authenticated'] = True
                request.session['unique_id'] = user['unique_id']
                return render(request,'landing.html')
            else:
                messages.error(request, 'Invalid username or password')
                return render(request,'login.html')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request,'login.html')
def logout(request):
    request.session.clear()
    return render(request,'landing.html')

class case_file(View):
    def get(self, request):
        if request.session.get('is_authenticated'):
            return render(request, 'case_filing_form.html')
        else:
            return render(request,'login.html')

    def post(self,request):
        if request.session.get('is_authenticated'):
            short_case_name = request.POST.get("short_case_name")
            case_type = request.POST.get("type")
            matter = request.POST.get("matter")
            petitioner = request.POST.get("petitioner")
            respondent = request.POST.get("respondent")
            court_of_origin = request.POST.get("court_of_origin")
            case_description = request.POST.get("case_description")
            user_id=request.session.get('unique_id')
            critical_score = get_critical(case_description)
            filed_case = CaseList(user_id=user_id,Short_Case_Name=short_case_name,Case_type=case_type,matter=matter,Petitioner=petitioner,Respondent=respondent,
            Court_of_origin=court_of_origin,Case_description=case_description,critical_score=critical_score)
            filed_case.save()
            return render(request, 'dashboard.html')




class judge_dash(View):
    def get(self,request):
        cases = CaseList.objects.all()
        cases = caseserializer(cases,many=True)
        # print(cases.data)
        cases=cases.data
        # cases = sorted(cases, key=lambda x: x['critical_score'], reverse=True)
        cases = sorted(cases, key=custom_sort_key)
        context={
            'cases':cases
        }
        return render(request,'judge_dash.html',context)
