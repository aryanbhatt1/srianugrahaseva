from django.shortcuts import render
from .models import slogan, OrgDetails, register
from .forms import registerForm, contactForm
from django.contrib import messages
from SriAnugrahaSeva.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage


# Create your views here.

def home(request):

    media = slogan.objects.all()
    orgdetails = OrgDetails.objects.all()

    context = {
        'media': media,
        'orgdetails': orgdetails,
    }
    return render(request, 'pages/home.html', context)

def registerView(request):
    orgdetails = OrgDetails.objects.all()
    form = registerForm()
    context = {
        'orgdetails': orgdetails,
        'form': form,
    }
    
    if request.method == "POST":
        form = registerForm(request.POST)
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        address = request.POST.get('address')
        postalCode = request.POST.get('postalCode')
        requirement = request.POST.get('requirement')
        services = request.POST.get('services')
        mode = request.POST.get('mode')
        date = request.POST.get('date')
        others = request.POST.get('others')

        r = register.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            phonenumber = phonenumber,
            address = address,
            postalCode = postalCode,
            requirement = requirement,
            services = services,
            mode = mode,
            date = date,
            others = others
        )

        r.save()

        subject = "Registered For Pooja - {}".format(str(email))

        message = """
        Hi,<br>
        New registration for Pooja<br><br>
        Here are the details<br><br>
        First Name : %s<br>
        Last Name : %s<br>
        Email : %s<br>
        Phone Number : %s<br>
        Address : %s<br>
        Postal Code : %s<br>
        Requirement : %s<br>
        Services : %s<br>
        Mode : %s<br>
        Date : %s<br>
        Others : %s<br>
        <br>
        Thank You
        """%(str(first_name), str(last_name), str(email),
            str(phonenumber), str(address), str(postalCode),
            str(requirement), str(services), str(mode),
            str(date), str(others)    
        )
        email = ['srianugrahaseva@gmail.com',]
        mail = EmailMessage(subject, message, str(EMAIL_HOST_USER), email)  
        mail.content_subtype = "html"
        mail.send() 

        messages.success(request,'Registered Sucessfully !!')
        return render(request, 'pages/register.html',  context)
            
    return render(request, 'pages/register.html', context)

def contact(request):
    orgdetails = OrgDetails.objects.all()
    form = contactForm()

    context = {
        'orgdetails': orgdetails,
        'form': form
    }

    return render(request, 'pages/contact.html', context)