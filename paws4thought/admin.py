from django.contrib import admin
from .models import Feature, CompanyDetail, TeamMember, TeamDetail
# Register your models here.

admin.site.register(Feature)
admin.site.register(CompanyDetail)
admin.site.register(TeamMember)
admin.site.register(TeamDetail)