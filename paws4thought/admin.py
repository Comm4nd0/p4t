from django.contrib import admin
from .models import Feature, CompanyPage, TeamMember, TeamPage
# Register your models here.

admin.site.register(Feature)
admin.site.register(CompanyPage)
admin.site.register(TeamMember)
admin.site.register(TeamPage)