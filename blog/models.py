from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime


class Event(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    begin_date = models.DateTimeField(default=timezone.now)
    complete_day = models.BooleanField(default=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def create(self, request):
        try:
            post = request.POST
            self.author = request.user
            self.title = post['title']
            self.text = post['text']
            self.begin_date = datetime.fromisoformat(post['begin_date']).isoformat(sep=' ')
            complete_day = 'on' == post.get('complete_day', 'off')
            if not complete_day:
                end_date = post['end_date']
            return True
        except Exception as e:
            print(e)
            return False

    def publish(self):
        self.save()

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['author']