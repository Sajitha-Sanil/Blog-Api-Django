

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Blog(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=35)
    blog_text = models.TextField(max_length=1500)
    main_image = models.ImageField(upload_to="blogs")
    hashtags = models.CharField(max_length=200, blank=True)
    seo_keyword = models.CharField(max_length=200, blank=True)
    

    def save(self, *args, **kwargs):
        if not self.slug:  # Check if the slug is not already set
            self.slug = slugify(self.title)  # Generate the slug from the title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
