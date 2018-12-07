from rest_framework import generics, mixins
from foods.models import Foods
from .serializers import FoodSerializer
from django.db.models import Q

class FoodAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = FoodSerializer

    def get_queryset(self):
        qs = Foods.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(foodname__icontains=query)).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, *kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, *kwargs)


class FoodPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = FoodSerializer

    def get_queryset(self):
        return Foods.objects.all()
