from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('create/', views.create_items_entry, name='create_items_entry'),
    path('add-ajax/', views.add_items_entry_ajax, name='add_items_entry_ajax'),
    path('edit/<int:id>/', views.edit_item, name='edit_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('json/', views.show_json, name='show_json'),
    path('json/<int:id>/', views.show_json_by_id, name='show_json_by_id'),
    path('xml/', views.show_xml, name='show_xml'),
    path('xml/<int:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('create-flutter/', views.create_item_flutter, name='create_item_flutter'),
]
