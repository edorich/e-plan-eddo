from rest_framework import serializers
from .models import Projects, Apps, Tasks


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'name']


class AppsSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source='project.name', read_only=True)

    class Meta:
        model = Apps
        fields = ['id', 'project', 'project_name', 'name']


class TasksSerializer(serializers.ModelSerializer):
    project = serializers.CharField(source='app.project', read_only=True)
    app_name = serializers.CharField(source='app.name', read_only=True)
    pic_name = serializers.CharField(source='pic.nama', read_only=True)

    class Meta:
        model = Tasks
        fields = ['id',
                  'project',
                  'app',
                  'app_name',
                  'name',
                  'pic',
                  'pic_name',
                  'start_date',
                  'end_date',
                  'status',
                  'progress',
                  'note',
                  ]
