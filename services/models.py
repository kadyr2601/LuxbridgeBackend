from django.db import models
from django.utils.text import slugify


class MainBanner(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True, verbose_name='Banner title')
    title_gold = models.CharField(max_length=256, null=True, blank=True, verbose_name='Banner title gold')
    description = models.TextField(null=True, blank=True, verbose_name='Banner description')
    image = models.ImageField(upload_to='Banners', verbose_name='Banner image')

    def __str__(self):
        if self.title:
            return self.title
        return 'Main Banner'

    class Meta:
        verbose_name = 'Main Banner'
        verbose_name_plural = 'Main Banner'


class Service(models.Model):
    title = models.CharField(max_length=256, verbose_name='Service name')
    slug = models.SlugField(max_length=256, verbose_name='Service slug', unique=True)
    description = models.TextField(verbose_name='Service description')
    detailedDescription = models.TextField(verbose_name='Service detailed description')
    keyBenefits = models.TextField(verbose_name='Service keyBenefits')
    card_image = models.ImageField(upload_to='Service', verbose_name='Service card image')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class ServiceStep(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='processSteps')
    title = models.CharField(max_length=256, verbose_name='Step title')
    description = models.TextField(verbose_name='Step description')
    image = models.ImageField(upload_to='Steps', verbose_name='Step image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Step'
        verbose_name_plural = 'Steps'


class FAQs(models.Model):
    question = models.CharField(max_length=256, verbose_name='FAQ question')
    answer = models.TextField(verbose_name='FAQ answer')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'FAQs'
        verbose_name_plural = 'FAQs'