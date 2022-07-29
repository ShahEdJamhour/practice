from django.urls import path 
from . import views
#python list for urls for the app 
urlpatterns = [ 
               #here we will set the routes so we will include the paths 
    # we will give it 3 paramenters, the link , the name of the veiw imported from veiws file and finally a name 
    path ('',views.home, name="home"),
    path ('room/', views.room, name="room"), 
    
  
    
]


