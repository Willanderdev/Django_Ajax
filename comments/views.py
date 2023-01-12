from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views import View
from comments.forms import CommentForm
from comments.models import Comment

class CommentView(View):
    form_class = CommentForm
    def get(self, request, *args, **kwargs):
        return render(request, "comments/index.html", {})

    # def get_context_data(self, **kwargs):
    #     context = super(CommentView, self).get_context_data(**kwargs)
    #     context['formset'] = self.get_formset()

    #     return context

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                # form = self.form_class()
                return JsonResponse({'message': 'success'})
            return JsonResponse({'message': 'Field couldn\'t validate'}) 
        return JsonResponse({'message': 'Wrong request'})

class CommentDataView(View):
    def get(self, request, *args, **kwargs):
        template = loader.get_template("comments/view.html")
        comments = Comment.objects.all()
        context = {
            "comment_list": comments
        }
        return HttpResponse(template.render(context, self.request))

