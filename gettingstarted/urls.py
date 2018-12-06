from django.urls import path, include
from core import views as core_views #Importing the vews from our core APP
from Articulos import views as articulos_views 

from django.conf import settings
from django.contrib import admin

admin.autodiscover()

import core.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path('', articulos_views.home, name = "home"),
    path("db/", core.views.db, name="db"),
    path("admin/", admin.site.urls),
    path('directorio/', core_views.directorio, name="directorio"),
    path('bolsa/', core_views.bolsa, name="bolsa-de-trabajo"),
    path('registro/', core_views.registro, name='registro'),
]

if settings.DEBUG:  # Displays media content from Dev site
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,  document_root= settings.MEDIA_ROOT)
