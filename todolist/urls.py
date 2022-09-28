from django.urls import path
# from wishlist.views import show_wishlist
# from wishlist.views import show_xml 
# from wishlist.views import show_json
# from wishlist.views import show_json_by_id
# from wishlist.views import show_xml_by_id
from todolist.views import register, show_todolist #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import logout_user #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import show_newtask

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', show_newtask, name='show_newtask'),
]