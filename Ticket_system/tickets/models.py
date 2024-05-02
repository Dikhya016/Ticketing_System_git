from django.db import models

# Create your models here.
from django.db import models

import datetime


class Ticket(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Closed', 'Closed')
    ]
    CATEGORY = [
        ('Technical', 'Technical'),
        ('Billing', 'Billing'),
        ('Service', 'Service'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    ticket_description = models.TextField()
    category = models.CharField(
        max_length=20, choices=CATEGORY, default='Technical')
    notes = models.TextField(blank=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='Open')
    creation_date = models.DateField(auto_now_add=True)
    last_modified_date = models.DateField(auto_now=True)
    # ticket_modify_time = models.DateTimeField(default=datetime.datetime.now()+datetime.timedelta(minutes=330))
    ticket_modify_time = models.DateTimeField(default=datetime.datetime.now())

    def save(self, *args, **kwargs):
        # Set the timezone to IST before saving

        self.ticket_modify_time = datetime.datetime.now()
        super(Ticket, self).save(*args, **kwargs)

    def __str__(self):
        return self.ticket_description
