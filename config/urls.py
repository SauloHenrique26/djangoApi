from django.contrib import admin
from django.urls import path,include
from tasklist.views import TarefaViewSet,VideoViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'Tarefa',TarefaViewSet)
router.register(r'Video',VideoViewSet)


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path( '' , include(router.urls)),
]
