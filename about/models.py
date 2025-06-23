from django.db import models


class Team(models.Model):
    fullname = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    overview = models.TextField()
    image = models.ImageField(upload_to='team_images')

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = 'teams'
        verbose_name = 'team'


class AboutPage(models.Model):
    banner_title = models.CharField(max_length=256, verbose_name="Banner title")
    banner_title_gold = models.CharField(max_length=256, verbose_name="Banner title gold")
    banner_image = models.ImageField(upload_to='banners', verbose_name="Banner image")
    welcome_section_title = models.CharField(max_length=256, verbose_name="Welcome section title")
    welcome_section_title_gold = models.CharField(max_length=256, verbose_name="Welcome section title gold")
    welcome_section_description = models.TextField(verbose_name="Welcome section description")
    our_mission = models.CharField(max_length=1052, verbose_name="Our mission")
    our_vision = models.CharField(max_length=1052, verbose_name="Our vision")
    our_values = models.CharField(max_length=1052, verbose_name="Our values")
    founder_image = models.ImageField(upload_to='founder', verbose_name="Founder image")
    founder_main_words = models.TextField(verbose_name="Founder main words")
    founder_sub_words = models.TextField(verbose_name="Founder sub words")
    team = models.ManyToManyField(Team, verbose_name="Team")

    def __str__(self):
        return "About page"

    class Meta:
        verbose_name = "About page"
        verbose_name_plural = "About page"