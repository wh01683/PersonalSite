from django.db import models
from django.utils import timezone
import datetime


class Project(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    date_started = models.DateField()
    date_completed = models.DateField(null=True)

    def __str__(self):
        return self.title

    def was_recently_completed(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=180)


class Skill(models.Model):
    name = models.CharField(max_length=50)
    rating = models.FloatField(default=1)

    def __str__(self):
        return self.name


class ProjectSkillList(models.Model):
    skills_used = models.ManyToManyField(Project, through='ProjectSkill')


class ProjectSkill(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    skill_list = models.ForeignKey(ProjectSkillList, on_delete=models.CASCADE)
    reason_used = models.CharField(max_length=300)

    def __str__(self):
        return self.project.__str__() + " required " + self.skill.__str__()
