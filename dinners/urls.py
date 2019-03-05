
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


app_name = 'dinners'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('onas/', views.AboutView.as_view()),
    path('przepisy/', include('recipes.urls')),
    path('uzytkownik/', include('accounts.urls')),
    path('', views.HomepageView.as_view(), name='home'),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
