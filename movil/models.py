from django.db import models

# Create your models here.

class Estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    nombre = models.TextField()
    carnet = models.TextField()


class Materias(models.Model):
    id_materia = models.AutoField(primary_key=True)
    nombre = models.TextField()
    codigo = models.TextField()


class Materias_X_Estudiante(models.Model):
    id_materia_estudiante = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    id_materia = models.ForeignKey(Materias, on_delete=models.CASCADE)