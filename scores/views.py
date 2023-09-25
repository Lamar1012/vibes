from django.shortcuts import render, redirect
from .forms import SubscriberForm
import os
# from twilio.rest import Client
from twilio.rest import Client
from django.conf import settings

# Create your views here.
twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

def landing_page(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)

        if form.is_valid():

            phone_number = form.cleaned_data['phone_number']
            if not phone_number.startswith('+1'):
                phone_number = '+1' + phone_number

            form.save()

            client = Client(settings.TWILIO_ACCOUNT_SID, twilio_auth_token)
            message = client.messages.create(
                body = "\U0001F680 Welcome to V.I.B.E.S Pre-Launch Alerts! \U0001F4F1 \n\nGet ready to be the first to experience local adventures like never before! \n\nStay Tuned for exciting updates. Your input will shape V.I.B.E.S into something amazing!\U0001F4AA\U0001F38A",
                from_ = settings.TWILIO_PHONE_NUMBER,
                to = phone_number
            )
            print(message.sid)
            return redirect("/connect-vibes/")
        else:
            return redirect("/connect-vibes/")
    else:
        form = SubscriberForm()
    context = {'form':form}
    return render(request, 'index.html', context)