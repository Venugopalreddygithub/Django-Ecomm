from rest_framework import serializers 
from tags.models import Tags

# Types of serializers 
# ReadSerializer is used to read a data from database (Read Operation)
# WriteSerializer is used to write data into database (Write Operation)

class WriteTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags 
        fields = ('name', 'slug')
        
class ReadTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags 
        fields = ('name', 'slug', 'created_at', 'updated_at')