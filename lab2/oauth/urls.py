from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', TemplateView.as_view(template_name='oauth/index.html'), name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]

# urlpatterns += staticfiles_urlpatterns()