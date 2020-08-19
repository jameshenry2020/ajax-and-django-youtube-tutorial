
from django.urls import path
from ajax_example2.views import Product_view

urlpatterns = [
    path('delete/',Product_view.as_view(), name='delete-product')
]
