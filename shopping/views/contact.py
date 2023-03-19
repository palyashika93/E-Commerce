from django.shortcuts import render,redirect
from home.models.contact import Contact
from django.core.mail import send_mail


    
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        Contact(name=name,
                email=email,
                subject=subject,
                message=message).save()
       
        
        subject='Delicious'
        from_email='testingpurpose8000@gmail.com'
        msg=f'Hi {name}, We have received your message.For few minutes we make a confirmation call.Please accept this.Thanking you to contact with us ☺.For any information call us 992199129 '
        to=[email]

        send_mail(subject,msg,from_email,to,fail_silently=False)
    return render(request,'contact.html')
     
    