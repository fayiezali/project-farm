from django.urls import path
from . import views

urlpatterns = [
#___________________________________________
# (A) Create New Record URLs
#___________________________________________
path(
    ''
    ,views.dashboard  
    ,name="url-dashboard"
    )
    ,
# path(
#     'about'
#     ,views.about  
#     ,name="url-about"
#     )
#     ,
]