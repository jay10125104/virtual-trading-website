from app import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('home/',views.home,name="home"),
    path('home/<slug:data>',views.home2,name="home2"),
    path('navbar/',views.navbar),
    path('success/',views.success),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
