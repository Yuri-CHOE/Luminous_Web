from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request,'main/bootexam.html',{})

#def bootexam(request):
#    return render(request,'main/bootexam.html',{})
