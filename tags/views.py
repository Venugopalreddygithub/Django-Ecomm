from django.shortcuts import render
from rest_framework import views, status 
from rest_framework.response import  Response 
from tags.serializers import WriteTagsSerializer, ReadTagsSerializer 
from tags.models import Tags 
from django.utils.text import slugify 
# Create your views here.


class CreateTagView(views.APIView):
    # def get(self, request):
    #     pass 
    
    # def put(self, request):
    #     pass 
    
    # def delete(self, request):
    #     pass 
    
    def post(self, request):
        serializer = WriteTagsSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            tag_object = Tags.objects.create(name=name, slug=slugify(name))
            response_data = ReadTagsSerializer(instance=tag_object).data 
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)