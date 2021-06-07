from django.db import models

CHOICE = (
    ('RVCE', 'RVCE'),
    ('BMS', 'BMS')
)

class Event(models.Model):
    name = models.CharField(max_length=300)
    option = models.CharField(max_length=500, choices=CHOICE, null=True, blank=True)
    number = models.IntegerField(default=4, help_text='just a random number', null=True, blank=True)
    data = models.DateTimeField(blank=True, null=True)
    ambassodor = models.BooleanField(default=True)

    def __str__(self):
        return self.name
