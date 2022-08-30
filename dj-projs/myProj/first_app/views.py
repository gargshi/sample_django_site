from distutils.command.build_scripts import first_line_re
from re import template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members
# Create your views here.
def index(request):
	#return HttpResponse("Hello World.") #display to user
	# template = loader.get_template("first.html")
	# return HttpResponse(template.render())
	mymembers=Members.objects.all().values()
	template=loader.get_template('index.html')
	context = {
		'mm' : mymembers,
	}
	return HttpResponse(template.render(context,request))

def add(request): #view for add to database template
	template=loader.get_template('add.html')
	return HttpResponse(template.render({},request))

def addrecord(request):
	x=request.POST['first']
	y=request.POST['last']
	member=Members(first_name=x,last_name=y)
	member.save()
	return HttpResponseRedirect(reverse('index'))

def delete(request,id):
	member = Members.objects.get(id=id)
	member.delete()
	return HttpResponseRedirect(reverse('index'))

def update(request,id):
	try:
		mymember=Members.objects.get(id=id)
	except Exception as e:
		print("error: "+e)
	template=loader.get_template('update.html')
	context={
		'mymember': mymember,
	}
	return HttpResponse(template.render(context,request))

def updaterecord(request,id):
	f=request.POST['first']
	l=request.POST['last']
	member=Members.objects.get(id=id)
	member.first_name=f
	member.last_name=l
	member.save()
	return HttpResponseRedirect(reverse('index'))