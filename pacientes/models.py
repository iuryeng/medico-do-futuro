from django.db import models

# Create your models here.
from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=20, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outro', 'Outro')])
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()
    numero_sus = models.CharField(max_length=20, unique=True)
    
    # Histórico Médico
    doencas_preexistentes = models.ManyToManyField('Doenca', related_name="doencas_preexistentes", blank=True)
    medicamentos_atual = models.ManyToManyField('Medicamento', related_name="medicamentos_em_uso", blank=True)
    alergias = models.TextField(blank=True)
    historico_cirurgias = models.TextField(blank=True)
    historico_familiar = models.TextField(blank=True)
    
    # Estilo de Vida
    atividade_fisica = models.CharField(max_length=30, choices=[('Sedentário', 'Sedentário'), ('Moderado', 'Moderado'), ('Ativo', 'Ativo')])
    dieta = models.CharField(max_length=50)
    consumo_alcool_tabaco = models.BooleanField(default=False)
    ocupacao = models.CharField(max_length=100)
    
    # Registro de Visitas
    visitas = models.ManyToManyField('Visita', blank=True)

    def __str__(self):
        return self.nome

class Doenca(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Sintoma(models.Model):
    TIPOS_SINTOMA = [
        ('Emocioanal', 'Emocional'),
        ('Fisico', 'Fisico'),
        ('Comportamental', 'Comportamental'),
    ]
    
    doenca = models.ForeignKey(Doenca, related_name='sintomas', on_delete=models.CASCADE)
    descricao = models.TextField()
    tipo = models.CharField(max_length=15, choices=TIPOS_SINTOMA)

    def __str__(self):
        return self.descricao
    

class Medicamento(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    dosagem = models.CharField(max_length=50)
    contra_indicacoes = models.TextField(blank=True)
    # Outros campos relevantes

    def __str__(self):
        return self.nome

class Visita(models.Model):
    data_visita = models.DateField()
    motivo = models.CharField(max_length=300)
    observacoes = models.TextField(blank=True)
    prescricoes = models.ManyToManyField(Medicamento, through='Prescricao', blank=True)
    # Outros campos relevantes

    def __str__(self):
        return f"Visita em {self.data_visita} - {self.motivo}"

class Prescricao(models.Model):
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    visita = models.ForeignKey(Visita, on_delete=models.CASCADE)
    dosagem = models.CharField(max_length=50)
    duracao = models.CharField(max_length=50)
    instrucoes = models.TextField()

    def __str__(self):
        return f"{self.medicamento.nome} - {self.dosagem}"
