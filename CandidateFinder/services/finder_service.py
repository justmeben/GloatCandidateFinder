from typing import List
from CandidateFinder.models import Skill, Candidate, Job
from django.db.models import Value, F, Case, When, Q
from functools import reduce

PERFECT_TITLE_SCORE = 100
PARTIAL_TITLE_SCORE = 50
HAS_SKILL_SCORE = 40


def candidate_finder(job: Job) -> List[Candidate]:
    """
    :param job: Job model instance
    :return: List of candidates, sorted by rank score. Only candidates with rank above 0 (some compatibility) are returned
    * assuming no pagination required *
    """

    # Partial title match
    terms = job.title.split(' ')
    queries = reduce(lambda q, value: q | Q(title__icontains=value), terms, Q())

    # Ranking by perfect, partial title matches, and if the candidate has the skill
    c = Candidate.objects.annotate(title_rank=Case(When(Q(title=job.title), then=PERFECT_TITLE_SCORE),
                                                   When(queries, then=PARTIAL_TITLE_SCORE),
                                                   default=0),
                                   skill_rank=Case(When(Q(skills=job.skill), then=HAS_SKILL_SCORE), default=0))\
                         .annotate(rank=F('title_rank') + F('skill_rank')) \
                         .filter(rank__gt=0).distinct('id').order_by('id', '-rank')

    return sorted(list(c), key=lambda x: x.rank, reverse=True)
