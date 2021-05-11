from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return f'{self.id}| {self.name}'


class Candidate(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    skills = models.ManyToManyField(Skill, null=True, blank=True, related_name='candidates')

    def __str__(self):
        return f'{self.id}| {self.title}'


class Job(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    skill = models.ForeignKey(Skill, null=False, blank=False, related_name='jobs', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.id}| {self.title}'
