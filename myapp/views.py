from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect

# For Database
from .models import Students

# For Django Form
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# For Django Messages
from django.contrib import messages

# For Authentication of User for Login
from django.contrib.auth import authenticate, login, logout

# For Provide Restrction using Login Decorator
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def home(request):
    myStudents = Students.objects.all().values()

    content = {
        'title': "Student List",
        "myStudents": myStudents
    }

    # output = ""
    # for i in myStudents:
    #     output += i["firstname"]
    # return HttpResponse(output)

    return render(request, 'home.html', content)


@login_required(login_url="login")
def about(request):
    return render(request, 'about.html', {'title': "About Page"})


@login_required(login_url="login")
def contact(request):
    return render(request, 'contact.html', {'title': "Contact Page"})


@login_required(login_url="login")
def add(request):
    return render(request, "add.html", {"title": "Add New Record"})


@login_required(login_url="login")
def addRecord(request):

    x = request.POST['first']
    y = request.POST['last']

    student = Students(firstname=x, lastname=y)
    student.save()
    return HttpResponseRedirect(reverse('home'))


@login_required(login_url="login")
def delete(request, id):
    student = Students.objects.get(id=id)
    student.delete()
    return HttpResponseRedirect(reverse('home'))


@login_required(login_url="login")
def update(request, id):
    student = Students.objects.get(id=id)

    content = {
        'title': "Update Record",
        'student': student
    }

    return render(request, 'update.html', content)


@login_required(login_url="login")
def updateRecord(request, id):
    student = Students.objects.get(id=id)
    fname = request.POST["first"]
    lname = request.POST["last"]

    student.firstname = fname
    student.lastname = lname

    student.save()
    return HttpResponseRedirect(reverse('home'))


# Authentication Views
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        # Recieve form Data and create USER
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {
            'form': form
        }
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')

        return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


# 404 Page Not Found View
def error_404_view(request):
    return render(request, '404.html')