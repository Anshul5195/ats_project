from django.urls import path
from ats_app.views import CandidateViewSet

urlpatterns = [
    path('candidates/', CandidateViewSet.as_view({"get": "list", "post": "create"}), name='candidate-list-create'),  # this is used for list, create and search candidates
    path('candidates/<uuid:unique_id>/', CandidateViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name='candidate-retrieve-update-destroy'),  # this is used for retrieve, update and delete candidates
]
