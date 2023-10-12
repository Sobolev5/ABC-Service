from django.db import models
from django.utils.translation import gettext_lazy as _


class Group(models.Model):
    name = models.CharField(_("Name"), max_length=140, null=True, blank=True)
    members_count = models.IntegerField(default=0)
    verified_members_count = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.name}"


class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=140, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}"