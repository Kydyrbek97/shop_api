from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework import permissions , mixins
from product.permissions import IsAuthor
from rating.models import Review
from . import serializers


class UpdateDestroyAPIView(mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           GenericAPIView):
    """
    Concrete view for , updating or deleting a model instance.
    """

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ReviewCreateApiView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializers

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RetrieveUpdateDeleteApiView(UpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewUpdateSerializers
    permission_classes = (permissions.IsAuthenticated, IsAuthor)

