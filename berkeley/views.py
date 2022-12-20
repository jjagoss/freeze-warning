from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .input_form import EmailForm
from .models import Subscriber

def index(request):

    if request.method == 'POST':

        form = EmailForm(request.POST)

        if form.is_valid():
            subscriber = Subscriber()
            subscriber.first_name = form.cleaned_data['first_name']
            subscriber.last_name = form.cleaned_data['last_name']
            subscriber.email_address = form.cleaned_data['email_address']

            subscriber.save()

            return HttpResponse("Thanks")

    else:

        form = EmailForm()
    
    return render(request, 'berkeley/index.html', {'form': form})