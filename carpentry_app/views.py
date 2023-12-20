from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import ProductImage, Testimonial
from .forms import ContactForm

def index(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'index.html', {'testimonial':testimonials})

def gallery(request):
    images = ProductImage.objects.all()
    return render(request, 'gallery.html', {'images': images})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance = form.save()
            # Send email
            subject = 'New Inquiry'
            message = f'Name: {contact_instance.name}\nEmail: {contact_instance.email}\nPhone: {contact_instance.phone}\nAddress: {contact_instance.address}\nDescription: {contact_instance.description}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.NOTIFY_EMAIL]  # Replace with your email
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)
            print("email send successfully")
            return redirect('/')  # Create a success page

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
