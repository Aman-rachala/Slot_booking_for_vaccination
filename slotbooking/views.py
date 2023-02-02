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

    return render(request,"signup.html")

def hlogin(request):
    return render(request,"hlogin.html")

def hsign(request):
    if request.method == "POST":
        hname = request.POST["hname"]
        email = request.POST["email"]
        slots = request.POST["slots"]
        addr = request.POST["addr"]
        ins = hmodel(hname = hname,email = email,addr = addr,slots = slots)
        ins.save()
        return render(request,"home.html")
    return render(request,"hsign.html")
        
    
@login_required
def slotbooking(request):
    content = hmodel.objects.all()
    print(content)
    return render(request,"slotbooking.html",{'content': content})

# hnames = ''
@login_required
def slots(request,hname):
    print("hname:",hname)
    ins = hmodel.objects.filter(hname = hname)[0]
    print("ins:",ins)
    if request.method == "POST":
        # hname = request.POST["hname"]
        # global hnames
        # hnames += hname
        '''
        ins = hmodel.objects().filter(hname = hname)
        ins.slots -= 1
        ins.save()
        print(hname)
        '''
        aadhaar = request.POST["aadhar"]
        email = request.POST["emaill"]
        slot = request.POST["inputGroupSelect01"]
        ins.slots = ins.slots - 1
        ins.save()
        
        send_mail(
            "Confirmation of Vaccination Appointment at"+ins.hname, # Subject
            '''Dear ''' + email +''',\n
This email is to confirm your upcoming vaccination appointment at '''+ins.hname+ ''' on '''+slot+'''.\n

Here is some important information to keep in mind:\n

Please arrive at the hospital at the specified time for your appointment.\n

Please bring a government-issued photo ID, insurance card, and any relevant medical records or reports.\n

If you need to cancel or reschedule your appointment, please contact us at least 24 hours in advance.\n

If you have any symptoms such as fever, cough, shortness of breath, or loss of taste or smell, please call us before coming to the hospital.\n

Please wear a face mask at all times while in the hospital and follow all safety protocols in place for the protection of patients and staff.\n

You may experience some side effects after receiving the vaccine, such as pain, redness, or swelling at the injection site, as well as fatigue, headache, or muscle pain. These side effects are usually mild and resolve within a few days.\n

If you have any questions or concerns, please don't hesitate to contact us at getvaccinated64@gmail.com\n

Thank you for choosing ''' + ins.hname+''' for your healthcare needs. We look forward to seeing you soon.\n

Best regards,\n'''+ins.hname




            ,   # Message
            "getvaccinated64@gmail.com", # From whom
            [email]                    # To whom
        )

        messages.success(request,"Your Slot has been booked! Check your gmail for confirmation")
        # return redirect("slots")

        return render(request,"slots.html",{'ins':ins})
    return render(request,"slots.html",{'ins':ins})

def logoutuser(request):
    logout(request)
    return redirect("home")
# print(hnames)
# def success(request):
#     if request.method == "POST":
#         aadhaar = request.POST["aadhar"]
#         email = request.POST["emaill"]
#         slot = request.POST["inputGroupSelect01"]
#         # ins = hmodel.objects.filter(hname = hnames).values()
#         #slotss = ins.slots 
#         # print(ins)
#         '''
#         if slotss == 0:
#             hmodel.objects.filter(hname = hname).update(slots = 20)
#             return redirect("sorry")

#         hmodel.objects.filter(hname = hname).update(slots = slotss-1)
#         print(aadhaar,email,slot,hname) 
        
#         #ins.slots -= 1
#         #ins[0].save()
#         # print(aadhaar,email,slot,hname)
        
#         send_mail(
#             "Vaccination Confirmation", # Subject
#             "This is to confirm that your slot " + slot +" has been booked on Aadhar no"+aadhaar+"."+"\n\n\n\n Thanks for choosing our Hospital!!",   # Message
#             "getvaccinated9@gmail.com", # From whom
#             [email]                    # To whom
#         )
#         '''
        

#         messages.success(request,"Your Slot has been booked! Check your gmail for confirmation")
#         return redirect("slots")
#     #return redirect("slots")

    

