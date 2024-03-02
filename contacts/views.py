from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Send confirmation email
            send_confirmation_email(form.cleaned_data['email'])
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contactapp/contact.html', {'form': form})

def send_confirmation_email(email):
    subject = 'Thank you for contacting us!'
    message = 'Hi there,\n\nThank you for reaching out to us. We appreciate you getting in touch and will respond to your message shortly.\n\nBest regards,\nThe My Contact Form Team'
    send_mail(subject, message, 'nayaksubhrajit84@gmial.com', [email])  # Replace with your email inside the 'your email'

