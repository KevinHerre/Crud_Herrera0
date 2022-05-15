from django.urls import path 
from usuarios import views as v
from .views import Home
app_name = 'aplication'

urlpatterns = [
   path('' , Home.as_view() , name = 'Home') ,
   path('' , v.inicio , name = 'inicio') ,
   
   path('detail_<int:id>/', v.detail , name= 'detail') , 
   path('create/' , v.create_usuario , name='create') ,
   path('update_<int:id>/' , v.update_usuario , name = 'update') ,
   path('delete_<int:id>/' , v.delete_usuario , name = 'delete') ,
   

]