from django.db import models
#from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Participante(models.Model):
	nome = models.CharField(max_length=100, default=None)
	data_nascimento = models.DateField(default=None)
	def __str__(self):
		return self.nome

class Levantamento(models.Model):
	data = models.DateField(default=None)
	participante = models.ForeignKey(
		Participante,
		on_delete=models.CASCADE,
		default=None
	)
	def __str__(self):
		return self.nome

class Levantamento_dados(models.Model):
	levantamento = models.ForeignKey(
		Levantamento,
		on_delete=models.CASCADE,
		default=None
	)
	variavel = models.CharField(max_length=45, default=None)
	valor = models.DecimalField(
		max_digits=10, 
		decimal_places=0,
		default=None
		#validators=[MaxValueValidator(10), MinValueValidator(0)]
	)
	def __str__(self):
		return f'{self.levantamento} {self.variavel} #{self.valor}'
	class Meta:
		verbose_name_plural = 'Levantamento Dados'