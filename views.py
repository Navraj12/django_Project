from django.shortcuts import render, HttpResponse
from MyApp.models import contact


# Create your views here.
def index(request):
    context = {
        'variable':"this is sent"
        
    } 
    return render(request,'index.html',context)

def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        # phone = request.POST.get('')
        phone = request.POST.get('phone', '')
        contact_instance = contact.objects.create(email=email, name=name, phone=phone)
        contact.save()
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is about page")  

def services(request):
    return render(request,'services.html')



def home(request):
    return render(request,'home.html')



