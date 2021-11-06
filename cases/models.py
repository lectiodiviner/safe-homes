from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


# Create your models here.

class Case(models.Model):
    title = models.CharField(
        verbose_name='제목',
        max_length= 100,
    )

    thumbnail_image = models.ImageField(
        upload_to='images/', blank=True, null=True
    )

    contents_text = RichTextField(
        verbose_name='본문',
        default=True,
        null=True
    )

    created_at = models.DateTimeField(
        verbose_name='작성일'
    )

    created_by = models.CharField(
        verbose_name='작성자',
        max_length=100
    )

    is_view = models.BooleanField(
        verbose_name='공개 여부',
        default=True
    )

    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    tags = TaggableManager()
    
    def __str__(self):
        return '%s-%s' % (self.title, self.tags)

    class Tags(models.Model):
        title = models.CharField('title', max_length=30)
        tags = TaggableManager()

        def __str__(self):
            return self.title
    # tag = models.ManyToManyField('tag.Tag', verbose_name= "태그")


# class Tag(models.Model):
#    name = models.CharField(
#        max_length=32, verbose_name="태그명"
#        )
#    registered_date = models.DateTimeField(
#        auto_now_add=True, verbose_name="등록시간"
#        ) 
    

# def __str__(self):
#     return self.name

