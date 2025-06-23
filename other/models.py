from django.db import models


class Seo(models.Model):
    PAGES = (
        ('Homepage', 'Homepage'),
        ('About', 'About'),
        ('Projects', 'Projects'),
        ('Properties', 'Properties'),
        ('Blog', 'Blog'),
        ('Services', 'Services'),
        ('Contact', 'Contact'),
        ('Careers', 'Careers'),
    )
    page = models.CharField(max_length=22, choices=PAGES, default='Homepage', unique=True)
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=160)
    og_title = models.CharField(max_length=60)
    og_description = models.CharField(max_length=160)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Seo'
        verbose_name_plural = 'Seo'