from django.shortcuts import render
import requests



def button(request):

    return render(request,'index.html')


def output(request):
    data=requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,'index.html',{'data':data})

def external(request):
    inp= request.POST.get('param')