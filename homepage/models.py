from django.db import models
from projects.models import Project
from properties.models import Property
from services.models import Service


class MainBanner(models.Model):
    image = models.ImageField(upload_to='banners/', verbose_name='Image')
    title = models.CharField(max_length=512, verbose_name='Title')
    subtitle = models.CharField(max_length=512, verbose_name='Subtitle')
    slogan = models.CharField(max_length=512, verbose_name='Slogan')
    project_name = models.CharField(max_length=512, verbose_name='Project Name')
    project_price = models.BigIntegerField(verbose_name='Project Price')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Main Banner'


class FeaturedPropertiesBanner(models.Model):
    subtitle = models.CharField(max_length=512, verbose_name='Subtitle')
    properties = models.ManyToManyField(Property, verbose_name='Properties')

    def __str__(self):
        return "Featured Properties Banner"

    class Meta:
        verbose_name = 'Featured Properties Banner'
        verbose_name_plural = 'Featured Properties Banner'


class PartnersBanner(models.Model):
    image = models.ImageField(upload_to='banners/', verbose_name='Image')

    def __str__(self):
        return "Partners Banner"

    class Meta:
        verbose_name = 'Partners Banner'
        verbose_name_plural = 'Partners Banner'


class FeaturedProjectsBanner(models.Model):
    card_image = models.ImageField(upload_to='banners/', verbose_name='Card Image')
    project_name = models.CharField(max_length=512, verbose_name='Project Name')
    project_price = models.CharField(max_length=512, verbose_name='Project Price')
    project_location = models.CharField(max_length=256, verbose_name='Project Location')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Project')

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = 'Featured Projects Banner'
        verbose_name_plural = 'Featured Projects Banners'


class ServicesBanner(models.Model):
    subtitle = models.CharField(max_length=512, verbose_name='Subtitle')
    services = models.ManyToManyField(Service, verbose_name='Services')

    def __str__(self):
        return "Services Banner"

    class Meta:
        verbose_name = 'Services Banner'
        verbose_name_plural = 'Services Banner'


class ProjectsByCityBanner(models.Model):
    card_image = models.ImageField(upload_to='banners/', verbose_name='Card Image')
    city = models.CharField(max_length=256, verbose_name='City')
    slogan = models.CharField(max_length=512, verbose_name='Slogan')

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Projects By City Banner'
        verbose_name_plural = 'Projects By City Banners'


class OurExperienceBanner(models.Model):
    title_gold = models.CharField(max_length=512, verbose_name='Title gold')
    title = models.CharField(max_length=512, verbose_name='Title')
    description = models.CharField(max_length=512, verbose_name='Description')
    image = models.ImageField(upload_to='banners/', verbose_name='Image')
    awards = models.CharField(max_length=512, verbose_name='Awards')
    projects = models.CharField(max_length=512, verbose_name='Projects')
    agents = models.CharField(max_length=512, verbose_name='Agents')
    experience = models.CharField(max_length=512, verbose_name='Experience')

    def __str__(self):
        return "Our Experience Banner"

    class Meta:
        verbose_name = 'Our Experience Banner'
        verbose_name_plural = 'Our Experience Banner'


class TestimonialsBanner(models.Model):
    fullname = models.CharField(max_length=512, verbose_name='Fullname')
    image = models.ImageField(upload_to='banners/', verbose_name='Image')
    location = models.CharField(max_length=256, verbose_name='Location')
    stars = models.IntegerField(verbose_name='Stars')
    review = models.TextField(verbose_name='Review')

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Testimonials Banner'
        verbose_name_plural = 'Testimonials Banner'