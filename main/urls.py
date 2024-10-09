from django.urls import path
from main.views import add_items_entry_ajax, show_main, create_items_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_item
from main.views import delete_item
from . import views
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-items-entry/', create_items_entry, name='create_items_entry' ),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-item/<uuid:id>', edit_item, name='edit_item'),
    path('delete/<uuid:id>', delete_item, name='delete_item'), 
    path('add-items-entry-ajax', add_items_entry_ajax, name='add_items_entry_ajax'),
    path('delete-item/<int:id>/', views.delete_item, name='delete_item'),
    path('edit-item/<int:id>/', views.edit_item, name='edit_item')
]