from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Receta(models.Model):
    HORAS = 'h'
    MINUTOS = 'min'
    SEGUNDOS = 's'
    UNIDADES_TIEMPO_CHOICES = [
        (HORAS, 'Horas'),
        (MINUTOS, 'Minutos'),
        (SEGUNDOS, 'Segundos')
    ]
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=128, primary_key=True)
    descripcion = models.TextField()
    tmp_preparacion = models.IntegerField(default=0)
    ud_tmp_preparacion = models.CharField(max_length=3, choices=UNIDADES_TIEMPO_CHOICES)
    tmp_total = models.IntegerField(default=0)
    ud_tmp_total = models.CharField(max_length=3, choices=UNIDADES_TIEMPO_CHOICES)

    def __str__(self):
        return f'{self.nombre}'


class Ingrediente(models.Model):
    UNIDADES = 'ud'
    MILIGRAMOS = 'mg'
    GRAMOS = 'g'
    KILOGRAMOS = 'kg'
    MILILITROS = 'ml'
    LITROS = 'l'
    UNIDADES_CANTIDAD_CHOICES = [
        (UNIDADES, 'Unidades'),
        (MILIGRAMOS, 'Miligramos'),
        (GRAMOS, 'Gramos'),
        (KILOGRAMOS, 'Kilogramos'),
        (MILILITROS, 'Mililitros'),
        (LITROS, 'Litros')
    ]
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=128)
    cantidad = models.IntegerField(default=0)
    ud_cantidad = models.CharField(max_length=2, choices=UNIDADES_CANTIDAD_CHOICES)

    class Meta:
        unique_together = [['receta', 'nombre']]

    def __str__(self):
        return f'{self.nombre}'

    def save(self, *args, **kwargs):
        field_name = 'nombre'
        val = getattr(self, field_name, False)
        if val:
            setattr(self, field_name, val.capitalize())
        super(Ingrediente, self).save(*args, **kwargs)

class Paso(models.Model):
    CENTIGRADOS = 'ºC'
    FARENHEIT = 'ºF'
    UNIDADES_TEMPERATURA_CHOICES = [
        (CENTIGRADOS, 'Grados centígrados'),
        (FARENHEIT, 'Grados farenheit')
    ]
    MOVER = 'mover'
    PERSONA = 'persona'
    COCINAR = 'cocinar'
    TIPO_VERBO_CHOICES = [
        (COCINAR, 'Cocinar'),
        (PERSONA, 'Por la persona'),
        (MOVER, 'Mover')
    ]
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    num_paso = models.IntegerField(validators=[MinValueValidator(1)])
    verbo = models.CharField(max_length=128)
    tipo_verbo = models.CharField(max_length=64, choices=TIPO_VERBO_CHOICES)
    ingredientes = models.TextField()
    temperatura = models.IntegerField(null=True, blank=True)
    ud_temperatura = models.CharField(max_length=2, blank=True, choices=UNIDADES_TEMPERATURA_CHOICES)
    velocidad = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(9)])

    class Meta:
        unique_together = [['receta', 'num_paso']]

    def __str__(self):
        return f'{self.num_paso}'

    def save(self, *args, **kwargs):
        field_name = 'verbo'
        val = getattr(self, field_name, False)
        if val:
            setattr(self, field_name, val.capitalize())
        super(Paso, self).save(*args, **kwargs)

