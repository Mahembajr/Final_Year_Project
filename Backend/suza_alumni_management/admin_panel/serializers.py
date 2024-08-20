
from rest_framework import serializers
from .models import Club, Event, Job, AssistanceOption,UserProfile

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class AssistanceOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssistanceOption
        fields = '__all__'

# class AssistanceRequestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AssistanceRequest
#         fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # Assuming you want to display the username of the user
    
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'certifications', 'cv']
