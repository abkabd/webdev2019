from django.shortcuts import render
from .models import TaskList
from django.http import HttpResponse, JsonResponse


def getAllTasksList(request):

    arr = TaskList.objects.all()
    arr1 = [i.to_json() for i in arr]

    return JsonResponse(arr1, safe=False)


def getOneTaskList(request, pk):
    return JsonResponse(TaskList.objects.get(id=pk).to_json(), safe=False)


def getTaskByTaskListID(request, pk):
    arr = TaskList.objects.get(id=pk)
    massiv = [i.to_json() for i in arr.task_set.all()]

    return JsonResponse(massiv, safe=False)

