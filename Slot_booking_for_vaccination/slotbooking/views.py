from django.shortcuts import render,redirect
from .models import pmodel,hmodel
from .forms import pform,hform
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail

# Create your views h
def display(request):
    return render(request,"home.html")

def patientlogin(request):
    return render(request,"plogin.html")

def userLogin(request):
    # print("hello")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        print(username,password)
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            # print("login")
            return redirect("slotbooking")
        # print(user)
        # login(request,user)
        
    #     values = pmodel.objects.all()
    #     print(values)
    #     if username in values and password in values:
    #         print("HII")
    #         return redirect("slotbooking")
    #     else:
    #         print("User not there")
    return render(request,"user.html")
        # '''
        # ins = authenticate(username = username,password = password)        
        # print(ins)
        # if ins is not None:
        #     login(request,ins)
        #     print("login")
        #     return redirect("slotbooking") 
        # else:
        #     print("Some Error")    
        #     # return render(request,"user.html")
        #     '''
    #return render(request,"user.html")
def adminLogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # print(username,password)
        user = authenticate(username = username,password = password)
        print("namaste",user)
        login(request,user)
        return redirect("slotbooking")
    return render(request,"admins.html")

def signup(request):
    if request.method == "POST":
        # fname = request.POST["fname"]
        # lname = request.POST["lname"]
        # age = request.POST["age"]
        # username = request.POST["username"]
        # phno = request.POST["phno"]        
        # pwd = request.POST["pwd"]
        # repwd = request.POST["repwd"]
        # ins = pmodel(fname = fname,lname = lname,age = age,username = username,phno = phno,pwd = pwd,repwd = repwd)
        # ins.save()
        form = SignUpForm(request.POST)
        print(form)
        if form.is_valid():              #Process the form to Check if parameters are valid
            user = form.save()
            # print("valid form")
            login(request,user)
            return redirect('slotbooking')
        else:
            print(form.errors.as_data()) 
        # ins.objects.create_user(username,pwd)
        # return redirect("slotbooking.html")
        return render(request,"signup.html")                 
    '''
        form = pform(request.POST)
        if form.is_valid() and request.POST["pwd"] == request.POST["repwd"]:
            user = form.save()
            # print(user)
            login(request,user)
            return redirect("slotbooking.html")
            '''

    return render(request,"signup.html")

def hlogin(request):
    return render(request,"hlogin.html")

def hsign(request):
    if request.method == "POST":
        hname = request.POST["hname"]
        email = request.POST["email"]
        addr = request.POST["addr"]
        ins = hmodel(hname = hname,email = email,addr = addr)
        ins.save()
        return render(request,"home.html")
    return render(request,"hsign.html")
        
    
    # if request.method == "POST":
    #     # print("hi")
    #     form = hform(request.POST)
    #     # print(form)
    #     if form.is_valid():
    #         # print("it is valid")
    #         user = form.save()
    #         login(request,user)
    #         return redirect("home.html")
    # return render(request,"hsign.html")
@login_required
def slotbooking(request):
    content = hmodel.objects.all()
    print(content)
    return render(request,"slotbooking.html",{'content': content})

hname = ""
@login_required
def slots(request):
    if request.method == "POST":
        global hname
        hname = request.POST["hname"]
        '''
        ins = hmodel.objects().filter(hname = hname)
        ins.slots -= 1
        ins.save()
        print(hname)
        '''
        return render(request,"slots.html",{'hname':hname})
    return render(request,"slots.html")

def logoutuser(request):
    logout(request)
    return redirect("home")

slotss = 20
def success(request):
    if request.method == "POST":
        aadhaar = request.POST["aadhar"]
        email = request.POST["emaill"]
        slot = request.POST["inputGroupSelect01"]
        global slotss
        if slotss == 0:
            hmodel.objects.filter(hname = hname).update(slots = 20)
            return redirect("sorry")
        slotss-=1
        #ins = hmodel.objects.filter(hname = hname).values()
        hmodel.objects.filter(hname = hname).update(slots = slotss)
        print(aadhaar,email,slot,hname) 
        
        #ins.slots -= 1
        #ins[0].save()
        # print(aadhaar,email,slot,hname)
        
        send_mail(
            "Vaccination Confirmation", # Subject
            "This is to confirm that your slot " + slot +" has been booked on Aadhar no"+aadhaar+"."+"\n\n\n\n Thanks for choosing our Hospital!!",   # Message
            "getvaccinated9@gmail.com", # From whom
            [email]                    # To whom
        )
        

        messages.success(request,"Your Slot has been booked! Check your gmail for confirmation")
        return redirect("slots")
    #return redirect("slots")

    

