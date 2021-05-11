from rest_framework import serializers

from CandidateFinder.models import Job


class JobSerializer(serializers.ModelSerializer):
    skill = serializers.CharField(source='skill.name')

    class Meta:
        model = Job
        fields = ('id', 'title', 'skill')
