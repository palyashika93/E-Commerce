from django.shortcuts import render,redirect
from home.models.customer import Customer
from django.contrib.auth.hashers import make_password

def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    else:
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2') 

        
        #validation
        error_message=None
        customer=Customer(name=name,email=email,password=password,password2=password2)
        
        if(not name):
            error_message='Username is Required !!'
        elif len(name)<4:
            error_message='Username must be 4 or more character long !! ' 
        elif not password:
            error_message='Password is Required !!'
        elif len(password)<4:
            error_message='Password is too short'    
        elif len(password)<6:
            error_message='Password must be 6 char long'        
        elif not password==password2:
            error_message='Password does not match !!'
        elif password==password2:
            if customer.isExists():
                error_message='Email is already exist !!'
                
        #saving
        if not error_message:
            print(name,email,password,password2)
            customer.password=make_password(customer.password)
            customer.password2=make_password(customer.password2)
          
            customer.register()
            return redirect('login')
        else:    
            return render(request,"register.html",{'error':error_message})