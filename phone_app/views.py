<<<<<<< HEAD
from django.shortcuts import render,redirect,get_object_or_404
from .models import Phone
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from .forms import  SearchForm
from .models import Grp
from .forms import DocumentForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
@login_required(login_url="signup")
def contacts(request,grp_id = ''):
        form = SearchForm()
        if grp_id:
            group_id=get_object_or_404(Grp,pk=grp_id)
            contacts=Phone.objects.all().filter(user=request.user).filter(group=group_id)
            groups=Grp.objects.all().filter(user=request.user)
            return render(request,'phone/index.html',{'contacts':contacts,'form':form,'groups':groups,'grp_id':group_id.id})

        else:
            contacts=Phone.objects.all().filter(user=request.user)
            paginator = Paginator(contacts, 2)
            page = request.GET.get('page')
            try:
                contacts = paginator.page(page)
            except PageNotAnInteger:
                contacts = paginator.page(1)
            except EmptyPage :
                contacts = paginator.page(paginator.num_pages)
            groups=Grp.objects.all().filter(user=request.user)
            return render(request,'phone/index.html',{'contacts':contacts,'form':form,'groups':groups , 'page':page})


from haystack.query import SearchQuerySet

def post_search(request):
    form = SearchForm()
    groups=Grp.objects.all().filter(user=request.user)

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd =form.cleaned_data
            results = SearchQuerySet().models(Phone).filter(content=cd['query']).load_all()
            total_results = results.count()
        return render(request , 'phone/index.html',{'form':form , 'cd':cd , 'results':results,'contacts':results ,'groups':groups , 'total_results': total_results})
    return render(request , 'phone/index.html', {'form':form , })




@login_required(login_url="signup")
def contacts_all(request):
        groups=Grp.objects.all().filter(user=request.user)
        contacts=Phone.objects.all().filter(user=request.user)
        return render(request,'phone/index.html',{'contacts':contacts,'groups':groups})


@login_required(login_url="signup")
def delete(request,contact_id,grp_id = ''):
        contact=get_object_or_404(Phone,pk=contact_id)
        Phone.objects.filter(id=contact.id).delete()
        if grp_id:
            return redirect('/contacts/'+str(grp_id)+'/')
        else:
            return redirect('/contacts/')




@login_required(login_url="signup")
def update(request,contact_id):
    if request.method=='POST':
            contact=get_object_or_404(Phone,pk=contact_id)
            if request.POST['name'] and request.POST['number'] and request.POST['group']  :

                group=Grp.objects.get(id=request.POST['group'])
                Phone.objects.filter(pk=contact_id).update(name=request.POST['name'],number=request.POST['number'],group=group)
                return redirect('/contacts/')
            else:
                groups=Grp.objects.all().filter(user=request.user)
                return render(request,'phone/add.html',{'error':'All field are required','groups':groups})


    else:
            contact=get_object_or_404(Phone,pk=contact_id)
            groups=Grp.objects.all().filter(user=request.user)
            return render(request,'phone/update.html',{'groups':groups,'contact':contact})






