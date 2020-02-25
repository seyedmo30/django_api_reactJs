from django.shortcuts import render,redirect,get_object_or_404
from .models import Phone
from .models import Grp
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
@login_required(login_url="signup")
def contacts(request,grp_id = ''):
        if grp_id:
            group_id=get_object_or_404(Grp,pk=grp_id)
            contacts=Phone.objects..raw('select * from phone_phone where user_id = {} and group_id = {}'.format(user.id,grp_id))
            groups=Grp.objects.raw('select * from phone_grp where user_id = {}'.format(user.id))
            return render(request,'phone/index.html',{'contacts':contacts,'groups':groups,'grp_id':group_id.id})

        else:
            contacts=Phone.objects.raw('select * from phone_phone where user_id = {} '.format(user.id))
            groups=Grp.objects.raw('select * from phone_grp where user_id = {}'.format(user.id))
            return render(request,'phone/index.html',{'contacts':contacts,'groups':groups})




@login_required(login_url="signup")
def delete(request,contact_id,grp_id = ''):
        contact=get_object_or_404(Phone,pk=contact_id)
        Phone.objects.raw('delete from phone_phone where user_id = {}'.format(contact.id))
        if grp_id:
            return redirect('/contacts/'+str(grp_id)+'/')
        else:
            return redirect('/contacts/')




@login_required(login_url="signup")
def update(request,contact_id):
    if request.method=='POST':
            contact=get_object_or_404(Phone,pk=contact_id)
            if request.POST['name'] and request.POST['number'] and request.POST['group']  :
                group=Grp.objects.raw('select * from phone_grp where user_id = {}'.format(user.id))
                Phone.objects.raw('update phone_phone set name = {} and number = {} and group_id = {} where user_id = {} '.format(request.POST['name'],request.POST['number'],request.POST['group'] user.id))
                return redirect('/contacts/')
            else:
                group=Grp.objects.raw('select * from phone_grp where user_id = {}'.format(user.id))
                return render(request,'phone/add.html',{'error':'All field are required','groups':groups})


    else:
            contact=get_object_or_404(Phone,pk=contact_id)
            group=Grp.objects.raw('select * from phone_grp where user_id = {}'.format(user.id))
            return render(request,'phone/update.html',{'groups':groups,'contact':contact})






def signup(request):
    if request.method=='POST':
        if request.POST['password']==request.POST['confirm']:
            try:
                user=User.objects.raw('select * from auth_user where username = {}'.format(request.POST['name']))
                return render(request,'phone/signup.html',{'error':'user alredy'})
            except User.DoesNotExist:
                user=User.objects.raw('insert into auth_user (username , email , password) values ({},{},{})'.format(request.POST['name'],request.POST['email'],Hash(request.POST['name'])))
                execute(user)
                return redirect('/contacts/')
        else:
            return render(request,'phone/signup.html',{'error':'password must be match'})



    else:
        return render(request,'phone/signup.html')

@login_required(login_url="signup")
def add(request):

    if request.method=='POST':
        group=Grp.objects.raw('select * from phone_grp where user_id = {}'.format(user.id))
        if request.POST['name'] and request.POST['number'] and request.POST['group']  :
            user=User.objects.raw('insert into phonr_phone (name , number , group_id , user_id) values ({},{},{},{})'.format(request.POST['name'],request.POST['number'],request.POST['group.id'],user.user_id ))
            execute(user)
            return redirect('/contacts/')
        else:

            group=Grp.objects.raw('select * from phone_grp where user_id = {}'.format(user.id))
            return render(request,'phone/add.html',{'error':'All field are required','groups':group})

    else:
        group=Grp.objects.raw('select * from phone_grp where user_id = {}'.format(user.id))
        return render(request,'phone/add.html',{'groups':group})


@login_required(login_url="signup")
def add_grp(request):

    if request.method=='POST':
        if request.POST['name'] :
            group=Grp.objects.raw('insert into phonr_grp (name , user_id) values ({},{})'.format(request.POST['name'],user.user_id ))
            execute(group)

            return redirect('/contacts/')
        else:

            groups=Grp.objects.all().filter(user=request.user)
            return render(request,'phone/add_grp.html',{'error':'All field are required','groups':groups})

    else:
        group=Grp.objects.raw('select * from phone_grp where user_id = {}'.format(user.id))
        return render(request,'phone/add_grp.html',{'groups':group})


def login (request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'] , password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('/contacts/')
        else:
            return render(request,'phone/login.html',{'error':'username or password is incorrect'})
    else:
        return render(request,'phone/login.html')



def logout (request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')

    else:
        return render(request,'phone/login.html')
