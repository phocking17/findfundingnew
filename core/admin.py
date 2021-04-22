from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(Tag)
admin.site.register(Tag_Type)
admin.site.register(Technology_Tag)

admin.site.register(Organization)
admin.site.register(Contact)
admin.site.register(Program)
admin.site.register(Award)
admin.site.register(Response)