from rest_framework.generics import mixins, GenericAPIView
from rest_framework import permissions
from .serializers import ProjectsSerializer, AppsSerializer, TasksSerializer
from .models import Projects, Apps, Tasks


class ProjectsAPIView(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)

        return qs


class AppsAPIView(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]
    queryset = Apps.objects.all()
    serializer_class = AppsSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)

        return qs


class TasksAPIView(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]
    queryset = Tasks.objects.all().order_by('id')
    serializer_class = TasksSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)

        return qs
