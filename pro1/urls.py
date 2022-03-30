from django.urls import path,include

from .views import homeview
app_name='core'
urlpatterns = [
    path('',homeview.as_view(),name="index"),
    

]
