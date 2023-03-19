from django.shortcuts import render,redirect
from home.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.http.response import HttpResponseRedirect

def login(request):
    return_url=None
    if request.method=='GET':
        return_url=request.GET.get('return_url')
        print(return_url)
        return render(request,"login.html")
    else:
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
     
        error_message=None
       
        if customer:
            flag=check_password(password,customer.password)
            if flag:
                request.session['customer']=customer.id
                if return_url:
                    return HttpResponseRedirect(return_url)
                else:
                    return_url=None
                    return redirect('home')    
            else:
                error_message='Invalid Credentials !!'    
        else:
            error_message='Invalid Credentials !!'

      
        print(name,email,password)    
        return render(request,"login.html",{'error':error_message})
        
def logout(request):
    request.session.clear()
    return redirect('home')   
