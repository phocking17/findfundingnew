from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader
import random
from .forms import *
from .models import *



def index(request):
	template=loader.get_template('core/index.html')
	context=dict()
	return HttpResponse(template.render(context, request))


def addtag(request, instance, metatag, addedtag):
	r = Response.objects.get(pk=instance)
	tag = Tag.objects.get(name=addedtag)
	meta = Tag_Type.objects.get(name=metatag)
	r.tags_selected.add(tag)
	r.tags_completed.add(meta)
	return redirect('/aboutme/'+str(instance))


def aboutme(request, instance=None):
	if instance==None:
		r = Response()
		r.save()
		return redirect('aboutme/'+str(r.id))

	else:
		r = Response.objects.get(pk=instance)

		tags_list = Tag_Type.objects.all()
		tags_list = [tag.name for tag in tags_list]

		completed_tags = r.tags_completed.all()
		completed_tags = [tag.name for tag in completed_tags]



		for tag in tags_list:
			if tag not in completed_tags:
				tag_obj = Tag_Type.objects.get(name=tag)

				question = tag_obj.question
				choices = Tag.objects.filter(tag_type__name=tag)

				template=loader.get_template('core/aboutme.html')
				context={
					'question':question,
					'choices':choices,
					'pkid' : r.id,
					'metatag' : tag
					}
				return HttpResponse(template.render(context, request))
		return redirect('../results/custom/'+str(r.id))




def quickfind(request):
	template=loader.get_template('core/quickfind.html')
	context={
		'tags' : [[tags, Tag.objects.filter(tag_type=tags)] for tags in Tag_Type.objects.all()],
		'arching_tag': Technology_Tag.objects.all(),
		}
	return HttpResponse(template.render(context, request))

def results_general(request, arching_name):
	template=loader.get_template('core/results.html')
	org_list = [[org] for org in Program.objects.filter(technology_tags__name=arching_name)]
	if org_list == []:
		org_list =  [[org] for org in Program.objects.filter(affiliations__name=arching_name)]
	context={
		'org_list': org_list,
		'tag':arching_name
	}
	return HttpResponse(template.render(context, request))

def results_tagspecific(request, tag_name,semi_name):
	template=loader.get_template('core/results.html')
	context={
		'org_list': [[org] for org in Program.objects.filter(focus__name=tag_name)],
		'tag':tag_name,
		'seminame':semi_name
	}
	return HttpResponse(template.render(context, request))


def results(request, instance):

	r=Response.objects.get(pk=instance)
	tags = r.tags_selected.all()
	overall_tags = r.overall_tags_selected.all()
	orgs = Program.objects.all()

###################################################################
### Matching Algorithm
	score_dict = {}
	for org in list(orgs):
		score = 0
		division = 0
		for tag in list(tags):
			if tag in list(org.focus.all()):
				score+=1
				division+=1
			else:
				division+=1
		for otag in list(overall_tags):
			if otag in org.technology_tags:
				score+=1
				division+=1
			else:
				division+=1
		fin_score = (score/division)*100
		score_dict[org]=round(fin_score, 2)

	sorted_keys = sorted(score_dict, key=score_dict.get)  # [1, 3, 2]

	sorted_list=[]
	for w in sorted_keys:
		key = w
		val = score_dict[w]
		sorted_list.append([key, val])

	sorted_list.reverse()

############################################################################



	template=loader.get_template('core/results.html')
	context={
		'customcheck':True,
		'org_list':sorted_list,
	}
	return HttpResponse(template.render(context, request))



def all_opportunities(request):
	template=loader.get_template('core/results.html')
	context={
		'org_list':[[org] for org in Program.objects.all()],
		'all':True,
	}
	return HttpResponse(template.render(context, request))

def program(request, pro_name):
	template=loader.get_template('core/program.html')
	pro=Program.objects.get(name=pro_name)
	related_list = [tag.name for tag in pro.technology_tags.all()]
	for org in pro.affiliations.all():
		related_list.append(org)
	context={
		'organization' : pro,
		'affiliations' : pro.affiliations.all(),
		'contact': pro.contact.all(),
		'awards': Award.objects.filter(program=pro),
		'overall_tags' : related_list
	}
	return HttpResponse(template.render(context, request))

def organization(request, org_name):
	template=loader.get_template('core/organization.html')
	org=Organization.objects.get(name=org_name)
	try:
		affiliations = org.affiliations
	except:
		affiliations = None
	context={
		'organization' : org,
		'contact': org.contact.all(),
		'overall_tags' : affiliations,
		'programs' : Program.objects.filter(affiliations=org)
	}
	return HttpResponse(template.render(context, request))

def photo(request,photoname,orgid):
	image_data = open("photos/"+ str(orgid) + "/"+photoname, "rb").read()
	return HttpResponse(image_data, content_type="image/png")

def add_organization(request):
	template=loader.get_template('core/add.html')
	new_form=OrganizationInformationForm()
	context={
		'form':new_form
	}
	return HttpResponse(template.render(context, request))

def organization_completed(request):
	template=loader.get_template('core/add.html')


	
	### Add Org
	name = request.POST['name']
	street = request.POST['street']
	city=request.POST['city']
	state= request.POST['state']
	zipcode = request.POST['zipcode']
	description = request.POST['description']
	tags=request.POST['tags']
	overall_tags = request.POST['overall_tags']

	website=request.POST['website']
	phone_number=request.POST['phone_number']
	email = request.POST['email']
	org_image = request.POST['org_image']

	contact_name = request.POST['contact_name']
	contact_phone_number=request.POST['contact_phone_number']
	contact_email = request.POST['contact_email']
	contact_image = request.POST['contact_image']

	new_obj = Organization.objects.create(name=name, street=street, city=city, state=state, zipcode=zipcode, description=description, tags=tags, overall_tags=overall_tags, website=website, phone_number=phone_number, email=email, org_image=org_image, contact_name=contact_name, contact_email=contact_email, contact_image=contact_image)



	context={
		'org-url': ('/organization'+ name)
	}
	return HttpResponse(template.render(context, request))