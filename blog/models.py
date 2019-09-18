from django.db import models
from django.forms import ModelForm
from django.utils import timezone


class Event(models.Model):
    author = models
    title = models.CharField(max_length=200)
    text = models.TextField()
    begin_date = models.DateTimeField(default=timezone.now)
    complete_day = models.BooleanField(default=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
