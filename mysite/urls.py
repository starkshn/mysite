"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

# http://127.0.0.1:8000/ 얘를 받아서 'polls/' include 함수로 받아서 -> parsing 한다음 urls.py polls 로  보냄

# 앱이 여러개 있다면 그 해당 path에 맞게 파싱해서 분기로 보낸다
# urlpatterns = [
#     path('polls123/', include('poll123.urls')),
#     path('polls133/', include('poll133.urls')),
#     path('polls33/', include('polls33.urls')),
#     path('polls2332/', include('polls2332.urls')),
#     path('admin/', admin.site.urls),
    
# ]

# http://127.0.0.1:8000/polls123
# http://127.0.0.1:8000/polls133
# http://127.0.0.1:8000/polls33
# http://127.0.0.1:8000/polls2332

# 만약 이렇게 앱이 여러개라면 url 에 따라서 parsing을 해주고 path따른 앱으로 분기를 시켜주는것이다.