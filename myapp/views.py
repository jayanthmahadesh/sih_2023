from django.shortcuts import render
from django.views import View
from .models import CaseList,CustomUser
# Create your views here.
def landing(request):
    return render(request,'landing.html')
def dashboard(request):
    return render(request,'dashboard.html')
class signup(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        aadhar = request.POST.get("aadhar")
        gender = request.POST.get("gender")
        password = request.POST.get("password")
        signed_user = CustomUser(first_name=first_name,last_name=last_name,aadhar_number=aadhar,password=password,gender=gender)
        signed_user.save()
        return render(request,'landing.html')

class case_file(View):
    def get(self, request):
        return render(request, 'case_filing_form.html')

    def post(self,request):
        short_case_name = request.POST.get("short_case_name")
        case_type = request.POST.get("type")
        matter = request.POST.get("matter")
        petitioner = request.POST.get("petitioner")
        respondent = request.POST.get("respondent")
        court_of_origin = request.POST.get("court_of_origin")
        case_description = request.POST.get("case_description")
        user_id=100
        filed_case = CaseList(user_id=user_id,Short_Case_Name=short_case_name,Case_type=case_type,matter=matter,Petitioner=petitioner,Respondent=respondent,
        Court_of_origin=court_of_origin,Case_description=case_description)
        filed_case.save()
        return render(request, 'landing.html')

