"""koutu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import koutuonline.views as view
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles


urlpatterns = [
    url(r'^$', view.uploadImg, name="index"),
    url(r'^admin/', admin.site.urls),
    url(r'^paint', view.uploadImg2, name="paint"),
    url(r'^scribble', view.uploadImg3, name="scribble"),
    url(r'^upload', view.uploadImg, name="upload"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
