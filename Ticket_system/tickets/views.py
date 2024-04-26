from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TicketForm
from .models import Ticket

def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tickets')
    else:
        form = TicketForm()
    return render(request, 'tickets/create_ticket.html', {'form': form})

def list_tickets(request):
    open_tickets = Ticket.objects.filter(status='Open')
    closed_tickets = Ticket.objects.filter(status='Closed')
    return render(request, 'tickets/list_tickets.html', {'open_tickets': open_tickets, 'closed_tickets': closed_tickets})

def view_edit_ticket(request, ticket_id):
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
    if request.method == 'POST':
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        category = request.POST.get('category')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        tickets = Ticket.objects.filter(phone=phone, email=email, category=category, creation_date__range=(start_date, end_date))
        # tickets = Ticket.objects.filter(phone=phone, email=email, category=category)
        return render(request, 'tickets/search_results.html', {'tickets': tickets})
    return render(request, 'tickets/search_ticket.html')

