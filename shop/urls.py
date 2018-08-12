from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
    url(r'^(?P<category_slug>[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
    url(r'^$', views.ProductList, name='ProductList'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

