from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def main(request):
    return render(request,'main/main.html')

def status(request):
    return render(request,'main/status.html',{})
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
def one(request):
    return render(request,'main/1.html',{})
def two(request):
    return render(request,'main/2.html',{})
def th(request):
    return render(request,'main/3.html',{})