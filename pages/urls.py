from django.urls import path
from . import views


urlpatterns =[
    path('index',views.index ,name='index'),
    path('about' , views.about , name ='about'),
    #path('name',where,name)

]

#www.meme.com/example/XXXX
#we must add /before path name 