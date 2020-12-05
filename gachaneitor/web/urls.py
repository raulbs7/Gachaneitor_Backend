from django.urls import path

from .views import IndexView, RecetasView

urlpatterns = [
    # /
    path('', IndexView.as_view(), name='index'),
    # /recetas/
    path('recetas/', RecetasView.as_view(), name='recetas'),
]