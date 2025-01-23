

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
   
    path("", views.HelloWorld, name="home"),
    path("about/", views.about, name="about"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("products/<int:pk>/", views.product, name="product"),
    path("category/<str:cat>/", views.category, name="category"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)