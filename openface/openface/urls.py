"""openface URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from . import view

from . import settings
from django.conf.urls.static import static
import logging

''' url函数
regex: 正则表达式，与之匹配的 URL 会执行对应的第二个参数 view。
view: 用于执行与正则表达式匹配的 URL 请求。
kwargs: 视图使用的字典类型的参数。
name: 用来反向获取 URL。
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^getMatchFacesTest$', view.getMatchFacesTest),
    url(r'^hello$', view.hello),
    url(r'^test$', view.test),
    url(r'^upload', view.uploadImg),
    url(r'^show', view.showImg),
    url(r'^$', view.hello)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

logging.basicConfig(level=logging.DEBUG)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")