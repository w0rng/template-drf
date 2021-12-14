from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class ExtendViewSet:
    permission_map = {}
    throttle_scope_map = {}
    throttle_class_map = {}
    serializer_class_map = {}

    def get_queryset(self):
        queryset = super().get_queryset()
        serializer_class = self.get_serializer_class()(self.action, self.serializer_class)
        if hasattr(serializer_class, 'setup_eager_loading'):
            queryset = serializer_class.setup_eager_loading(queryset)
        return queryset

    def get_serializer_class(self):
        self.serializer_class = self.serializer_class_map.get(self.action, self.serializer_class)
        return super().get_serializer_class()

    def initialize_request(self, request, *args, **kwargs):
        request = super().initialize_request(request, *args, **kwargs)
        throttle_scope = self.throttle_scope_map.get(self.action, None)
        throttle_class = self.throttle_class_map.get(self.action, None)
        cls_throttle_scope = getattr(self, 'throttle_scope', None)
        cls_throttle = getattr(self, 'throttle_classes', None)
        self.throttle_scope = throttle_scope or cls_throttle_scope or ''
        self.throttle_classes = throttle_class or cls_throttle
        return request

    def get_permissions(self):
        perms = self.permission_map.get(self.action, None)
        if perms and not isinstance(perms, (tuple, list)):
            perms = [perms]
        self.permission_classes = perms or self.permission_classes
        return super().get_permissions()


class ExtendedViewSet(ExtendViewSet, GenericViewSet):
    pass


class ExtendedModelViewSet(ExtendViewSet, viewsets.ModelViewSet):
    pass


class RUDExtendedModelViewSet(
    ExtendViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    pass


class CRDExtendedModelViewSet(
    ExtendViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    pass


class CRUExtendedModelViewSet(
    ExtendViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    pass
