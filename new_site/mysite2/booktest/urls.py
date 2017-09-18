from django.conf.urls import url
from . import views
from . import view1
urlpatterns = [
    url(r'^$',views.gettest,name='index'),
    url(r"^(?P<p1>\d+)/(?P<p2>\d+)/(?P<p3>\d+)",views.detail,name='detail'),
    url(r'^index2/',views.index2,name='index2')
]