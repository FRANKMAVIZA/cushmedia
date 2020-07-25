from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Portfolio, Testimonials, Services
from django.core.mail import EmailMessage
from .form import ContactForm
from django.template.loader import get_template


# Create your views here.

def index(request):
 tests = Testimonials.objects.all()
 dests = Portfolio.objects.all()
 servics = Services.objects.all()
 return render(request,'index.html', {'dests': dests, 'tests' : tests, 'servics' : servics } )


def contactform(request):
 Contact_form = ContactForm

 if request.method == 'POST':
     form = Contact_form(data=request.POST)

     if form.is_valid():
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')

        template = get_template('contact_form.txt')

        context = {
          name: name,
          email: email,
          subject: subject
     }

        content = template.render(context)

        email = EmailMessage(
           "New contact form email",
            content,
            "Cush Media" + '',
            ['mavizatanyaradzwa0@gmail.com'],
            headers={'Reply-To' : email}

     )
        email.send()

        return redirect('/')
 return render(request, 'index.html', {'form': Contact_form})




