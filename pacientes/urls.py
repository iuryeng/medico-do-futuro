from django.urls import path
from .views import (PacienteListCreateView, PacienteDetailView, 
                    DoencaListCreateView, DoencaDetailView,
                    SintomaListCreateView, SintomaDetailView,
                    MedicamentoListCreateView, MedicamentoDetailView,
                    VisitaListCreateView, VisitaDetailView,
                    PrescricaoListCreateView, PrescricaoDetailView)

urlpatterns = [
    path('', PacienteListCreateView.as_view(), name='paciente-list-create'),
    path('<int:pk>/', PacienteDetailView.as_view(), name='paciente-detail-update-delete'),

    path('doencas/', DoencaListCreateView.as_view(), name='doenca-list-create'),
    path('doencas/<int:pk>/', DoencaDetailView.as_view(), name='doenca-detail-update-delete'),

    path('sintomas/', SintomaListCreateView.as_view(), name='sintoma-list-create'),
    path('sintomas/<int:pk>/', SintomaDetailView.as_view(), name='sintoma-detail-update-delete'),

    path('medicamentos/', MedicamentoListCreateView.as_view(), name='medicamento-list-create'),
    path('medicamentos/<int:pk>/', MedicamentoDetailView.as_view(), name='medicamento-detail-update-delete'),

    path('visitas/', VisitaListCreateView.as_view(), name='visita-list-create'),
    path('visitas/<int:pk>/', VisitaDetailView.as_view(), name='visita-detail-update-delete'),

    path('prescricoes/', PrescricaoListCreateView.as_view(), name='prescricao-list-create'),
    path('prescricoes/<int:pk>/', PrescricaoDetailView.as_view(), name='prescricao-detail-update-delete'),
]
