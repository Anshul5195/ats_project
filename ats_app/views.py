from django.db.models import Q, Value
from django.db.models.functions import Length, Replace
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
        query_param = self.request.query_params.get("name")
        if not query_param:
            return Candidate.objects.all()
        else:
            query_words = query_param.split()
            search_conditions = Q()
            for word in query_words:
                search_conditions |= Q(name__icontains=word)

            # Annotate candidates with relevance(word match count)
            candidates = Candidate.objects.filter(search_conditions).annotate(
                relevance=sum(
                    (Length('name') - Length(Replace(expression='name', text=Value(word), replacement=Value('')))) / Length(Value(word))
                    for word in query_words
                )
            ).order_by('-relevance')
            return candidates
