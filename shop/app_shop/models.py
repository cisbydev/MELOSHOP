from django.db import models


class Products(models.Model):
    nom_produit = models.CharField(max_length=180)
    slug = models.SlugField(unique=True , blank=True)
    stock_produit = models.IntegerField()
    prix_produit = models.DecimalField(max_digits=8, decimal_places=0)
    image_produit = models.ImageField(upload_to="photos", blank=True, null=True)
    
    def __str__(self):
        return self.nom_produit

    
        
class FormulaireContact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    
    
class Article(models.Model):
    nom_article = models.CharField(max_length=180)
    image_article = models.ImageField(upload_to="photos", blank=True, null=True)
    
    def __str__(self):
        return self.nom_article
    