from django.db.models import Q, Count
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

    def get_queryset(self):
        queryset = Candidate.objects.all()
        query_param = self.request.query_params.get("name")
        if not query_param:
            return queryset
        else:
            query_words = query_param.split()
            search_conditions = Q()
            for word in query_words:
                search_conditions |= Q(name__icontains=word)
            candidates = queryset.filter(search_conditions).annotate(
                relevance=Count('name', filter=Q(name__icontains=query_words[0]))
            ).order_by('-relevance')
            return candidates
