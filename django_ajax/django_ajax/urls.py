
from django.contrib import admin
from django.urls import path, include
from ajax_example.views import postlist_view,post_fetch
from ajax_example2.views import Product_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', postlist_view, name='post-list'),
    path('fetch/', post_fetch, name="post-data"),
    path('', include("ajax_example2.urls"))
]
