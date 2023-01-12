from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from tasks.forms import TaskForm
from tasks.models import Task
# from django.shortcuts import render, redirect
# from django.template import loader


class TaskView(View):
    form_class = TaskForm

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({"message": "success"})
            return JsonResponse({"message": "Validation failed"})
        return JsonResponse({"message": "Wrong request"})

    def get(self,request, *args, **kwargs):
        return render(request, "tasks/index.html", {})

class ViewTaskView(View):

    def get(self,request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, "tasks/view.html", {"tasks":tasks})

class TaskDeleteView(View):
    form_class = TaskForm
    
    def get(self,request, pk, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            task = Task.objects.get(pk=pk)
            task.delete()
            return JsonResponse({"message":"success"})
        return JsonResponse({"message": "ajax failed"})
    
    def post(self, request, pk, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            task = Task.objects.get(pk=pk)
            data = {
                "owner":task.owner,
                "name":task.name,
                "task_date":task.task_date,
                "start_time":task.start_time,
                "end_time":task.end_time
            }
            
            form = self.form_class(request.POST, initial=data)
            if form.is_valid():
                owner = form.cleaned_data['owner']
                name = form.cleaned_data['name']
                task_date = form.cleaned_data['task_date']
                start_time = form.cleaned_data['start_time']
                end_time = form.cleaned_data['end_time']
                
                if form.has_changed():
                    task.owner = owner
                    task.name = name
                    task.task_date = task_date
                    task.start_time = start_time
                    task.end_time = end_time
                    task.save()
                    return JsonResponse({'message': 'success'})
                return JsonResponse({'message': 'dados não editados'})
            
            return JsonResponse({'message': 'dados invalidos'})
        return JsonResponse({'message': 'ajax failed'})



# class TaskUpdateView(View):
#     form_class = TaskForm
    
#     def post(self, request, pk, *args, **kwargs):
#         if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#             task = Task.objects.get(pk-pk)
#             form = self.form_class(request.POST)
#             if form.is_valid():
#                 owner = form.cleaned_data['owner']
#                 name = form.cleaned_data['name']
#                 task_date = form.cleaned_data['task_date']
#                 strat_time = form.cleaned_data['strat_time']
#                 end_time = form.cleaned_data['end_time']
                
#                 task.owner = owner
#                 task.name = name
#                 task.task_date = task_date
#                 task.strat_time = strat_time
#                 task.end_time = end_time
#                 return JsonResponse({'message': 'success'})
#             return JsonResponse({'message': 'dados invalidos'})
#         return JsonResponse({'message': 'ajax failed'})
                
                        
        
    