from django.db import models



class prob5_the_anikanik_girls(models.Model):
		created_at = models.DateTimeField(auto_now_add=True)
		first_name = models.CharField(max_length=50)
		gc_name = models.CharField(max_length=50)
		favorite_collectible = models.CharField(max_length=200)
		favorite_collection = models.CharField(max_length=200)
		hacipupu_owned = models.CharField(max_length=200)
		zsiga_owned = models.CharField(max_length=200)
		hirono_owned = models.CharField(max_length=200)
		monthly_expense_on_collectible = models.CharField(max_length=100)

		def __str__(self):
				return(f"{self.code_name}")