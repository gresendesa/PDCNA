"""from rest_framework import serializers

class MaxInt:
    def __init__(self, base):
        self.base = base
    def __call__(self, value):
        if value > self.base:
            message = f'This field requires an integer lower than {self.base}'
            raise serializers.ValidationError(message)

class MinInt:
    def __init__(self, base):
        self.base = base
    def __call__(self, value):
        if value < self.base:
            message = f'This field requires an integer higher than {self.base}'
            raise serializers.ValidationError(message)

"""