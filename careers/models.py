from django.db import models


class MainBanner(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True, verbose_name='Banner title')
    title_gold = models.CharField(max_length=256, null=True, blank=True, verbose_name='Banner title gold')
    image = models.ImageField(upload_to='Banners', verbose_name='Banner image')

    def __str__(self):
        if self.title:
            return self.title
        return 'Main Banner'

    class Meta:
        verbose_name = 'Main Banner'
        verbose_name_plural = 'Main Banner'


class Position(models.Model):
    title = models.CharField(max_length=512, verbose_name='Position title')
    department = models.CharField(max_length=128, verbose_name='Position department')
    location = models.CharField(max_length=128, verbose_name='Position location')
    type = models.CharField(max_length=128, verbose_name='Position type Full-time || Part-Time')
    experience = models.CharField(max_length=128, verbose_name='Position experience')
    overview = models.CharField(max_length=512, verbose_name='Position overview')
    requirements = models.TextField(verbose_name='Position requirements')
    benefits = models.TextField(verbose_name='Position benefits')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Opened Positions'


class Application(models.Model):
    position = models.CharField(max_length=512, verbose_name='Position title')
    first_name = models.CharField(max_length=128, verbose_name='First Name')
    last_name = models.CharField(max_length=128, verbose_name='Last Name')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=128, verbose_name='Phone')
    experience = models.CharField(max_length=128, verbose_name='Experience')
    linkedin = models.CharField(max_length=256, verbose_name='Linkedin profile', null=True, blank=True)
    portfolio = models.CharField(max_length=256, verbose_name='Portfolio || Website', null=True, blank=True)
    cover_letter = models.CharField(max_length=256, verbose_name='Cover Letter')
    resume = models.FileField(upload_to='resumes', verbose_name='Resume File || CV')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applied Applications'