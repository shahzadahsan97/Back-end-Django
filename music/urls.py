from django.urls import path , re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('' , views.index , name = 'index') , 
    re_path(r'^(?P<album_id>[0-9]+)/$' , views.details , name = 'details')

]
 