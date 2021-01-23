from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Subject
import json

# Create your views here.


class FormView(View):
    template_name = 'vote/form_template.html'

    def get(self, request):
        subject_list = Subject.objects.all()
        ctx = {"subjects": subject_list}
        return render(request, self.template_name, ctx)

    def post(self, request):
        subject_id = request.POST['id']
        button_type = request.POST['type']
        subject = Subject.objects.get(id=subject_id)
        if button_type == 'like':
            subject.like = subject.like + 1
        else:
            subject.dislike = subject.dislike + 1
        subject.save()

        subject_list = Subject.objects.all()

        ctx = {"subjects": subject_list}
        return render(request, self.template_name, ctx)


class AjaxView(View):
    template_name = 'vote/ajax_template.html'

    def get(self, request):
        subject_list = Subject.objects.all()
        ctx = {"subjects": subject_list}
        return render(request, self.template_name, ctx)

    def post(self, request):
        req = json.loads(request.body)

        return JsonResponse({'message': 'Hello JSON'})

