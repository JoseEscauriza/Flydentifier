from django.db import models
from apps.core.models import TimestampBase
from config.settings.base import BASE_DIR


class Post(TimestampBase):
    user_id = models.ForeignKey("user.User", verbose_name=(
        "Username"), on_delete=models.CASCADE)
    post_type_id = models.ForeignKey("post.PostType", verbose_name=(
        "Post Type"), on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(max_length=300, null=True, blank=True)
    tags = models.ManyToManyField("post.Tag", verbose_name=("Tags"))
    upload = models.ImageField(verbose_name="Image upload", upload_to="post_img_dir",
                               height_field=None, width_field=None, max_length=None, null=True, blank=True)

    def __str__(self):
        return f"{self.user_id.username} - {self.title}"

    def username(self):
        return self.user_id.username


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostTag(TimestampBase):
    modified_at = None
    post_id = models.ForeignKey("post.Post", verbose_name=(
        "Post id"), on_delete=models.CASCADE)
    tag_id = models.ForeignKey("post.Tag", verbose_name=(
        "Tag id"), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post_id.title} - {self.tag_id.name}"

    class Meta:
        verbose_name_plural = "Post Tags"


class PostType(models.Model):
    type = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Post Types"

    def __str__(self):
        return self.type


class Fly(TimestampBase):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    fly_type_id = models.ForeignKey(
        "post.FlyType", verbose_name=("Fly Type"), on_delete=models.CASCADE)
    mat_amount = models.IntegerField(
        verbose_name="Amount of materials", null=True, blank=True)
    upload = models.ImageField(verbose_name="Image upload", upload_to="fly_img_dir",
                               height_field=None, width_field=None, max_length=None, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Flies"

    def __str__(self):
        return f"{self.name} - Fly Type: {self.fly_type_id.name}"


class FlyType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Fly Types"

    def __str__(self):
        return self.name
