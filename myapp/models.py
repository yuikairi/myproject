from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    main_image =  models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.CharField(max_length=100, blank=True)
    short_description = models.CharField(max_length=255, blank=True)
    cart_id = models.CharField(max_length=200, unique=True, blank=True, null=True)  # カラーミーのカートID
    short_description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.name}"

"""すべての画像を取得するときは
product = Product.objects.get(id=some_product_id)
images = product.images.all()
"""      