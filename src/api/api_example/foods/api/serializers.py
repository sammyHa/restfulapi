from rest_framework import serializers
from foods.models import Foods

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = [
            'id',
            'foodname',
            'calories',
            'protein',
            'timestamp'
        ]
        # read_only_fields = ['id', 'foodname', 'calories', 'protein']
