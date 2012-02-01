from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.models import User

urlpatterns = patterns('',
    (r'^login/$', 'django.contrib.auth.views.login',
     {'template_name': 'rewards/login.html'}),
    (r'^profile/', 'rewards.views.user_object_detail',
     {'template_name': 'rewards/my_user_detail.html',
      'queryset':User.objects.all()})
)