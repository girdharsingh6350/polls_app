from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    Question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')

    def was_published_recntly(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.Question_text


class choice(models.Model):
    Question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    vote = models.IntegerField(default =0)

    def __str__(self):
        return self.choice_text