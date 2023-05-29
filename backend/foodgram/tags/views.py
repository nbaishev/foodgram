from rest_framework import viewsets

from tags.models import Tag
from tags.serializers import TagSerializer
from utils.permissions import IsAdminOrReadOnly


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAdminOrReadOnly,)
