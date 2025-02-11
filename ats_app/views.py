from django.db.models import Q
from rest_framework import viewsets
from ats_app.models import Candidate
from ats_app.serializers import CandidateSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing candidates.
    Supports: List, Create, Retrieve, Update, Delete, and Search candidates.
    """
    lookup_field = "unique_id"
    serializer_class = CandidateSerializer

    @staticmethod
    def word_match(candidate, query_words):
        candidate_words = candidate.name.split()
        total = 0
        for word in candidate_words:
            if word in query_words:
                total += 1
        return total

    def get_queryset(self):
        query_param = self.request.query_params.get("name")
        if not query_param:
            return Candidate.objects.all()
        else:
            query_words = query_param.split()
            search_conditions = Q()

            for word in query_words:
                search_conditions |= Q(name__icontains=word)

            candidates = list(Candidate.objects.filter(search_conditions))

            candidates_word_count = {}
            for candidate in candidates:
                word_matches = self.word_match(candidate, query_words)
                candidates_word_count[candidate] = word_matches

            sorted_candidates = [key for key, value in sorted(candidates_word_count.items(), key=lambda item: item[1], reverse=True)]
            return sorted_candidates
