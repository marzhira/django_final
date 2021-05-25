from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'gazua'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.first_view, name='first_view'),
    path('ml_analysis/', views.analysis, name='analysis'),
    path('ml_analysis/predict/', views.predict_analysis, name='predict_analysis'),
    path('resource/', views.resource, name='resource'),
    path('aboutus/', views.aboutus, name='aboutus'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
