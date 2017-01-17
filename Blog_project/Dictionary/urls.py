from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^choice', views.choice, name="choice"),
    url(r'^dictionary', views.dictionary, name="dictionary"),
    url(r'^thesaurus', views.thesaurus, name="thesaurus"),
]
