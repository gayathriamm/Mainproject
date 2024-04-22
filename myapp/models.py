from django.db import models

class Login(models.Model):
    Name = models.CharField(max_length=50)
    Password = models.CharField(max_length=10)
    Usertype = models.CharField(max_length=100)

class statecenter(models.Model):
    Name = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    estd = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)

class Rationproducts(models.Model):
    productname=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)

class Rationcardtype(models.Model):
    cardtype=models.CharField(max_length=100)

class District(models.Model):
    district=models.CharField(max_length=100)
    STATECENTER = models.ForeignKey(statecenter, on_delete=models.CASCADE)


class Area(models.Model):
    area = models.CharField(max_length=100)
    DISTRICT= models.ForeignKey(District,on_delete=models.CASCADE)


class suplyco(models.Model):
    offcode= models.CharField(max_length=100)
    AREA= models.ForeignKey(Area,on_delete=models.CASCADE)
    email= models.CharField(max_length=150)
    phone= models.CharField(max_length=50)
    estd= models.CharField(max_length=50)
    LOGIN= models.ForeignKey(Login,on_delete=models.CASCADE)




class cardholder(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    file = models.CharField(max_length=100)
    hname = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    cast = models.CharField(max_length=100)
    CARDTYPE = models.ForeignKey(Rationcardtype, on_delete=models.CASCADE)
    AREA =  models.ForeignKey(Area, on_delete=models.CASCADE)
    adhar = models.CharField(max_length=100)


class familymember(models.Model):
    CARDHOLDER= models.ForeignKey(cardholder,on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    gender= models.CharField(max_length=20)
    dob=models.CharField(max_length=25)
    adhar= models.CharField(max_length=25)
    relation= models.CharField(max_length=25)



class user(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    file = models.CharField(max_length=100)
    hname = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    adhar = models.CharField(max_length=100)
    LOGIN= models.ForeignKey(Login,on_delete=models.CASCADE)






class notification(models.Model):
    PRODUCT= models.ForeignKey(Rationproducts,on_delete=models.CASCADE)
    title=models.CharField(max_length=500)
    message=models.CharField(max_length=500)
    price=models.CharField(max_length=20)
    quantiy=models.CharField(max_length=20)
    lastdate= models.DateField()
    createddate= models.DateField()
    STATECENTRE= models.ForeignKey(statecenter,on_delete=models.CASCADE)


class item_user(models.Model):
    USER= models.ForeignKey(user,on_delete=models.CASCADE)
    status= models.CharField(max_length=50,default="pending")


class ration_product_cardtype(models.Model):

    RATIONPRODUCT= models.ForeignKey(Rationproducts,on_delete=models.CASCADE)
    CARDTYPE=models.ForeignKey(Rationcardtype,on_delete=models.CASCADE)

class Complaints(models.Model):
    Compliant = models.CharField(max_length=200)
    Date = models.DateField()
    Status = models.CharField(max_length=300)
    Replay = models.CharField(max_length=200)
    USER = models.ForeignKey(user, on_delete=models.CASCADE)

class Scheme(models.Model):
     scheme = models.CharField(max_length=200)
     discription = models.CharField(max_length=200)


