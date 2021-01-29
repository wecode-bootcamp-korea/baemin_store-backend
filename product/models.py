from django.db import models

class Category(models.Model):
	name = models.CharField(max_length	=45)

	class Meta: 
		db_table = 'categories'

class Like(models.Model):
	user	 = models.ForeignKey('user.User',  on_delete=models.CASCADE)
	product  = models.ForeignKey('Product',  on_delete=models.CASCADE)
	liked    = models.BooleanField(default= True)

	class Meta:
		db_table  = 'likes'

class Product(models.Model):
	category	  = models.ForeignKey('Category', on_delete=models.CASCADE)
	name          = models.CharField(max_length=45)
	main_image	  = models.URLField(max_length=2000)
	price		  = models.DecimalField(max_digits=18, decimal_places=2, default=0)
	money_replace = models.CharField(max_length=45)
	create_at 	  = models.DateTimeField(auto_now_add=True)
	update_at     = models.DateTimeField(auto_now=True)
	on_sales	  = models.ForeignKey('Sale', on_delete=models.CASCADE, null=True)
	tags 		  = models.ManyToManyField('Tag', through='ProductTag')
	hashtags 	  = models.ManyToManyField('HashTag', through='ProductHashTag')
	liked         = models.ManyToManyField('user.User', through='Like',null=True)

	class Meta: 
		db_table = 'products'

class Sale(models.Model):
	rate = models.DecimalField(max_digits=3, decimal_places=2)
	status = models.BooleanField(default= True)

	class Meta: 
		db_table = 'sales'

class Stock(models.Model):
	product	 = models.ForeignKey('Product', on_delete=models.CASCADE)
	quantity = models.IntegerField(default=0)

	class Meta:
		db_table = 'stocks'
	
class ProductTag(models.Model):
	product	= models.ForeignKey('Product', on_delete=models.CASCADE)
	tag		= models.ForeignKey('Tag', on_delete=models.CASCADE)
	
	class Meta: 
		db_table = 'product_tags'

class Tag(models.Model):
	name = models.CharField(max_length=45)
	
	class Meta: 
		db_table = 'tags'		


class ProductHashTag(models.Model):
	product	= models.ForeignKey('Product', on_delete=models.CASCADE)
	hashtag	= models.ForeignKey('HashTag', on_delete=models.CASCADE)

	class Meta: 
		db_table = 'product_hash_tags'


class HashTag(models.Model):
	name = models.CharField(max_length=45)

	class Meta: 
		db_table = 'hash_tags'


class ProductImage(models.Model):
	product		= models.ForeignKey('Product', on_delete=models.CASCADE)
	detail_url	= models.URLField(max_length=2000)
	image_flow	= models.IntegerField(default=0)

	class Meta: 
		db_table = 'product_images'



class Review(models.Model):
	user		= models.ForeignKey('user.User',  on_delete=models.CASCADE)
	product		= models.ForeignKey('Product',   on_delete=models.CASCADE)
	description	= models.TextField()
	create_at	= models.DateField(auto_now_add=True)
	update_at	= models.DateField(auto_now=True)
	
	class Meta:
		db_table  = 'reviews'


class ReviewImage(models.Model):
	review	  = models.ForeignKey('Review', on_delete=models.CASCADE)
	image_url = models.URLField(max_length=2048)

	class Meta:
		db_table  = 'review_images'