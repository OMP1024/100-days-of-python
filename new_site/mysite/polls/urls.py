from django.conf.urls import url
from . import views

urlpatterns = [
    # url 正则， view 参数指定的视图函数（HttpRequest第一个参数，正则表达式捕获值，作为其他参2）
    url(r'^$',views.index,name='index'),
    # ?P<question_id>\d+ 匹配数字，并以 question_id 为名进行捕获
    url(r'(?P<pk>\d+)/$',views.DetailView.as_view(),name='detail'),
    url(r'(?P<pk>\d+)/results/$',views.ResultsView.as_view(),name='result'),
    url(r'(?P<question_id>\d+)/vote/$',views.vote,name='vote'),

]