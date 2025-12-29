from django.urls import path
from . import views

app_name = 'app_shop'

urlpatterns = [
    path('accueil/', views.index, name='index'),  
    path('page_article/', views.article, name='articles')
    # path('page_contact/', views.contact, name='contact'),
]