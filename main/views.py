from django.shortcuts import render
from .models import emails

# Create your views here.

def home(request):
    if request.method == "POST":
        email1 = request.POST.get( 'email1' )
        email2 = request.POST.get( 'email2' )
        
        if  email1 and email2:
            emails.objects.create(email=email1)
        elif  (email1 and not email2):
            emails.objects.create(email=email1)
        elif (email2 and not email1):
            emails.objects.create(email=email2)
            

    return render(request,'index.html')