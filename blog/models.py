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

    category = models.ForeignKey(category, related_name='posts', on_delete=models.)
    title  = models.