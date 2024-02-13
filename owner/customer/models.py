from django.db import models



class userlogin(models.Model):
    username=models.CharField(max_length=200,blank=True)
    password=models.CharField(max_length=50,blank=True)
    utype=models.CharField(max_length=50,blank=True)


class carbooking(models.Model):
    booking_id=models.CharField(max_length=200,null=True,blank=True)
    cust_id=models.CharField(max_length=200,null=True,blank=True)
    car_id=models.CharField(max_length=200,null=True,blank=True)
    booking_date=models.DateField(null=True,blank=True)
    reg_date=models.DateField(null=True,blank=True)
    to_place=models.CharField(max_length=200,null=True,blank=True)
    no_of_days=models.CharField(max_length=150,null=True,blank=True)
    rent_id=models.CharField(max_length=20,null=True,blank=True)
    status=models.CharField(max_length=200,null=True,blank=True)

class cardetails(models.Model):
    car_id=models.CharField(max_length=250,null=True,blank=True)
    company=models.CharField(max_length=200,null=True,blank=True)
    make=models.CharField(max_length=200,null=True,blank=True)
    reg_no=models.CharField(max_length=200,null=True,blank=True)
    fuel_type=models.CharField(max_length=150,null=True,blank=True)
    capacity=models.CharField(max_length=100,null=True,blank=True)
    photo=models.FileField(upload_to='documents/')




class complaint(models.Model):
    cust_id=models.CharField(max_length=20,null=True,blank=True)
    trip_id=models.CharField(max_length=20,null=True,blank=True)
    complaint_type=models.CharField(max_length=200,null=True,blank=True)
    details=models.CharField(max_length=200,null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    status=models.CharField(max_length=200,null=True,blank=True)

class addcustomer(models.Model):
    cust_id=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=200,null=True,blank=True)
    mobile_no=models.CharField(max_length=20,null=True,blank=True)
    email_id=models.EmailField(max_length=20,null=True,blank=True)
    cust_type=models.CharField(max_length=100,null=True,blank=True)

class adddriver(models.Model):
    driver_id=models.CharField(max_length=20,null=True,blank=True)
    name=models.CharField(max_length=150,null=True,blank=True)
    address=models.CharField(max_length=200,null=True,blank=True)
    mobile_no=models.CharField(max_length=20,null=True,blank=True)
    reference_given=models.CharField(max_length=200,null=True,blank=True)
    liscense_no=models.CharField(max_length=150,null=True,blank=True)
    liscense_type=models.CharField(max_length=200,null=True,blank=True)
    expire_date=models.DateField(null=True,blank=True)
    aadhar_no=models.CharField(max_length=20,null=True,blank=True)



class rentdetails(models.Model):
    rent_id=models.CharField(max_length=20,null=True,blank=True)
    car_id=models.CharField(max_length=20,null=True,blank=True)
    rateper_km=models.CharField(max_length=100,null=True,blank=True)
    driver_charges=models.CharField(max_length=200,null=True,blank=True)

class tripchart(models.Model):
    booking_id=models.CharField(max_length=20,null=True,blank=True)
    cust_id=models.CharField(max_length=20,null=True,blank=True)
    driver_name=models.CharField(max_length=70,null=True,blank=True)
    start_date=models.DateField(null=True,blank=True)
    start_km=models.CharField(max_length=200,null=True,blank=True)
    end_date=models.DateField(null=True,blank=True)
    end_km=models.CharField(max_length=200,null=True,blank=True)
    total_kms=models.CharField(max_length=200,null=True,blank=True)
    total_days=models.CharField(max_length=100,null=True,blank=True)

