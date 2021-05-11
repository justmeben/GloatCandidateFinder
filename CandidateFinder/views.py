from rest_framework.response import Response
from rest_framework.views import APIView

from CandidateFinder.models import Job
from CandidateFinder.serializers.candidate_serializers import CandidateWithRankSerializer
from CandidateFinder.serializers.job_serializers import JobSerializer
from CandidateFinder.services.finder_service import candidate_finder


class FindCandidates(APIView):
    def get(self, request, job_id):
        try:
            job = Job.objects.select_related('skill').get(id=job_id)
        except Job.DoesNotExist:
            return Response('Not Found', 404)

        candidates = candidate_finder(job)
        response = {
            'job': JobSerializer(job).data,
            'candidates': CandidateWithRankSerializer(candidates, many=True).data
        }
        return Response(response)
