"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from foto.views import (index, PostDetalle, PostListar, 
                        PostCrear, PostBorrar, PostActualizar,
                        UserSignUp, UserLogin, UserLogout, 
                        AvatarActualizar, UserActualizar, MensajeCrear, MensajeListar, 
                        MensajeDetalle, about, MensajeBorrar)
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foto/', index, name="foto-index"),
    path('foto/<int:pk>/detalle/', PostDetalle.as_view(), name="foto-detalle"),
    path('foto/listar/', PostListar.as_view(), name="foto-listar"),
    path('foto/crear/', staff_member_required(PostCrear.as_view()), name="foto-crear"),
    path('foto/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="foto-borrar"),
    path('foto/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="foto-actualizar"),
    path('foto/signup/', UserSignUp.as_view(), name ="foto-signup"),
    path('foto/login/', UserLogin.as_view(), name= "foto-login"),
    path('foto/logout/', UserLogout.as_view(), name="foto-logout"),
    path('foto/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="foto-avatars-actualizar"),
    path('fotousers/<int:pk>/actualizar/', UserActualizar.as_view(), name="foto-users-actualizar"),
    path('foto/mensajes/crear/', MensajeCrear.as_view(), name="foto-mensajes-crear"),
    path('foto/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="foto-mensajes-detalle"),
    path('foto/mensajes/listar/', MensajeListar.as_view(), name="foto-mensajes-listar"),
    path('foto/mensajes/<int:pk>/borrar/', staff_member_required(MensajeBorrar.as_view()), name="foto-mensajes-borrar"),
    path('foto/about', about, name="about"),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

""


