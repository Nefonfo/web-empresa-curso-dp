from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # ENVIAR CORREO Y REDIRECCIONAR
            email = EmailMessage(
                'La Caffetiera: Nuevo Mensaje',
                'De {} <{}> \n\nEscribio:\n\n{}'.format(name, email, content),
                'no-reply@inbox.mailtrap.io',
                ['victorarmenta30@gmail.com'],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact') + '?ok')
            except:
                # Algo No ha ido bien, redirecciona Fail
                return redirect(reverse('contact') + '?fail')
    return render(request, "contact/contact.html", {'form': contact_form})