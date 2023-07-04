from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Student, Teacher, Classroom, Gradelevel
from simple_history.admin import SimpleHistoryAdmin

class TeacherInline(admin.StackedInline):
    model = Teacher
    can_delete = False #Teacher should not be deletable unless the user is deleted first
    verbose_name_plural = 'Teachers'

class CustomizedUserAdmin(UserAdmin):
    inlines = (TeacherInline, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)


admin.site.register(Classroom)

admin.site.register(Student, SimpleHistoryAdmin)

admin.site.register(Gradelevel)

admin.site.register(Teacher, SimpleHistoryAdmin, inherit = True)