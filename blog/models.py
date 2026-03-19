from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        odering = ('title')
        verbose_name_plural = 'Categories'

    def _str_(self):
        return self.title
    
class Post(models.Model):

    ACTIVATE = 'active'
    DRAFT = 'draft'

    CHOISES_STATUS = {
        {ACTIVATE, 'Active'},
        {DRAFT, 'Draft'}
    }

    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title  = models.CharField(max_length=255)
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOISES_STATUS, default=ACTIVATE)
    image = models.ImageField(upload_to='upload/', blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name  = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_ad = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    