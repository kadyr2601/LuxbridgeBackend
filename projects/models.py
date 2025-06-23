from django.db import models
from django.utils.text import slugify


class PropertyType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Property Type')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Property Type'
        verbose_name_plural = 'Property Types'


class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name='Project Name')
    slug = models.SlugField(max_length=100, verbose_name='Project Slug')
    location = models.CharField(max_length=100, verbose_name='Project Location')
    card_overview = models.CharField(max_length=100, verbose_name='Project Card Overview')
    description = models.TextField(verbose_name='Project Description')
    developer = models.CharField(max_length=100, verbose_name='Developer')
    city = models.CharField(max_length=100, verbose_name='City')
    card_property_type = models.CharField(max_length=100, verbose_name='Project Card Property Type', default="Apartments")
    starting_price = models.BigIntegerField(verbose_name='Price from')
    handover = models.CharField(max_length=100, verbose_name='Handover')
    card_image = models.ImageField(upload_to='card_images', verbose_name='Card Image')
    featured = models.BooleanField(default=False, verbose_name='Featured ?')
    status = models.CharField(max_length=100, verbose_name='Project Status', default="Off-plan")
    property_types = models.ManyToManyField(PropertyType, verbose_name='Property Types')
    amenities = models.TextField(verbose_name='Amenities')
    map_location = models.CharField(max_length=100, verbose_name='Map Location')
    mainBanner = models.ImageField(upload_to='main_banner', verbose_name='Main Banner')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class ProjectGallery(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Project', related_name='project_gallery')
    image = models.ImageField(upload_to='project_gallery', verbose_name='Project Gallery')

    def __str__(self):
        return self.project.name

    class Meta:
        verbose_name = 'Project Gallery'
        verbose_name_plural = 'Project Gallery'


class NearbyPlace(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='nearby_places', verbose_name='Project Nearby Places')
    name = models.CharField(max_length=256, verbose_name='Place Name')
    type = models.CharField(max_length=256, verbose_name='Place Type')
    distance = models.CharField(max_length=256, verbose_name='Place Distance')
    travelTime = models.CharField(max_length=256, verbose_name='Place Travel Time')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Nearby Place'
        verbose_name_plural = 'Nearby Places'


class DownloadedInformation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='downloaded_informations', verbose_name='Project')
    title = models.CharField(max_length=256, verbose_name='Title', default='Get all the floor plans')
    image = models.ImageField(upload_to='downloaded_images', verbose_name='Background Image')
    buttonText = models.CharField(max_length=256, verbose_name='Button Text', default='Download floor plans')
    file = models.FileField(upload_to='downloaded_files', verbose_name='Downloaded File')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Downloaded Information'
        verbose_name_plural = 'Downloaded Information'


class SimilarProjects(models.Model):
    title = models.CharField(max_length=256, verbose_name='Title', default='Related Projects You May Like')
    projects = models.ManyToManyField(Project, verbose_name='Related Projects')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Similar Project'
        verbose_name_plural = 'Similar Projects'