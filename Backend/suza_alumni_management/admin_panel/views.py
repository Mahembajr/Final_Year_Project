

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Club, Event, Job, AssistanceOption, UserProfile
from .serializers import ClubSerializer, EventSerializer, JobSerializer, AssistanceOptionSerializer, UserProfileSerializer

# Club views
@api_view(['GET'])
def get_clubs(request):
    clubs = Club.objects.all()
    serializer = ClubSerializer(clubs, many=True)
    return Response(serializer.data)

# Event views
@api_view(['GET'])
def get_events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

# Job views
@api_view(['GET'])
def get_jobs(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

# Assistance Request views
@api_view(['GET'])
def get_assistance_options(request):
    options = AssistanceRequest.objects.all()  # Fixed the model name to AssistanceRequest
    serializer = AssistanceOptionSerializer(options, many=True)
    return Response(serializer.data)

# User Profile views
@api_view(['GET', 'PUT'])
def user_profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return Response({"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ViewSets
class ClubViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Club instances.
    """
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Event instances.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class JobViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Job instances.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class AssistanceOptionViewSet(viewsets.ModelViewSet):
    queryset = AssistanceOption.objects.all()
    serializer_class = AssistanceOptionSerializer
