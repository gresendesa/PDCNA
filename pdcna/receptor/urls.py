from django.urls import include, path, re_path
from . import views

urlpatterns = [
    re_path('participante/?', views.ParticipanteView.as_view()),
    re_path('levantamento/?$', views.LevantamentoView.as_view()),
    re_path('levantamento_dados/?', views.Levantamento_dadosView.as_view()),
    re_path('.+', views.index)
]
