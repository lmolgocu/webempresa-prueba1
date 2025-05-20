from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage


# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data = request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name", "")
            user_email = request.POST.get("email", "")
            content = request.POST.get("content", "")
            # Enviamos el correo y lo redireccionamos
            email = EmailMessage(
                subject= "La Caffetiera: Nuevo mensaje de contacto",
                body= "De {} <{}>\n\nEscribio:\n\n{}".format(name, user_email, content),
                from_email= "no-contestar@inbox.mailtrap.io",
                to=["luismortizl1975@gmail.com"],
                reply_to=[user_email]
            )
            try:

                email.send()
                # Todo ha ido bien, redireccionamos a ok
                print("✅ Correo enviado correctamente")
                return redirect(reverse("contact")+"?ok")
            except Exception as e:
                # ha habido un fallo al enviar, redireccionamos falla
                print(f"❌ Error al enviar correo: {e}")
                return redirect(reverse("contact")+"?fail")



    return render(request, "contact/contact.html", {"form": contact_form})

