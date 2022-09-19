
from django.contrib import admin
from django.urls import path

from asosiy.views import *
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('blog/', blog),
    path('about/', about),
    path('maqola/', maqola),
    path('maqola/<int:pk>/', maqola),
    path('intervyular/', intervyular),
    # path('intervyu/<int:pk>/', intervyu),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
