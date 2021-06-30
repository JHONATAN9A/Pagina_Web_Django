from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def covid19(request):
    dic ={'etiqueta':"Esto se introdujo deste django"}
    return render(request,"Covid19.html",context=dic)

