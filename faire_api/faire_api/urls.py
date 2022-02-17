from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from tasks.views import TaskViewSet, SubTaskViewSet

router = routers.SimpleRouter()

router.register(r'tasks', TaskViewSet)
router.register(r'sub_tasks', SubTaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
