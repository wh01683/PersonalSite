from django.contrib import admin
from projects.models import Project, Skill, ProjectSkill
# Register your models here.

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(ProjectSkill)