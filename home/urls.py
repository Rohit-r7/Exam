
from django.urls import path,include
from . import views 
app_name ='home'
urlpatterns = [
   path('',views.index,name='hom'),
   path('about',views.about,name='abt'),
   path('conatct',views.contact,name='con'),
   path('academic',views.academic,name='aca'),
   path('student',views.student,name='std')
]