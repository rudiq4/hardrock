from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.productlist, name='ProductList'),
    url(r'^deliver/$', views.deliver, name='deliver'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.productlist, name='ProductListByCategory'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.productdetail, name='ProductDetail'),
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
