from django.conf.urls import url
from . import views


app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='OrderCreate'),
    url(r'^admin/order/(?P<order_id>\d+)/$', views.admin_order_detail, name='AdminOrderDetail')
]
