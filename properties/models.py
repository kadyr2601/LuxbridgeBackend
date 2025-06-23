from django.db import models


class Property(models.Model):
    ref = models.CharField(max_length=120, unique=True, verbose_name='Property Reference Number')
    name = models.CharField(max_length=512, verbose_name='Property Name')
    location = models.CharField(max_length=256, verbose_name='Property Location')
    price = models.BigIntegerField(verbose_name='Property Price')
    bedrooms = models.IntegerField(verbose_name='Bedrooms Count')
    bathrooms = models.IntegerField(verbose_name='Bathrooms Count')
    area = models.CharField(max_length=12, verbose_name='Property Area - sq.f')
    overview = models.TextField(verbose_name='Property Overview')
    features = models.TextField(verbose_name='Property Features')
    amenities = models.TextField(verbose_name='Building Amenities')
    map = models.TextField(verbose_name='Property Google Map location', null=True, blank=True)
    type = models.CharField(max_length=120, verbose_name='Property Type')
    STATUS_CHOICES = [
        ("Ready", "Ready"),
        ("Off-plan", "Off-plan"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Property Status')
    for_rent = models.BooleanField(default=False, verbose_name='Property For Rent ?')
    card_image = models.ImageField(upload_to='property/', verbose_name='Property Card Image', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'


class PropertyGallery(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='gallery', verbose_name='Property Gallery')
    image = models.ImageField(upload_to='property/', verbose_name='Property Gallery Image', null=True, blank=True)

    def __str__(self):
        return self.property.name

    class Meta:
        verbose_name = 'Property Gallery'
        verbose_name_plural = 'Property Galleries'


class NearbyPlace(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='nearby_places', verbose_name='Property Nearby Place')
    name = models.CharField(max_length=256, verbose_name='Place Name')
    type = models.CharField(max_length=256, verbose_name='Place Type')
    distance = models.CharField(max_length=256, verbose_name='Place Distance')
    travelTime = models.CharField(max_length=256, verbose_name='Place Travel Time')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Place Nearby Place'
        verbose_name_plural = 'Place Nearby'


class AdditionalProperties(models.Model):
    PAGES = (
        ('Properties', 'Properties'),
        ('Blog', 'Blog'),
        ('Services', 'Services'),
    )
    page = models.CharField(max_length=22, choices=PAGES, default='Properties', unique=True)
    title = models.CharField(max_length=256, verbose_name='Additional properties section title')
    description = models.TextField(verbose_name='Additional properties section description')
    properties = models.ManyToManyField(Property, verbose_name='Additional properties')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Additional properties'
        verbose_name_plural = 'Additional properties'