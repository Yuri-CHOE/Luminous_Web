from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request,'main/bootexam.html',{})

def led(request):
    return render(request,'main/led.html',{})
def calender(request):
    return render(request,'main/calender.html',{})
def alarm(request):
    return render(request,'main/alarm.html',{})
def music(request):
    return render(request,'main/music.html',{})
def time(request):
    return render(request,'main/time.html',{})

