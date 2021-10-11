from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Contact
import datetime
from django.http.response import HttpResponse
from django.core.mail import send_mail

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        sem = request.POST.get('sem')
        yes = request.POST.get('yes')
        no = request.POST.get('no')
        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.subject = subject
        contact.message = message
        contact.sem = sem
        contact.yes = yes
        contact.no = no
        contact.save()
        messages.success(request, 'Thanks for Sending us quote, we will get back to you with 24hours')
        return redirect('contact')
    return render(request, 'contact-us.html')


def success(request):
    return render(request, 'success.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def projects(request):
    return render(request, 'projects.html')


def faq(request):
    return render(request, 'faq.html')


def team(request):
    return render(request, 'team.html')


def more(request):
    return render(request, 'more-about-us.html')


def advisory(request):
    return render(request, 'advisory.html')


def digital(request):
    return render(request, 'digital.html')


def data(request):
    return render(request, 'data.html')


def design(request):
    return render(request, 'design.html')


def it(request):
    return render(request, 'it.html')


def training(request):
    return render(request, 'training.html')


def content(request):
    return render(request, 'content.html')


def terms(request):
    return render(request, 'terms.html')


def privacy(request):
    return render(request, 'privacy.html')


def boost(request):
    return render(request, 'boost.html')


def mobile(request):
    return render(request, 'mobile.html')


def cyber(request):
    return render(request, 'cyber.html')


def software(request):
    return render(request, 'software.html')


def team_detail(request):
    return render(request, 'team-detail.html')


def team_detail_kingsley(request):
    return render(request, 'team-detail-kingsley.html')


def team_dan(request):
    return render(request, 'team-dan.html')


def team_ify(request):
    return render(request, 'team-ify.html')


def team_timi(request):
    return render(request, 'team-timi.html')


def team_ndeya(request):
    return render(request, 'team-ndeya.html')


def team_victor(request):
    return render(request, 'team-victor.html')


def team_ben(request):
    return render(request, 'team-ben.html')


def team_bode(request):
    return render(request, 'team-bode.html')


def team_adrar(request):
    return render(request, 'team-adrar.html')


def SetCookie(response, key, value, days_expire=7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  # one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
        "%a, %d-%b-%Y %H:%M:%S GMT",
    )
    response.set_cookie(
        key,
        value,
        max_age=max_age,
        expires=expires,

    )


def GetCookie(request):
    bookname = request.COOKIES['bookname']
    return HttpResponse(f'The book name is: {bookname}')


def animate(request):
    return render(request, 'animate.html')


def pricing(request):
    return render(request, 'pricing.html')


def pricing_main(request):
    return render(request, 'pricing-main.html')


def send_request(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        budget = request.POST.get('budget')
        network = request.POST.get('network')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'phone': phone,
            'budget': budget,
            'network': network,
            'message': message
        }
        message = '''
        New message: {}
        phone: {}
        budget: {}
        network: {}
        
        From: {}
        '''.format(data['message'], data['phone'], data['budget'], data['network'], data['email'])
        send_mail(data['subject'], message, '', ['info@bluwire-il.com'])

        return redirect('success-page')
    else:
        return render(request, 'mass.html', {})


# def send_request(request):
#     form = ContactForm()
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = f'Message from {form.cleaned_data["name"]}'
#             message = form.cleaned_data["message"]
#             sender = form.cleaned_data["email"]
#             recipients = ['info@bluwire-il.com']
#             try:
#                 send_mail(subject, message, sender, recipients, fail_silently=True)
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found')
#             return render(request, 'success.html')
#     return render(request, 'mass.html', {'form': form})


def success_main(request):
    return render(request, 'success.html')


def site_price(request):
    return render(request, 'site-price.html')


def site_main(request):
    return render(request, 'site-main.html')


def site_maint(request):
    return render(request, 'site-maint.html')


def send_request1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        budget = request.POST.get('budget')
        website = request.POST.get('website')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'phone': phone,
            'budget': budget,
            'website': website,
            'message': message
        }
        message = '''
        New message: {}
        phone: {}
        budget: {}
        website: {}

        From: {}
        '''.format(data['message'], data['phone'], data['budget'], data['website'], data['email'])
        send_mail(data['subject'], message, '', ['info@bluwire-il.com'])

        return redirect('success-page')
    else:
        return render(request, 'mass1.html', {})
