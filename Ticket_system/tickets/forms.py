from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('name', 'phone','email','city','state','ticket_description','category','notes','status',)

