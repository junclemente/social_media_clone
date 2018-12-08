from django.contrib import admin
from .import models
# Register your models here.


class GroupMemberInline(admin.TabularInLine):
    mode = models.GroupMember


admin.site.register(models.Group)