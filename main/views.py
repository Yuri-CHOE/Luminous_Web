from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def main(request):
    return render(request,'main/main.html')

def bootexam(request):
    return render(request,'main/bootexam.html')

def status(request):
    return render(request,'main/status.html')
