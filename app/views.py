from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.
def Registration(request):
    EFRO=RegistrationForm()
    d={'EFRO':EFRO}

    if request.method=='POST':
        DFRO=RegistrationForm(request.POST)
        if DFRO.is_valid():
            return HttpResponse(str(DFRO.cleaned_data))
    return render(request,'Registration.html',d)