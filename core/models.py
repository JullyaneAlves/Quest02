from django.db import models

# Create your models here.


from django.db import models
from django.core.validators import RegexValidator


from django.contrib import admin

class Professor(models.Model):
        class Meta:
                verbose_name_plural = "Professores"

        nome = models.CharField('Nome', max_length=30)
        fone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        fone = models.CharField(validators=[fone_regex], max_length=17, blank=True) # validators should be a list
        valor = models.FloatField('Valor h/a')

        def __str__(self):
            return self.nome



class Curso(models.Model):
    nome = models.CharField('Nome do curso', max_length=50)
    carga_horaria = models.TimeField('Carga Horária')
    ementa = models.TextField('Ementa')
    valor = models.FloatField('Valor Total')

    class Meta:
        verbose_name_plural = 'Cursos Disponíveis'
        verbose_name = 'Curso Disponível'

class Turma(models.Model):

        nome = models.CharField('Ident. Turma', max_length=50)
        datainicio = models.DateField('Data Inicio')
        datatermino = models.DateField('Data Termino')
        horainicio = models.TimeField('Hora Inicio')
        horatermino = models.TimeField('Hora Termino')
        professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
        curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

        def __str__(self):
            return self.nome

        class Meta:
                verbose_name_plural = "Turmas"
                ordering = ('-datainicio', 'horainicio')
