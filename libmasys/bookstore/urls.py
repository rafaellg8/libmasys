from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/',views.addBook, name='addBook'),
    url(r'^search/',views.search, name='search'),
    url(r'^catalogo/',views.catalogo, name='catalogo'),
    url(r'^catalogojsonLibros/',views.getLibrosJSON, name='catalogoJSONLibros'),
    url(r'^catalogojsonDVDs/',views.getDVDsJSON, name='catalogoJSONDVDs'),
    url(r'^dvd/',views.catalogoDVD, name='catalogoDVD'),
    url(r'^sitemap\.xml$', views.sitemap, name='sitemap'),
]
