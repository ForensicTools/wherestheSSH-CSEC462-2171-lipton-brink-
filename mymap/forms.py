from django import forms
from django.contrib.auth.models import User
import datetime

#Create dateform
class DateForm(forms.Form):
    startdate = forms.DateField(initial=datetime.date.today, required = True)
    enddate = forms.DateField(initial=datetime.date.today, required = True)