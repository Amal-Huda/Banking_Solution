from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import render, redirect, reverse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Districts, Branches,NetBankingCustomer
from .forms import Customerform


# Create your views here.
def Home(request):
    return render(request, 'index.html')


def Login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pword = request.POST.get('pword')
        if not uname or not pword:
            messages.error(request, 'Please enter both username and password.')
            return render(request, 'Login.html')
        user = auth.authenticate(username=uname, password=pword)
        # print(user.is_authenticated, user.username)

        if user is not None and user.is_active:
            if user.check_password(pword):
                auth.login(request, user)
                print(" username", user.username)
                return redirect('/')
            # print(user.is_authenticated, request.user.is_authenticated)
            else:
                messages.error(request, 'Invalid password.')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'Login.html', {'request': request})



def Register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pword = request.POST['pword']
        cpword = request.POST['cpword']
        if not uname or not pword or not cpword:
            messages.error(request, 'Please enter your details')
            return render(request, 'Register.html')
        if pword == cpword:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'username already exists')
                # return redirect('BankingApp:register')
            else:
                user = User.objects.create_user(username=uname, password=pword)
                user.save()
                return redirect('BankingApp:loginn')
        else:
            messages.info(request, 'Passwords are not matching')
            return render('Register.html')
        return redirect('/')
    return render(request, 'Register.html')
def ApplyNet(request):
    districts=Districts.objects.all()
    branches=Branches.objects.all()
    if request.method=='POST':
            name=request.POST.get('name')
            age=request.POST.get('age')
            dob=request.POST.get('bod')
            try:
                birthdate=datetime.strptime(dob, '%Y-%m-%d').date()
            except ValueError:
                # Handle invalid date format (e.g., display an error message)
                return redirect('BankingApp:application')
            gender =request.POST.get('gender')
            print('gender is         -----------------------------------------------------------',gender)
            selected_district=request.POST.get('district')
            district =Districts.objects.get(district=selected_district)
            selected_branch=request.POST.get('branch')
            branch =Branches.objects.get(branch=selected_branch)
            accountype =request.POST.get('account')
            material=request.POST.getlist('material')
            materials=','.join(material)
            print(materials)
            phone=request.POST.get('phone')
            address = request.POST.get('address')
            newregistration=NetBankingCustomer.objects.create(Name=name,BirthDate=birthdate,Gender=gender,Age=age,Account_type=accountype, Materials=materials, District=district,Branch=branch,Address=address,Phone=phone)
            newregistration.save()
            print('registered successfully.................................................')
            return redirect('BankingApp:applicationsuccess')

    return render(request,'ApplyNetBanking.html',{'branches':branches,'districts':districts})

#to fetch branches and pass it to the template without form submission
def fetch_branches(request):
    print((request.method))
    if request.method == 'GET':
        district = request.GET.get('district_id')
        district_selected=Districts.objects.get(district=district)
        district_id=district_selected.pk
        print(district_id)
        try:
            branches = Branches.objects.filter(district_id=district_id)
            print(branches)
            return JsonResponse({'branches': list(branches.values())})
        except Branches.DoesNotExist:
            return JsonResponse({'error': 'Branches not found for the selected district.'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)


def ApplicationSuccess(request):
    message = 'Application Submitted succesfully..'
    return render(request, 'ApplicationAccept.html', {'message': message})


def Logout(request):
    auth.logout(request)
    return redirect('/')
