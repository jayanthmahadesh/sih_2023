from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework.views import APIView
from .serializer import backendserializer
import requests
from .models import jsondata
from datetime import datetime,timedelta
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

# Create your views here.
key = '81ef2125fd93249117f5f3dafb757933'
@csrf_exempt
@api_view(('GET','POST'))
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def homepage(request):
    if request.method == "POST":
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        detail = request.POST.get('detail')
        backend = jsondata.objects.all()
        backend = backend.filter(latitude=latitude,longitude=longitude,detail=detail)
        t=0
        if not backend:
            t=1
        if t==0:
            serializedbackend = backendserializer(backend,many=True)
            serializedbackend = serializedbackend.data[0]
            serializedbackend = dict(serializedbackend)
            current_time = datetime.now()
            timestamp = serializedbackend["date"]
            parsed_timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
            time_difference = current_time - parsed_timestamp
            ten_minutes = timedelta(minutes=10)

        if(t==0 and time_difference<=ten_minutes):
            data = serializedbackend["data"]
        else:
            if backend:
                backend.delete()
            url = f'https://api.openweathermap.org/data/2.5/{detail}?lat={latitude}&lon={longitude}&appid={key}'
            response = requests.get(url)
            data = response.json()
            model_instance = jsondata(
                latitude = latitude,
                longitude = longitude,
                detail = detail,
                data = data,
                date = datetime.now()
            )
            model_instance.save()
        context = {}
        if(detail=="forecast"):
            final = []
            tempdict = data["list"]
            for i in range(0,data["cnt"]):
                tempdict={}
                tempdict["temp"]=data["list"][i]["main"]["temp"]
                tempdict["weather"]=data["list"][i]["weather"][0]["description"]
                tempdict["humidity"]=data["list"][i]["main"]["humidity"]
                tempdict["date"] = data["list"][i]["dt_txt"]
                final.append(tempdict)
            context = {
                'final':final,
                'latitude':latitude,
                'longitude':longitude
            }
            return render(request,'forecast.html',context)
            # return Response({'status':200,'payload':final})
        else:

            weather= data["weather"][0]["description"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]

            context = {
                'weather':weather,
                'latitude':latitude,
                'longitude':longitude,
                'humidity':humidity,
                'wind':wind,
                'temp':temp
            }
            return render(request,'current.html',context)
            # return Response({'status':200,'payload':context})
        
    return render(request,'homepage.html')




