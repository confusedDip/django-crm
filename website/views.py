from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, AddRecordForm
from .models import Record


# Create your views here.
def home(request):
    records = Record.objects.all()

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "Error logging in, please try again!")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully logged out!")

    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request, username=username, password=password)
            login(request, user)

            messages.success(request, "You have successfully registered!")
            return redirect('home')

    else:
        form = SignUpForm()
    return render(request, 'register.html', {"form": form})


def view_record(request, pk):
    if request.user.is_authenticated:

        record = Record.objects.get(id=pk)
        return render(request, 'record.html', {"record": record})

    else:
        messages.success(request, "You must be logged in to view this page!")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, f"Record {pk} has been successfully deleted!")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to view this page!")
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)

    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()

                first_name = form.cleaned_data["first_name"]
                last_name = form.cleaned_data["last_name"]
                email = form.cleaned_data["email"]
                phone = form.cleaned_data["phone"]
                address = form.cleaned_data["address"]
                city = form.cleaned_data["city"]
                state = form.cleaned_data["state"]
                zipcode = form.cleaned_data["zipcode"]

                messages.success(request, "Record Added Sucessfully!")
                return redirect('home')

        return render(request, "add_record.html", {"form": form})

    else:

        messages.success(request, "You must be logged in to view this page!")
        return redirect("home")
