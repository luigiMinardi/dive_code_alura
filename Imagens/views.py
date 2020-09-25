from rest_framework import viewsets
from Imagens.models import Imagem
from Imagens.serializers import ImagemSerializer

class ImagemViewSet(viewsets.ModelViewSet):
   queryset = Imagem.objects.all()
   serializer_class = ImagemSerializer
