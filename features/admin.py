from django.contrib import admin
from.models import *
from django_summernote.models import Attachment
from django.contrib.auth.models import Group
from django_summernote.admin import SummernoteModelAdmin



# Register your models here.
admin.site.unregister(Attachment)
admin.site.unregister(Group)
admin.site.unregister(User)

class BlogAdmin(SummernoteModelAdmin):
    list_display = ('title', 'created')
    summernote_fields = ('blog',) 
admin.site.register(Blog,BlogAdmin)

admin.site.register(CompanySetup)
admin.site.register(Contact)
admin.site.register(Partner)
admin.site.register(Slider)

class ProjectAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',) 
admin.site.register(Project,ProjectAdmin)