from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Project, ProjectSkill, Skill
# Create your views here.


def index(request):
    project_list = Project.objects.order_by('-date_completed')
    context = {
        'project_list': project_list
    }
    return render(request, 'projects/index.html', context)


def detail(request, project_id):
    project_obj = get_object_or_404(Project, pk=project_id)
    project_skill_list = get_list_or_404(ProjectSkill, project=project_obj)
    context = {
        'project': project_obj,
        'project_skill_list': project_skill_list
    }
    return render(request, 'projects/detail.html', context)


def skills(request):
    skill_list = get_list_or_404(Skill)
    context = {
        'skill_list': skill_list,
    }

    return render(request, 'projects/skills.html', context)