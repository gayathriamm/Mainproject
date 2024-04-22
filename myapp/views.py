from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect





import json
from web3 import Web3, HTTPProvider
blockchain_address = 'http://127.0.0.1:7545'
web3 = Web3(HTTPProvider(blockchain_address))
web3.eth.defaultAccount = web3.eth.accounts[0]

compiled_contract_path = 'C:\\crwdbc\\build\\contracts\\Crowdfunding.json'
deployed_contract_addressa = web3.eth.accounts[0]
print(deployed_contract_addressa)



from myapp.models import*

def home(request):

    return  render(request,"admin/home.html")

def login(request):
    return render(request, 'Login_index.html')

def login_post(request):
    uname=request.POST['name']
    pswrd=request.POST['password']

    log=Login.objects.filter(Name=uname,Password=pswrd)
    if log.exists():
        log1=Login.objects.get(Name=uname,Password=pswrd)
        request.session['lid']=log1.id
        if log1.Usertype=='admin':
            return HttpResponse('''<script>alert('Logined');window.location='/myapp/home/'</script>''')
        elif log1.Usertype == 'user':
            return redirect('/myapp/farmer_home/')
        elif log1.Usertype == 'statecenter':
            # name=statecenter.objects.get(LOGIN_id=log1.LOGIN_id).name

            return redirect('/myapp/statecenter_home/')
        elif log1.Usertype == 'supplyco':
            return redirect('/myapp/supplyco_home/')
        else:
            return HttpResponse('''<script>alert("invalid credentials");window.location="/myapp/login/"</script>''')
    else:
        return HttpResponse('''<script>alert("invalid credentials");window.location="/myapp/login/"</script>''')




