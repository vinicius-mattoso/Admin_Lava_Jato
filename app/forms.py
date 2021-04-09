from django.forms import ModelForm
from app.models import Carros

# Create the form class.
# # Classes utilizadas
#     modelo = models.CharField(max_length=150)
#     marca = models.CharField(max_length=100)
#     cor = models.CharField(max_length=100)
#     ano = models.IntegerField()
#     servico = models.IntegerField()
#     entrada = models.DateField()
#     pagamento = models.CharField(max_length=100)
class CarrosForm(ModelForm):
    class Meta:
        model = Carros
        fields = ['modelo', 'marca', 'cor','ano','servico','entrada','pagamento']