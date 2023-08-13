
from rest_framework import generics
from .models import Paciente, Doenca, Sintoma, Medicamento, Visita, Prescricao
from .serializers import (PacienteSerializer, DoencaSerializer, SintomaSerializer, 
                          MedicamentoSerializer, VisitaSerializer, PrescricaoSerializer)

class PacienteListCreateView(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class DoencaListCreateView(generics.ListCreateAPIView):
    queryset = Doenca.objects.all()
    serializer_class = DoencaSerializer

class DoencaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doenca.objects.all()
    serializer_class = DoencaSerializer

class SintomaListCreateView(generics.ListCreateAPIView):
    queryset = Sintoma.objects.all()
    serializer_class = SintomaSerializer

class SintomaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sintoma.objects.all()
    serializer_class = SintomaSerializer

class MedicamentoListCreateView(generics.ListCreateAPIView):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class MedicamentoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class VisitaListCreateView(generics.ListCreateAPIView):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer

class VisitaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer

class PrescricaoListCreateView(generics.ListCreateAPIView):
    queryset = Prescricao.objects.all()
    serializer_class = PrescricaoSerializer

class PrescricaoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prescricao.objects.all()
    serializer_class = PrescricaoSerializer

