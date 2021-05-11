from rest_framework import serializers

from CandidateFinder.models import Candidate
from CandidateFinder.serializers.skill_serializers import SkillSerializer


class CandidateWithRankSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    rank = serializers.SerializerMethodField()

    def get_rank(self, candidate):
        return candidate.rank if hasattr(candidate, 'rank') else None

    class Meta:
        model = Candidate
        fields = ('id', 'title', 'skills', 'rank')
