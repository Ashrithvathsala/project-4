from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def  ashrith(request):
     return HttpResponse ('ashrith is an achiever')
def goal(request):
    return HttpResponse('he will reach his goal soon')