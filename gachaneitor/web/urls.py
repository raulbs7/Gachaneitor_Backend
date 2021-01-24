from django.urls import path

from .views import IndexView, RecetasView, HowToView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('howto/', HowToView.as_view(), name='howto'),
    path('recetas/', RecetasView.as_view(), name='recetas'),
]