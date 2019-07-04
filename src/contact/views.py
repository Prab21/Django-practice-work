from django.shortcuts import render

from .forms import contactForm
from django.conf import settings 
from django.core.mail import send_mail
# Create your views here.

def contact(request):
	#title='Contact'
	form=contactForm(request.POST or None)
	#context={'title' : title,'f}

	if form.is_valid():
		print(request.POST)
		name= form.cleaned_data['name']
		comment=form.cleaned_data['comment']
		subject= 'message from my gmail'
		message='%s %s' %(comment,name)
		emailForm= form.cleaned_data['email']
		emailTo=[settings.EMAIL_HOST_USER]
		send_mail(subject,message,emailForm,emailTo,fail_silently=True)

		# print (form.cleaned_data['email'])
		
		
	context=locals()
	template='contact.html'
	return render(request,template,context)

# def contact(request):
# 	context=locals()
# 	template='contact.html's
# 	return render(request,template,context)
