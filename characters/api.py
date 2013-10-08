from tastypie.resources import ModelResource
from characters.models import characters

# Create your models here.

class CharactersResource(ModelResource):
    class Meta:
        queryset = characters.objects.all()
        resource_name = 'characters'