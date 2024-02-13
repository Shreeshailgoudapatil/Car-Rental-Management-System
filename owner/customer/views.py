import smtplib

from django.shortcuts import render
from customer.models import userlogin

from customer.models import carbooking

from customer.models import complaint

from customer.models import addcustomer

from customer.models import adddriver

from customer.models import rentdetails

from customer.models import tripchart

from customer.models import cardetails

from customer.models import userlogin


# Create your views here.




def insertaddcustomer(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        addcustomer.objects.create( cust_id=s1, name=s2, address=s3, mobile_no=s4, email_id=s5, cust_type=s6)
        return render(request, "add_customer.html")
    return render(request,"add_customer.html")

def viewcustomer(request):
    userdict = addcustomer.objects.all()
    return  render(request,"view_add_customer.html",{'userdict':userdict})

def customer_del(request,pk):
    rid=addcustomer.objects.get(id=pk)
    rid.delete()
    userdict=addcustomer.objects.all()
    return render(request,'view_add_customer.html',{'userdict':userdict})


def insertadddriver(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.POST.get("t8")
        s9 = request.POST.get("t9")
        adddriver.objects.create( driver_id=s1,  name=s2, address=s3, mobile_no=s4, reference_given=s5, liscense_no=s6, liscense_type=s7, expire_date=s8, aadhar_no=s9)
        return render(request, "adddriver.html")
    return render(request,"adddriver.html")

def viewadddriver(request):
    userdict = adddriver.objects.all()
    return render(request, 'viewadddriver.html', {'userdict': userdict})


def driver_del(request, pk):
    rid = adddriver.objects.get(id=pk)
    rid.delete()
    userdict = adddriver.objects.all()
    return render(request, 'viewadddriver.html', {'userdict': userdict})


def insertcarbooking(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.POST.get("t8")
        s9 = request.POST.get("t9")
        carbooking.objects.create( booking_id=s1,  cust_id=s2, car_id=s3, booking_date=s4, reg_date=s5, to_place=s6, no_of_days=s7,rent_id=s8,status=s9)
        return render(request, "CarBooking.html")
    return render(request, "CarBooking.html")

def viewcarbooking(request):
    userdict = carbooking.objects.all()
    return render(request, "viewcarbooking.html", {'userdict': userdict})

def carbooking_del(request,pk):
    rid=carbooking.objects.get(id=pk)
    rid.delete()
    userdict=carbooking.objects.all()
    return render(request,'viewcarbooking.html',{'userdict':userdict})

def insertcardetails(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        cardetails.objects.create(car_id=s1, company=s2, make=s3, reg_no=s4, fuel_type=s5, capacity=s6,
                                  photo=s7)
        return render(request, "Cardetails.html")
    return render(request,"CarDetails.html")

def viewcardetails(request):
    userdict = cardetails.objects.all()
    return render(request, "viewcardetails.html", {'userdict': userdict})


def cardetails_del(request, pk):
    rid = cardetails.objects.get(id=pk)
    rid.delete()
    userdict = cardetails.objects.all()
    return render(request, 'viewcardetails.html', {'userdict': userdict})

def insertcomplaint(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        complaint.objects.create(cust_id=s1, trip_id=s2, complaint_type=s3, details=s4, date=s5, status=s6)
        return render(request, "complaint.html")
    return render(request,"complaint.html")

def viewcomplaint(request):
    userdict = complaint.objects.all()
    return render(request, 'viewcomplaint.html', {'userdict': userdict})


def complaint_del(request, pk):
    rid = complaint.objects.get(id=pk)
    rid.delete()
    userdict = complaint.objects.all()
    return render(request, 'viewcomplaint.html', {'userdict': userdict})



#
# def insertlogin(request):
#     if (request.method == "POST"):
#         s1 = request.POST.get("t1")
#         s2 = request.POST.get("t2")
#         s3 = request.POST.get("t3")
#         userlogin.objects.create(  username=s1,  password=s2, utype=s3)
#         return render(request, "login.html")
#     return render(request,"login.html")

def viewlogin(request):
    userdict = userlogin.objects.all()
    return  render(request,"viewlogin.html",{'userdict':userdict})

def login_del(request,pk):
    rid=userlogin.objects.get(id=pk)
    rid.delete()
    userdict=userlogin.objects.all()
    return render(request,'viewlogin.html',{'userdict':userdict})

def insertrentdetails(request):
    if(request.method =="POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        rentdetails.objects.create(rent_id=s1,  car_id=s2, rateper_km=s3, driver_charges=s4)
        return render(request, "rentdetails.html")
    return render(request, "rentdetails.html")

def viewrentdetails(request):
    userdict = rentdetails.objects.all()
    return render(request, 'viewrentdetails.html', {'userdict': userdict})


def rentdetails_del(request, pk):
    rid = rentdetails.objects.get(id=pk)
    rid.delete()
    userdict = rentdetails.objects.all()
    return render(request, 'viewrentdetails.html', {'userdict': userdict})



def inserttripchart(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.POST.get("t8")
        s9 = request.POST.get("t9")
        tripchart.objects.create( booking_id=s1, cust_id=s2, driver_name=s3, start_date=s4, start_km=s5, end_date=s6, end_km=s7, total_kms=s8, total_days=s9)
        return render(request, "tripchart.html")
    return render(request, "tripchart.html")

def viewtripchart(request):
    userdict = tripchart.objects.all()
    return render(request, 'viewtripchart.html', {'userdict': userdict})


def tripchart_del(request, pk):
    rid = tripchart.objects.get(id=pk)
    rid.delete()
    userdict = tripchart.objects.all()
    return render(request, 'viewtripchart.html', {'userdict': userdict})


def adminhome(request):
    return render(request,template_name="admin_home.html")

def index(request):
    return render(request,'index.html')

def signin(request):
    if request.method == "POST":
        s1 = request.POST.get("t1")
        request.session['username'] = s1
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        ucheck = userlogin.objects.filter(username=s1).count()
        if ucheck >= 1:
            udata = userlogin.objects.get(username=s1)
            upass = udata.password
            utype = udata.utype
            if upass == s2 and utype==s3:
                if utype == "admin":
                    return render(request, 'admin_home.html')
                if utype == "user":
                    return render(request, 'user_home.html')
            else:
                return render(request, 'login.html', {'msg': 'invalid password'})
        else:
            return render(request, 'login.html', {'msg': 'invalid username'})
    return render(request,"login.html")

def logcheck(request):
    if request.method == "POST":
        s1 = request.POST.get("t1")
        request.session['username'] = s1
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        ucheck = userlogin.objects.filter(username=s1).count()
        if ucheck >= 1:
            udata = userlogin.objects.get(username=s1)
            upass = udata.password
            utype = udata.utype
            if upass == s2 and utype==s3:
                if utype == "admin":
                    return render(request, 'admin_home.html')
                if utype == "user":
                    return render(request, 'user_home.html')
            else:
                return render(request, 'login.html', {'msg': 'invalid password'})
        else:
            return render(request, 'login.html', {'msg': 'invalid username'})
    return render(request,"login.html")


def newuser(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        userlogin.objects.create(  username=s1,  password=s2, utype=s3)
        return render(request, "newuser.html")
    return render(request,"newuser.html")





def sendpass(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        udata = userlogin.objects.get(username=s1)
        upass = udata.passwordcd
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('pshreeshail629@gmail.com', 'cavx iyck kgay pwhh')
        mail.sendmail('pshreeshail629@gmail.com', s1, upass)
        mail.close()
        return render(request, "login.html")
    return render(request, "forgotpassword.html")


def user_home(request):
    return render(request,"user_home.html")









