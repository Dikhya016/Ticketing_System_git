# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import TicketForm
from .models import Ticket

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

name = ''


@login_required(login_url='login')
def HomePage(request):
    return render(request, 'tickets/index.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'tickets/signup.html')


def LoginPage(request):
    global name
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            name = username
            # return redirect('open_index')
            return render(request, 'tickets/index.html')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    if (len(name) > 0):
        return render(request, 'tickets/index.html')

    return render(request, 'tickets/login.html')


def LogoutPage(request):
    global name
    name = ''
    logout(request)
    return redirect('login')


def open_index(request):
    return render(request, 'tickets/index.html')


def create_ticket(request):
    global name
    if(len(name) == 0):
        return redirect('login')
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tickets')
    else:
        form = TicketForm()
    return render(request, 'tickets/create_ticket.html', {'form': form})


def list_tickets(request):
    global name
    if (len(name) == 0):
        return redirect('login')

    technical_tickets = Ticket.objects.filter(category='Technical')
    service_tickets = Ticket.objects.filter(category='Service')
    billing_tickets = Ticket.objects.filter(category='Billing')

    return render(request, 'tickets/list_tickets.html', {'TT': technical_tickets, 'ST': service_tickets, 'BT': billing_tickets})


def view_edit_ticket(request, ticket_id):
    global name
    if (len(name) == 0):
        return redirect('login')
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('list_tickets')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'tickets/view_edit_ticket.html', {'form': form, 'ticket': ticket})


def search_ticket(request):
    global name
    if(len(name) == 0):
        return redirect('login')
    if request.method == 'POST':
        # phone = request.POST.get('phone')
        email = request.POST.get('email')
        category = request.POST.get('category')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        tickets = Ticket.objects.filter(
            email=email, category=category, creation_date__range=(start_date, end_date))
        # tickets = Ticket.objects.filter(phone=phone, email=email, category=category)
        return render(request, 'tickets/search_results.html', {'tickets': tickets})
    return render(request, 'tickets/search_ticket.html')
