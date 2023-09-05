from django.contrib import admin
from apps.post import models

# Register your models here.


class CustomPost(admin.ModelAdmin):
    list_display = [
        "username",
        "title",
        "get_tags",
        "created_at"
    ]

    @admin.display(description="Tags")
    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])


class CustomFly(admin.ModelAdmin):
    list_display = [
        "name",
        "author",
        "get_fly_type",
        "get_mat_amount"
    ]

    @admin.display(description="Fly Type")
    def get_fly_type(self, obj):
        return obj.fly_type_id.name

    @admin.display(description="Amount of materials")
    def get_mat_amount(self, obj):
        return obj.mat_amount


admin.site.register(models.Post, CustomPost)
admin.site.register(models.PostType)
admin.site.register(models.Tag)
admin.site.register(models.PostTag)
admin.site.register(models.Fly, CustomFly)
admin.site.register(models.FlyType)
