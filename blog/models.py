from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)
    page_title = models.CharField(max_length=256)
    image = models.ImageField(upload_to='Categories', verbose_name='Image')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class PopularTags(models.Model):
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return "Tags banner"

    class Meta:
        verbose_name = 'Popular tags'
        verbose_name_plural = 'Popular tags'


class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs')
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=512)
    card_image = models.ImageField(upload_to='Blog', verbose_name='Card image')
    banner_image = models.ImageField(upload_to='Blog', verbose_name='Banner image')
    slug = models.SlugField(unique=True)
    overview = models.TextField()
    created = models.CharField(max_length=50)
    author_fullname = models.CharField(max_length=128)
    author_position = models.CharField(max_length=128)
    author_overview = models.CharField(max_length=1000)
    author_image = models.ImageField(upload_to='Blog', verbose_name='Author')
    time_of_read = models.CharField(max_length=128)
    details = models.TextField()
    keywords = models.TextField()
    image = models.ImageField(upload_to='Blog', verbose_name='Image')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'