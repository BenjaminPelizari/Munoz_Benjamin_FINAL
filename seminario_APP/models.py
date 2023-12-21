from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Inscrito(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    hora_inscripcion = models.TimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ])
    observacion = models.TextField(blank=True, null=True)