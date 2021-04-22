from django import forms
from .models import *
class CustomMultipleModelChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        if isinstance(obj, Tag):
            return obj.name
        if isinstance(obj, Technology_Tag):
            return obj.name

'''
class OrganizationInformationForm(forms.Form):
	name = forms.CharField(label="Organization Name", max_length=200)
	street = forms.CharField(label="Street Address", max_length=300)
	city=forms.CharField(label="City", max_length=100)
	state= forms.CharField(label="State", max_length=2)
	zipcode = forms.CharField(label="ZipCode", max_length=5)
	description = forms.CharField(label="Please describe your organization:", max_length=1000)
	tags=CustomMultipleModelChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Tag.objects.filter())
	overall_tags = CustomMultipleModelChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Arching_Tag.objects.filter())

	website=forms.URLField(label="Website URL", max_length=500)
	phone_number=forms.CharField(label="Phone Number", max_length=12)
	email = forms.EmailField(label="Email", max_length=254)
	org_image = forms.ImageField(label="Organization Image")

	contact_name = forms.CharField(label="Contact Name", max_length=125)
	contact_phone_number=forms.CharField(label="Contact Phone Number", max_length=12)
	contact_email = forms.EmailField(label="Contact Email", max_length=254)
	contact_image = forms.ImageField(label="Contact Image")
'''