import json
from rest_framework import serializers

from .. import models
from ..utils import get_string_size


class NodeBodySerializer(serializers.ModelSerializer):

    data = serializers.JSONField(required=False, default=list)

    class Meta:
        model = models.NodeBody
        fields = ('id', 'type', 'meta', 'data', 'node', 'size', 'fields')
        read_only_fields = ('fields', 'size', 'id')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        data = representation['data']
        fields = representation.pop('fields')
        combined_data = {}
        if type(data) == list and len(data) > 0:
            for index, field_name in enumerate(fields):
                combined_data[field_name] = data[index]
        representation['data'] = combined_data
        return representation

    def create(self, validated_data):
        if 'data' in validated_data:
            data = validated_data.get('data', None)
            if type(data) is dict:
                validated_data['fields'] = list(data.keys())
                validated_data['data'] = list(data.values())
            validated_data['size'] = get_string_size(json.dumps(data))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'meta' in validated_data:
            validated_data['meta'] = {
                **instance.meta,
                **validated_data.get('meta', {})
            }

        if 'data' in validated_data:
            data = validated_data.get('data', None)
            if type(data) is dict:
                validated_data['fields'] = list(data.keys())
                validated_data['data'] = list(data.values())
            validated_data['size'] = get_string_size(json.dumps(data))

        only_type_changed = list(validated_data.keys()) == ['type']
        if only_type_changed:
            validated_data['meta'] = {}
            validated_data['data'] = {}
        return super().update(instance, validated_data)
