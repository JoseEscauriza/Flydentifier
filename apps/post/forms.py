from django.forms import ModelForm
from apps.post import models


class PostForm(ModelForm):
    class Meta:
        model = models.Post
        fields = ["post_type_id", "title", "body", "tags", "upload"]
