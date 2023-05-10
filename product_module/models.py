from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, verbose_name='عنوان در url')

    def __str__(self):
        return f'( {self.title} - {self.url_title} )'

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductInformation(models.Model):
    color = models.CharField(max_length=200, verbose_name='رنگ')
    size = models.CharField(max_length=200, verbose_name='سایز')

    def __str__(self):
        return f'{self.size} - {self.color}'

    class Meta:
        verbose_name = 'اطلاعات تکمیلی'
        verbose_name_plural = 'تمامی اطلاعات تکمیلی'


class Product(models.Model):
    title = models.CharField(max_length=300)
    product_information = models.OneToOneField(
        ProductInformation,
        on_delete=models.CASCADE,
        related_name='product_information',
        verbose_name='اطلاعات تکمیلی',
        null=True,
        blank=True)
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        null=True,
        related_name='products',
        verbose_name='دسته بندی')
    price = models.IntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    short_description = models.CharField(max_length=360, null=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True)

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
