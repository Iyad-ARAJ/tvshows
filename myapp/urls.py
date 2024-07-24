from django.urls import path
from . import views

urlpatterns = [
    path('shows/new',views.add_new_show,name='addshow'),
    path('shows/create',views.create_show,name= 'createshow'),
    path('shows/<int:id>',views.show_details,name= 'show_details'),
    path('shows/<int:id>/delete',views.delete_show,name= 'show_details'),
    path('shows/',views.all_shows,name='allshows'),
    path('shows/<int:id>/edit',views.edit_show),
    path('shows/<int:id>/update',views.update_show ),


]