def signup(request):
    if request.method=='POST':
        if request.POST['password']==request.POST['confirm']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'phone/signup.html',{'error':'user alredy'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'],email=request.POST['email'] ,password=request.POST['password'])
                auth.login(request,user)
                return redirect('/contacts/')
        else:
            return render(request,'phone/signup.html',{'error':'password must be match'})



    else:
        return render(request,'phone/signup.html')

@login_required(login_url="signup")
def add(request):

    if request.method=='POST':
        grps=Grp.objects.all().filter(user=request.user)
        if request.POST['name'] and request.POST['number'] and request.POST['group']  :
            phone=Phone()
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                phone.document = form.cleaned_data['document']
            phone.name=request.POST['name']
            phone.number=request.POST['number']
            phone.group=Grp.objects.get(id=request.POST['group'])
            phone.user=request.user
            phone.save()
            return redirect('/contacts/')
        else:

            groups=Grp.objects.all().filter(user=request.user)
            return render(request,'phone/add.html',{'error':'All field are required','groups':groups})

    else:
        form = DocumentForm()

        groups=Grp.objects.all().filter(user=request.user)
        return render(request,'phone/add.html',{'groups':groups,'form': form})


@login_required(login_url="signup")
def add_grp(request):

    if request.method=='POST':
        if request.POST['name'] :
            grp=Grp()
            grp.name=request.POST['name']
            grp.user=request.user
            grp.save()
            return redirect('/contacts/')
        else:

            groups=Grp.objects.all().filter(user=request.user)
            return render(request,'phone/add_grp.html',{'error':'All field are required','groups':groups})

    else:
        groups=Grp.objects.all().filter(user=request.user)
        return render(request,'phone/add_grp.html',{'groups':groups})


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



from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect

from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts

class GenerateRandomUserView(FormView):
    template_name = 'phone/generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('users_list')
=======
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
            contacts=Phone.objects.all().filter(user=request.user).filter(group=group_id)
            groups=Grp.objects.all().filter(user=request.user)
            return render(request,'phone/index.html',{'contacts':contacts,'groups':groups,'grp_id':group_id.id})

        else:
            contacts=Phone.objects.all().filter(user=request.user)
            groups=Grp.objects.all().filter(user=request.user)
            return render(request,'phone/index.html',{'contacts':contacts,'groups':groups})



@login_required(login_url="signup")
def contacts_all(request):
        groups=Grp.objects.all().filter(user=request.user)
        contacts=Phone.objects.all().filter(user=request.user)
        return render(request,'phone/index.html',{'contacts':contacts,'groups':groups})


@login_required(login_url="signup")
def delete(request,contact_id,grp_id = ''):
        contact=get_object_or_404(Phone,pk=contact_id)
        Phone.objects.filter(id=contact.id).delete()
        if grp_id:
            return redirect('/contacts/'+str(grp_id)+'/')
        else:
            return redirect('/contacts/')




@login_required(login_url="signup")
def update(request,contact_id):
    if request.method=='POST':
            contact=get_object_or_404(Phone,pk=contact_id)
            if request.POST['name'] and request.POST['number'] and request.POST['group']  :

                group=Grp.objects.get(id=request.POST['group'])
                Phone.objects.filter(pk=contact_id).update(name=request.POST['name'],number=request.POST['number'],group=group)
                return redirect('/contacts/')
            else:
                groups=Grp.objects.all().filter(user=request.user)
                return render(request,'phone/add.html',{'error':'All field are required','groups':groups})


    else:
            contact=get_object_or_404(Phone,pk=contact_id)
            groups=Grp.objects.all().filter(user=request.user)
            return render(request,'phone/update.html',{'groups':groups,'contact':contact})






def signup(request):
    if request.method=='POST':
        if request.POST['password']==request.POST['confirm']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'phone/signup.html',{'error':'user alredy'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'],email=request.POST['email'] ,password=request.POST['password'])
                auth.login(request,user)
                return redirect('/contacts/')
        else:
            return render(request,'phone/signup.html',{'error':'password must be match'})



    else:
        return render(request,'phone/signup.html')

@login_required(login_url="signup")
def add(request):

    if request.method=='POST':
        grps=Grp.objects.all().filter(user=request.user)
        if request.POST['name'] and request.POST['number'] and request.POST['group']  :
            phone=Phone()
            phone.name=request.POST['name']
            phone.number=request.POST['number']
            phone.group=Grp.objects.get(id=request.POST['group'])
            phone.user=request.user
            phone.save()
            return redirect('/contacts/')
        else:

            groups=Grp.objects.all().filter(user=request.user)
            return render(request,'phone/add.html',{'error':'All field are required','groups':groups})

    else:
        groups=Grp.objects.all().filter(user=request.user)
        return render(request,'phone/add.html',{'groups':groups})


@login_required(login_url="signup")
def add_grp(request):

    if request.method=='POST':
        if request.POST['name'] :
            grp=Grp()
            grp.name=request.POST['name']
            grp.user=request.user
            grp.save()
            return redirect('/contacts/')
        else:

            groups=Grp.objects.all().filter(user=request.user)
            return render(request,'phone/add_grp.html',{'error':'All field are required','groups':groups})

    else:
        groups=Grp.objects.all().filter(user=request.user)
        return render(request,'phone/add_grp.html',{'groups':groups})


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
>>>>>>> 2a6c62489d1acf598d77c6946474d1a50c5119bc