def admin_add_ration_product(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    return  render(request,"admin/add_ration_product.html")
def admin_add_ration_product_post(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    name= request.POST["textfield"]
    Quantity= request.POST["textfield2"]

    r = Rationproducts.objects.filter(productname__icontains=name)
    if r.exists():
        return HttpResponse(
            "<Script>alert('Already Added');window.location='/myapp/admin_add_ration_product/'</script>"
        )


    r=Rationproducts()
    r.productname= name
    r.quantity= Quantity
    r.save()
    return  HttpResponse(
        "<Script>alert('Product added successfully');window.location='/myapp/admin_add_ration_product/'</script>"
    )
def admin_view_rationproduct(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    r=Rationproducts.objects.all()
    return render(request,"admin/view_ration_product.html",{'data':r})
def admin_delete_product(request,id):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    Rationproducts.objects.filter(id=id).delete()
    return HttpResponse(
        "<script>alert('Product deleted successfully');window.location='/myapp/admin_view_rationproduct/'</script>"
    )
def admin_edit_product(request,id):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    r=Rationproducts.objects.get(id=id)
    return  render(request,"admin/edit_ration_product.html",{'data':r})

def admin_edit_product_post(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    name = request.POST["textfield"]
    id = request.POST["id"]
    # r=Rationproducts.objects.filter(productname__icontains=name)
    # if r.exists():
    #     return HttpResponse(
    #         "<Script>alert('Already Added');window.location='/myapp/admin_add_ration_product/'</script>"
    #     )
    r = Rationproducts.objects.get(id=id)
    r.productname = name
    r.save()
    return HttpResponse(
        "<Script>alert('Product edit successfully');window.location='/myapp/admin_add_ration_product/'</script>"
    )



def admin_add_ration_card(request):
    return  render(request,"admin/add_ration_card_type.html")
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
def admin_add_ration_card_post(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    name= request.POST["textfield"]
    r=Rationcardtype()
    r.cardtype= name
    r.save()
    return  HttpResponse(
        "<Script>alert('Card type added successfully');window.location='/myapp/admin_add_ration_card/'</script>"
    )
def admin_view_rationcardtype(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    r=Rationcardtype.objects.all()
    return render(request,"admin/view_ration_cardtype.html",{'data':r})
def admin_delete_ration_cardtype(request,id):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    Rationcardtype.objects.filter(id=id).delete()
    return HttpResponse(
        "<script>alert('Deleted successfully');window.location='/myapp/admin_view_rationcardtype/'</script>"
    )
def admin_edit_ration_cardtype(request,id):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    r=Rationcardtype.objects.get(id=id)
    return  render(request,"admin/edit_ration_card_type.html",{'data':r})
def admin_edit_rationcardtype_post(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    name = request.POST["textfield"]
    id = request.POST["id"]
    r = Rationcardtype.objects.get(id=id)
    r.productname = name
    r.save()
    return HttpResponse(
        "<Script>alert('Edited successfully');window.location='/myapp/admin_view_rationcardtype/'</script>"
    )


def admin_add_statecenters(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    import datetime
    d = datetime.date.today()
    return render(request,"admin/add_statecenters.html", {'dt':str(d)})

def admin_add_statecenters_post(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    name= request.POST["name"]
    phone= request.POST["phone"]
    email= request.POST["email"]
    estd= request.POST["estd"]
    state= request.POST["state"]




    l=Login()
    l. Name= email
    l.Password= phone
    l.Usertype="statecenter"
    l.save()
    u=statecenter()
    u.LOGIN=l
    u.Name= name
    u.Phone=phone
    u.Email= email
    u.estd= estd
    u.state= state
    u.LOGIN= l
    u.save()

    return  HttpResponse("<script>alert('State center added successfully');window.location='/myapp/admin_add_statecenters/'</script>")


def admin_view_statecenters(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    res= statecenter.objects.all()

    return render(request,"admin/view-statecenters.html",{'data':res})

def admin_delete_statecenters(request,id):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    statecenter.objects.filter(id=id).delete()

    return  HttpResponse(
        "<script>alert('Delete successfully');window.location='/myapp/admin_view_statecenters/'</script>"
    )

def admin_edit_statcenteres(request,id):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    res=statecenter.objects.get(id=id)

    return render(request,"admin/edit_statecenters.html",{'data':res})


def admin_edit_statecenters_post(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    id = request.POST["id"]
    name = request.POST["name"]
    phone = request.POST["phone"]
    email = request.POST["email"]
    estd = request.POST["estd"]
    state = request.POST["state"]

    u = statecenter.objects.get(id=id)
    u.Name = name
    u.Phone = phone
    u.Email = email
    u.estd = estd
    u.state = state
    u.save()

    return HttpResponse(
        "<script>alert('State center edited successfully');window.location='/myapp/admin_view_statecenters/'</script>")


def cng_pswrd(request):
    if request.session['lid']=='':
        return redirect('/myapp/login/')
    return render(request, 'admin/change_password.html')

def cng_pswrd_pst(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    pswd = request.POST['password']
    npswd = request.POST['n_password']
    cpswd = request.POST['c_password']
    log = Login.objects.filter(Password=pswd)
    if log.exists():
        log1 = Login.objects.get(Password=pswd, id=request.session['lid'])
        if npswd == cpswd:
            log1 = Login.objects.filter(Password=pswd, id=request.session['lid']).update(Password=cpswd)
            return HttpResponse('''<script>alert("successfully changed");window.location="/myapp/login/"</script>''')

        else:
            return HttpResponse(
                '''<script>alert("password incorrect");window.location="/myapp/cng_pswrd/"</script>''')
    else:
        return HttpResponse(
            '''<script>alert("password incorrect");window.location="/myapp/cng_pswrd/"</script>''')





def f_cng_pswrd(request):
    if request.session['lid']=='':
        return redirect('/myapp/login/')
    return render(request, 'farmer/change_password.html')

def f_cng_pswrd_pst(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    pswd = request.POST['password']
    npswd = request.POST['n_password']
    cpswd = request.POST['c_password']
    log = Login.objects.filter(Password=pswd)
    if log.exists():
        log1 = Login.objects.get(Password=pswd, id=request.session['lid'])
        if npswd == cpswd:
            log1 = Login.objects.filter(Password=pswd, id=request.session['lid']).update(Password=cpswd)
            return HttpResponse('''<script>alert("successfully changed");window.location="/myapp/login/"</script>''')

        else:
            return HttpResponse(
                '''<script>alert("password incorrect");window.location="/myapp/cng_pswrd/"</script>''')
    else:
        return HttpResponse(
            '''<script>alert("password incorrect");window.location="/myapp/cng_pswrd/"</script>''')




def state_cng_pswrd(request):
    if request.session['lid']=='':
        return redirect('/myapp/login/')
    return render(request, 'state/change_password.html')

def state_cng_pswrd_pst(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    pswd = request.POST['password']
    npswd = request.POST['n_password']
    cpswd = request.POST['c_password']
    log = Login.objects.filter(Password=pswd)
    if log.exists():
        log1 = Login.objects.get(Password=pswd, id=request.session['lid'])
        if npswd == cpswd:
            log1 = Login.objects.filter(Password=pswd, id=request.session['lid']).update(Password=cpswd)
            return HttpResponse('''<script>alert("successfully changed");window.location="/myapp/login/"</script>''')

        else:
            return HttpResponse(
                '''<script>alert("password incorrect");window.location="/myapp/cng_pswrd/"</script>''')
    else:
        return HttpResponse(
            '''<script>alert("password incorrect");window.location="/myapp/cng_pswrd/"</script>''')



def supplyco_cng_pswrd(request):

    if request.session['lid']=='':
        return redirect('/myapp/login/')
    return render(request, 'supplyco/change_password.html')

def supplyco_cng_pswrd_pst(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    pswd = request.POST['password']
    npswd = request.POST['n_password']
    cpswd = request.POST['c_password']
    log = Login.objects.filter(Password=pswd)
    if log.exists():
        log1 = Login.objects.get(Password=pswd, id=request.session['lid'])
        if npswd == cpswd:
            log1 = Login.objects.filter(Password=pswd, id=request.session['lid']).update(Password=cpswd)
            return HttpResponse('''<script>alert("successfully changed");window.location="/myapp/login/"</script>''')

        else:
            return HttpResponse(
                '''<script>alert("password incorrect");window.location="/myapp/cng_pswrd/"</script>''')
    else:
        return HttpResponse(
            '''<script>alert("password incorrect");window.location="/myapp/cng_pswrd/"</script>''')










def user_home(request):
    if request.session['lid']=='':
        return redirect('/myapp/login/')
    return render(request, 'user/user_home.html')

#
def register(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    return render(request, 'user/sindex.html')

def register_pst(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    dob = request.POST['dob']
    gender = request.POST['gender']
    place = request.POST['place']
    post = request.POST['post']
    district = request.POST['district']
    state = request.POST['state']
    pin = request.POST['pin']
    photo = request.FILES['photo']
    password = request.POST['password']
    c_password = request.POST['cpassword']

    if password==c_password:

        lobj = Login()
        lobj.Name = email
        lobj.Password = c_password
        lobj.Usertype = "User"
        lobj.save()

        robj = User()
        robj.Name = name
        robj.Phone = phone
        robj.Email = email
        robj.Dob = dob
        robj.Gender = gender
        robj.Place = place
        robj.Post = post
        robj.District = district
        robj.State = state
        robj.Pin = pin

        from datetime import datetime
        date = datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ".jpg"
        fs = FileSystemStorage()
        fs.save(date, photo)
        path = fs.url(date)
        robj.Photo = path

        robj.Photo = path
        # robj.Password = password
        # robj.C_password = c_password
        robj.LOGIN=lobj
        robj.save()

        return HttpResponse('''<script>alert("Registered Succesfully");window.location="/myapp/login/"</script>''')

    else:
        return HttpResponse('''<script>alert("Mismatched");window.location="/myapp/register/"</script>''')

#
def u_cng_pswrd(request):
    if request.session['lid']=='':
        return redirect('/myapp/login/')
    return render(request, 'user/u_change_pswrd.html')

def u_cng_pswrd_pst(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    pswd = request.POST['password']
    npswd = request.POST['n_password']
    cpswd = request.POST['c_password']
    log = Login.objects.filter(Password=pswd)
    if log.exists():
        log1 = Login.objects.get(Password=pswd, id=request.session['lid'])
        if npswd == cpswd:
            log1 = Login.objects.filter(Password=pswd, id=request.session['lid']).update(Password=cpswd)
            return HttpResponse('''<script>alert("successfully changed");window.location="/myapp/login/"</script>''')

        else:
            return HttpResponse(
                '''<script>alert("password incorrect");window.location="/myapp/u_cng_pswrd/"</script>''')
    else:
        return HttpResponse(
            '''<script>alert("password incorrect");window.location="/myapp/u_cng_pswrd/"</script>''')






def user_send_complaint(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    return render(request,'user/send_complaint.html')

def user_send_complaint_post(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    complaint = request.POST['textarea']

    cobj = Complaints()
    cobj.Compliant = complaint
    cobj.Replay = 'pending'

    cobj.LOGIN_id =request.session['lid']
    from datetime import datetime
    cobj.Date = datetime.now().strftime('%Y-%m-%d')
    cobj.Status = 'pending'
    cobj.save()
    return HttpResponse('''<script> alert("COMPLAINT SEND!!!");window.location="/myapp/user_send_complaint/"</script>''')
#
def view_reply(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    data = Complaints.objects.filter(LOGIN__id=request.session['lid'])
    return render(request,'user/view_reply.html',{'dt':data})

def view_reply_post(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    frm = request.POST['textfield']
    to = request.POST['textfield2']
    data = Complaints.objects.filter(LOGIN__id=request.session['lid'],Date__range=[frm,to])
    return render(request, 'user/view_reply.html', {'dt': data})
def logout(request):
    request.session['lid'] = ''
    return render(request,'Login_index.html')




def statecenter_home(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    return render(request,'stategovernment/aindex.html')



def stategovernement_adddistrict(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    return render(request,"stategovernment/add_district.html")

def stategovernement_adddistrict_post(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    dist=request.POST["textfield"]
    d=District()
    d.district=dist
    d.STATECENTER= statecenter.objects.get(LOGIN_id= request.session['lid'])
    d.save()
    return HttpResponse("<script>alert('District added successfully');window.location='/myapp/stategovernement_adddistrict/'</script>")


def state_view_district(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    d=District.objects.filter(STATECENTER= statecenter.objects.get(LOGIN_id=request.session['lid']))

    return render(request,"stategovernment/view_district.html",{'data':d})



def state_delete_district(request,id):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    District.objects.filter(id=id).delete()

    return HttpResponse("<script>alert('District deleted successfully');window.location='/myapp/state_view_district/'</script>")


def stategovernement_addarea(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    res=District.objects.all()
    return render(request,"stategovernment/add_area.html",{'data': res})


def stategovernemnet_area_post(request):
     if request.session['lid'] == "":
        return redirect('/myapp/login/')
     district= request.POST["district"]
     area= request.POST["textfield"]

     a=Area()
     a.DISTRICT_id= district
     a.area= area
     a.save()

     return HttpResponse(
         "<script>alert('Area added successfully');window.location='/myapp/stategovernement_addarea/'</script>"
     )

def stategovernement_scheme(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    res=District.objects.all()
    return render(request,"stategovernment/add_scheme.html",{'data': res})


def stategovernemnet_scheme_post(request):
     if request.session['lid'] == "":
        return redirect('/myapp/login/')
     Title= request.POST["textfield"]
     Description= request.POST["textfield2"]

     a=Scheme()
     a.scheme= Title
     a.discription= Description
     a.save()

     return HttpResponse(
         "<script>alert('Scheme added successfully');window.location='/myapp/stategovernement_scheme/'</script>"
     )


def state_view_scheme(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    data=Scheme.objects.all()

    return render(request,"stategovernment/View_scheme.html",{'data':data})


def state_view_area(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    data=Area.objects.all()

    return render(request,"stategovernment/View_area.html",{'data':data})



def state_delete_area(request,id):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    Area.objects.filter(id=id).delete()

    return HttpResponse("<script>alert('Deleted successfully');window.location='/myapp/state_view_area/'</script>")


def state_delete_scheme(request,id):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    Scheme.objects.filter(id=id).delete()

    return HttpResponse("<script>alert('Deleted successfully');window.location='/myapp/state_view_scheme/'</script>")



def state_addsupplyco(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    area= Area.objects.all()
    import datetime
    d = datetime.date.today()
    return render(request,"stategovernment/add_supplyco_office.html",{'data': area, 'dt':str(d) })


def state_addsuplycopost(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    offcode= request.POST["name"]
    area= request.POST["area"]
    email= request.POST["email"]
    estd= request.POST["estd"]
    phone= request.POST["phone"]

    r = suplyco.objects.filter(offcode__icontains=offcode)
    if r.exists():
        return HttpResponse(
            "<Script>alert('Already Added');window.location='/myapp/state_addsupplyco/'</script>"
        )


    s=suplyco()
    s.offcode= offcode
    s.AREA_id=area
    s.email= email
    s.estd=estd
    s.phone=phone


    l=Login()
    l.Name= email
    l.Password= phone
    l.Usertype="supplyco"
    l.save()

    s.LOGIN=l
    s.save()

    return HttpResponse(
        "<script>alert('Added successfully');window.location='/myapp/state_addsupplyco/'</script>"
    )


def view_supplyco(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    s=suplyco.objects.filter(AREA__DISTRICT__STATECENTER__LOGIN_id= request.session['lid'])
    return render(request,"stategovernment/view_supplyco.html",{'data':s})



def delete_supplyco(request,id):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    suplyco.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('Supplyco deleted successfully');window.location='/myapp/view_supplyco/'</script>")



def state_add_rationcard(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    data=Rationcardtype.objects.all()
    area=Area.objects.all()
    return render(request,"stategovernment/add_card.html",{'data':data,'area':area})

def state_add_rationcard_post(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    name=request.POST["name"]
    gender=request.POST["gender"]
    dob=request.POST["dob"]
    file=request.FILES["file"]
    hname=request.POST["hname"]
    place=request.POST["place"]
    post=request.POST["post"]
    district=request.POST["district"]
    state=request.POST["state"]
    email=request.POST["email"]
    phone=request.POST["phone"]
    religion=request.POST["religion"]
    cast=request.POST["cast"]
    cardtype=request.POST["cardtype"]
    area=request.POST["area"]
    adhar=request.POST["adhar"]
    from datetime import  datetime
    fname= datetime.now().strftime("%Y%m%d%H%M%f")+".jpg"
    fs=FileSystemStorage()
    fs.save(fname,file)
    s=cardholder()
    s.file= fs.url(fname)
    s.name= name
    s.gender= gender
    s.dob=dob
    s.hname=hname
    s.place=place
    s.post=post
    s.district=district
    s.state=state
    s.email=email
    s.phone=phone
    s.religion=religion
    s.cast=cast
    s.CARDTYPE_id=cardtype
    s.AREA_id=area
    s.adhar=adhar
    s.save()
    return HttpResponse(
        "<script>alert('Added successfully');window.location='/myapp/state_add_rationcard/'</script>"
    )

def view_card(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    s=cardholder.objects.filter(AREA__DISTRICT__STATECENTER__LOGIN_id= request.session['lid'])
    return render(request,"stategovernment/View_card.html",{'data':s})

def searchcard(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    name= request.POST["name"]
    s = cardholder.objects.filter(AREA__DISTRICT__STATECENTER__LOGIN_id=request.session['lid'],name__icontains=name)
    return render(request, "stategovernment/View_card.html", {'data': s})

#############supplyco
def supplyco_view_card(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    s=cardholder.objects.filter(AREA__DISTRICT__STATECENTER__LOGIN_id= request.session['lid'])
    s=cardholder.objects.all()
    return render(request,"supplyco/View_card.html",{'data':s})


def supplyco_searchcard(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    name= request.POST["name"]
    s = cardholder.objects.filter(name__icontains=name)
    # s = cardholder.objects.filter(AREA__DISTRICT__STATECENTER__LOGIN_id=request.session['lid'],name__icontains=name)
    return render(request, "supplyco/View_card.html", {'data': s})

def user_signup(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    data=Rationcardtype.objects.all()
    area=Area.objects.all()
    return render(request,"farmer/signup.html",{'data':data,'area':area})


def user_signup_post(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    name=request.POST["name"]
    gender=request.POST["gender"]
    dob=request.POST["dob"]
    file=request.FILES["file"]
    hname=request.POST["hname"]
    place=request.POST["place"]
    post=request.POST["post"]
    district=request.POST["district"]
    state=request.POST["state"]
    email=request.POST["email"]
    phone=request.POST["phone"]
    adhar=request.POST["adhar"]
    password=request.POST["password"]

    from datetime import  datetime
    fname= datetime.now().strftime("%Y%m%d%H%M%f")+".jpg"
    fs=FileSystemStorage()
    fs.save(fname,file)
    s=user()
    s.file= fs.url(fname)
    s.name= name
    s.gender= gender
    s.dob=dob
    s.hname=hname
    s.place=place
    s.post=post
    s.district=district
    s.state=state
    s.email=email
    s.phone=phone
    l=Login()
    l.Name=email
    l.Password= password
    l.Usertype="user"
    l.save()

    s.adhar=adhar
    s.LOGIN=l
    s.save()
    return HttpResponse(
        "<script>alert('Added successfully');window.location='/myapp/login/'</script>"
    )

def user_viewprofile(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    res= user.objects.get(LOGIN_id= request.session['lid'])
    return render(request,"farmer/profile.html",{'data':res})

def farmer_home(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    return render(request,"farmer/home.html")

def supplyco_home(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    return render(request,"supplyco/home.html")

def stategovt_send_notice_to_collect_crops(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    res=Rationproducts.objects.all()

    return render(request,"stategovernment/send_notice_to_collect_crops.html",{'data':res})





def stategovt_send_notice_to_collect_crops_post(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    itemname= request.POST["itemname"]
    title= request.POST["textfield"]
    message= request.POST["message"]
    Quantity= request.POST["Quantity"]
    price= request.POST["price"]
    date= request.POST["date"]

    n=notification()

    n.PRODUCT_id= itemname
    n.title=title
    n.message=message
    n.quantiy=Quantity
    n.price=price
    from datetime import  datetime
    n.createddate= datetime.now()
    n.lastdate= date
    n.STATECENTRE= statecenter.objects.get(LOGIN_id= request.session["lid"])
    n.save()

    return HttpResponse("<script>alert('Notification sent successfully');window.location='/myapp/stategovt_send_notice_to_collect_crops/'</script>")


def state_view_notification(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    n=notification.objects.filter(STATECENTRE__LOGIN_id= request.session['lid'])
    return render(request,"stategovernment/view_notification.html",{'data':n})

def state_view_notification_search(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    f=request.POST["textfield"]
    t=request.POST["textfield2"]
    n=notification.objects.filter(STATECENTRE__LOGIN_id= request.session['lid'],lastdate__range=[f,t])
    return render(request,"stategovernment/view_notification.html",{'data':n})

def state_delete_notification(request,id):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    notification.objects.filter(id=id).delete()

    return HttpResponse(
        "<script>alert('Notification deleted successfully');window.location='/myapp/state_view_notification/'</script>")



def farmer_view_notification(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')


    f=notification.objects.all()

    return render(request, "farmer/view_notification.html", {'data':f})


def farmer_add_items(request,nid,pid):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    return render(request,"farmer/additems.html",{'nid':nid,'pid':pid})


def farmer_add_item_post(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    nid=request.POST["nid"]
    pid=request.POST["pid"]
    qty=request.POST["textfield2"]


    its=item_user()
    its.USER= user.objects.get(LOGIN_id=request.session['lid'])
    its.status="pending"
    its.save()

    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
        print(contract_abi)
    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()

    try:

        from datetime import  datetime
        message2 = contract.functions.additem(str(its.id),str(request.session["lid"]),str(pid),str(nid),str(qty), datetime.now().strftime("%Y-%m-%d"),"item").transact()

        return HttpResponse("<script>alert('Item added successfully');window.location='/myapp/farmer_view_notification/'</script>")
    except:

        return HttpResponse(
            "<script>alert('Failed to add item');window.location='/myapp/farmer_view_notification/'</script>")






def add_family_member(request,id):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    request.session["id"]= id

    return render(request,"stategovernment/add_family_member.html")


def add_family_member_post(request):
    name= request.POST["name"]
    gender= request.POST["gender"]
    dob= request.POST["dob"]
    adhar= request.POST["adhar"]
    relation= request.POST["relation"]


    f=familymember()
    f.name= name
    f.CARDHOLDER_id= request.session["id"]
    f.gender= gender
    f.dob=dob
    f.adhar=adhar
    f.relation=relation
    f.save()

    return HttpResponse(
        "<script>alert('Family member added successfully');window.location='/myapp/view_card/#mu-features'</script>"
    )








def view_family_member(request,id):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    res= familymember.objects.filter(CARDHOLDER_id= id)
    return render(request,"stategovernment/View_familymember.html",{'data': res})





def supplyco_add_transactions(request,rationid):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    p=Rationproducts.objects.all()

    request.session['rationid']=str(rationid)

    return render(request,"supplyco/add_transactions.html",{'data':p})



def supplyco_add_trans_post(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    qty= request.POST["textfield"]
    pid= request.POST["pid"]


    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
        print(contract_abi)
    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()

    try:

        from datetime import  datetime
        message2 = contract.functions.addtrans(str(blocknumber),str(pid), datetime.now().strftime("%Y-%m-%d"),qty,request.session['rationid'],"trans").transact()

        return HttpResponse("<script>alert('Transactions added  successfully');window.location='/myapp/supplyco_add_transactions/"+request.session['rationid']+"'</script>")
    except:

        return HttpResponse(
            "<script>alert('Failed to add transaction');window.location='/myapp/supplyco_add_transactions/"+request.session['rationid']+"'</script>")






def supplyco_view_notification(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    # n=notification.objects.filter(STATECENTRE__LOGIN_id= request.session['lid'])
    n=notification.objects.all()
    return render(request,"supplyco/view_notification.html",{'data':n})

def supplyco_view_notification_search(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    f=request.POST["textfield"]
    t=request.POST["textfield2"]
    n=notification.objects.filter(STATECENTRE__LOGIN_id= request.session['lid'],lastdate__range=[f,t])
    return render(request,"supplyco/view_notification.html",{'data':n})


def supplyco_view_notification_response(request,id):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)

    blocknumber = web3.eth.get_block_number()
    print(blocknumber)

    l=[]
    for i in range(blocknumber,2, -1):
        a = web3.eth.get_transaction_by_block(i, 0)
        decoded_input = contract.decode_function_input(a['input'])
        c = decoded_input[1]
        print(c)
        if c['typea'] == "item":
            print("ins1",c['productida'], str(id))
            if c['notida'] == str(id):
                ns=notification.objects.get(id=c['notida'])

                sk=item_user.objects.get(id=c['ida'])
                l.append({'date': c['datea'],'qtya':c['quantitya'], 'no': ns, 'status': sk.status })


    print(l,"helllooooooooooooooooooooooooooooooooooo")
    return render(request,"supplyco/view_notification_response.html",{'data':l})



def supplyco_view_notification_response(request,id):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')



    request.session['ids']=id

    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)

    blocknumber = web3.eth.get_block_number()
    print(blocknumber)

    l=[]
    for i in range(blocknumber,2, -1):
        a = web3.eth.get_transaction_by_block(i, 0)
        decoded_input = contract.decode_function_input(a['input'])
        c = decoded_input[1]
        print(c)
        if c['typea'] == "item":
            print("ins1",c['productida'], str(id))
            if c['notida'] == str(id):

                ss=item_user.objects.get(id= c['ida'])
                ns=notification.objects.get(id=c['notida'])
                l.append({'date': c['datea'],'qtya':c['quantitya'], 'no': ns , 'status':ss.status, 'id':ss.id})


    print(l)
    return render(request,"supplyco/view_notification_response.html",{'data':l})



def forwardtostate(request,id):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    item_user.objects.filter(id=id).update(status='forwarded')

    return HttpResponse("<script>alert('Forwarded');window.location='/myapp/supplyco_view_notification_response/"+request.session['ids']+"'</script>")

def statecenter_view_notification_response(request,id):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    request.session["ids"]=id


    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi -
        # necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)

    blocknumber = web3.eth.get_block_number()
    print(blocknumber)

    l=[]
    for i in range(blocknumber,2, -1):
        a = web3.eth.get_transaction_by_block(i, 0)
        decoded_input = contract.decode_function_input(a['input'])
        c = decoded_input[1]
        print(c)
        if c['typea'] == "item":
            print("ins1",c['productida'], str(id))
            if c['notida'] == str(id):
                ns=notification.objects.get(id=c['notida'])

                s=item_user.objects.get(id=c['ida'])


                l.append({'date': c['datea'],'qtya':c['quantitya'], 'no': ns,'status':s.status, 'id':s.id })


    print(l)
    return render(request,"stategovernment/view_notification_response.html",{'data':l})



def ApprovePayment(request, id):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    item_user.objects.filter(id=id).update(status='Approved')

    return HttpResponse(
        "<script>alert('Approved');window.location='/myapp/statecenter_view_notification_response/" + request.session[
            'ids'] + "'</script>")


def admin_product_assign_card(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    c=Rationcardtype.objects.all()

    s=Rationproducts.objects.all()

    return render(request,"admin/assign_product_to_rationcard.html",{'c':c,'p':s})


def admin_product_assign_Card_post(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    cid= request.POST["c"]
    pid= request.POST["pid"]

    ms=ration_product_cardtype()
    ms.CARDTYPE_id= cid
    ms.RATIONPRODUCT_id=pid
    ms.save()

    return HttpResponse("")


    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)

    blocknumber = web3.eth.get_block_number()
    print(blocknumber)

    l=[]
    for i in range(blocknumber,2, -1):
        a = web3.eth.get_transaction_by_block(i, 0)
        decoded_input = contract.decode_function_input(a['input'])
        c = decoded_input[1]
        print(c)
        if c['typea'] == "item":
            print("ins1",c['productida'], str(id))
            if c['notida'] == str(id):
                ns=notification.objects.get(id=c['notida'])
                l.append({'date': c['datea'],'qtya':c['quantitya'], 'no': ns })


    print(l)
    return render(request,"supplyco/view_notification_response.html",{'data':l})



def user_view_itemss(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)

    blocknumber = web3.eth.get_block_number()
    print(blocknumber)

    l=[]
    for i in range(blocknumber,2, -1):
        a = web3.eth.get_transaction_by_block(i, 0)
        decoded_input = contract.decode_function_input(a['input'])
        c = decoded_input[1]
        print(c)
        if c['typea'] == "item":
            print("ins1",c['productida'], str(id))
            if c['lida'] == str(request.session["lid"]):
                ns=notification.objects.filter(id=c['notida'])
                if ns.exists():
                    ns=ns[0]

                d=item_user.objects.filter(id=c['ida'])
                if d.exists():
                    d=d[0].status
                else:
                    d='pending'


                l.append({'date': c['datea'],'qtya':c['quantitya'], 'no': ns, 'status':d })
    print(l)
    return render(request,"farmer/view_notification_response.html",{'data':l})

def farmer_view_scheme(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    data=Scheme.objects.all()

    return render(request,"farmer/View_scheme.html",{'data':data})



def farmer_view_transactions(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)

    blocknumber = web3.eth.get_block_number()
    print(blocknumber)

    l=[]
    for i in range(blocknumber,2, -1):
        a = web3.eth.get_transaction_by_block(i, 0)
        decoded_input = contract.decode_function_input(a['input'])
        c = decoded_input[1]
        print(c)
        if c['typea'] == "trans":
            print("ins1",c['itemida'], str(id))
            # if c['lida'] == str(request.session["lid"]):
            ns=Rationproducts.objects.get(id=c['itemida'])
            l.append({'date': c['datea'],'qtya':c['qtya'], 'no': ns })
    print(l)
    return render(request,"farmer/view_trans.html",{'data':l})



def supplyco_view_transactions(request,id):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)

    blocknumber = web3.eth.get_block_number()
    print(blocknumber)

    l=[]
    for i in range(blocknumber,2, -1):
        a = web3.eth.get_transaction_by_block(i, 0)
        decoded_input = contract.decode_function_input(a['input'])
        c = decoded_input[1]
        print(c)
        if c['typea'] == "trans":
            print("ins1",c['itemida'], str(id))
            # if c['lida'] == str(request.session["lid"]):
            ns=Rationproducts.objects.filter(id=c['itemida'])
            if ns.exists():
                ns = ns[0]
                l.append({'date': c['datea'],'qtya':c['qtya'], 'no': ns })
    print(l)
    return render(request,"supplyco/view_trans.html",{'data':l})



def user_Send_complaint(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    return render(request,"farmer/sendcomlaint.html")


def user_sendomplaint_post(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    complaint= request.POST["textfield2"]

    from datetime import  datetime
    c=Complaints()
    c.Date= datetime.now()
    c.Compliant=complaint
    c.Replay="pending"
    c.Status="pending"
    c.USER= user.objects.get(LOGIN_id= request.session['lid'])
    c.save()

    return HttpResponse("<Script>alert('Complaint sent successfully');window.location='/myapp/user_Send_complaint/'</script>")



def user_view_reply(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    c=Complaints.objects.filter(USER__LOGIN_id=request.session['lid'])

    return render(request,"farmer/viewreply.html",{'data':c})


def reply(request,id):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')

    request.session["id"]=id

    return render(request,"admin/sendreply.html")


def replypost(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    replys= request.POST["reply"]

    c=Complaints.objects.get(id= request.session["id"])

    c.Status="Replied"
    c.Replay= replys
    c.save()

    return HttpResponse("<script>alert('Reply sent successfully');window.location='/myapp/admin_view_reply/'</script>")


def admin_view_reply(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    c=Complaints.objects.all()

    return render(request,"admin/complaints.html",{'data':c})

def admin_view_reply_post(request):
    if request.session['lid'] == "":
        return redirect('/myapp/login/')
    f=request.POST["f"]
    t=request.POST["t"]
    c=Complaints.objects.filter(Date__range=[f,t])

    return render(request,"admin/complaints.html",{'data':c})