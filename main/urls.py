from django.urls import path
#from django.conf.urls.static import static
#from django.conf import settings
#static 이미지를 한번에 모으는게 좋다고 하는 거 같은데 오류남

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('status/', views.status),
    path('calender/', views.calender),
    path('music/', views.music),
    path('time/', views.time),
    path('alarm/', views.alarm),
    path('led/', views.led),
    path('1/', views.one),
    path('2/', views.two),
    path('3/', views.th)

]#+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
