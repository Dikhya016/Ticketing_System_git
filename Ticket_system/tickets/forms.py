from django import forms
from .models import Ticket,Note

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('name', 'phone','email','city','state','ticket_description','category','status',)


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['content']
