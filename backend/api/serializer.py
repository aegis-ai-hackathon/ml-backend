from rest_framework import serializers
class SpamSerializer(serializers.Serializer):
    email_id=serializers.EmailField()
    content=serializers.CharField(max_length=10000)
    
#emailid
#number of spams