from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from .form import NewUser, UserMessage
from .models import UsersList, UserMessages


def home(request):
    forms = UserMessage()
    if request.method == 'POST':
        forms = UserMessage(request.POST)
        if forms.is_valid():
            forms.save(commit=True)
            return redirect("/")
        else:
            print("error")
    context = {'forms': forms}
    return render(request, 'index.html', context)


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid username or password")
            return redirect('register')
    else:
        return redirect("/")


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                messages.info(request, "User Created")
                return redirect('register')
        else:
            messages.info(request, "Password doesn't match")
            return redirect("register")
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")


def users(request):
    forms = NewUser()
    if request.method == 'POST':
        forms = NewUser(request.POST)
        if forms.is_valid():
            forms.save(commit=True)
            return redirect("/")
        else:
            print("error")
    context = {'forms': forms}
    return render(request, 'form.html', context)


def view(request):
    print("shflshsklhfskdhfkjsdhfhskdfhkhjdhfskdhfkhskdfhsdjfh")
    details = UsersList.objects.all()
    print("details::::::::::::",details)
    context = {'enq': details}
    return render(request, 'formview.html', context)


def delete(request, id):
    UsersList.objects.get(id=id).delete()
    return redirect('view')


def update(request, id):
    print("kdfskldjfskjdfksjdfklsjf")
    values = UsersList.objects.get(id=id)
    print("2222222222222222222222222222222")
    return render(request, 'update.html', {'form': values})


def updateform(request, id):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    UsersList.objects.filter(id=id).update(first_name=first_name, last_name=last_name, email=email)
    return redirect('view')


def header(request):
    return render(request, 'header.html')
