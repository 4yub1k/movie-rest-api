from rest_framework import serializers
from api.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'

class CommentSerializer(serializers.Serializer):
    comment = serializers.CharField(max_length=500) #there is not Textfield in REST, it will accept all as VARCHAR