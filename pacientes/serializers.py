from rest_framework import serializers
from .models import Paciente, Doenca, Sintoma, Medicamento, Visita, Prescricao

class DoencaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doenca
        fields = '__all__'

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'

class SintomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sintoma
        fields = '__all__'

class PrescricaoSerializer(serializers.ModelSerializer):
    medicamento = MedicamentoSerializer(read_only=True)
    
    class Meta:
        model = Prescricao
        fields = '__all__'

class VisitaSerializer(serializers.ModelSerializer):
    prescricoes = PrescricaoSerializer(many=True, read_only=True)

    class Meta:
        model = Visita
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    doencas_preexistentes = DoencaSerializer(many=True, read_only=True)
    medicamentos_atual = MedicamentoSerializer(many=True, read_only=True)
    visitas = VisitaSerializer(many=True, read_only=True)

    class Meta:
        model = Paciente
        fields = '__all__'

