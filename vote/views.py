from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
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

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AjaxView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        subject_list = Subject.objects.all()
        ctx = {"subjects": subject_list}
        return render(request, self.template_name, ctx)

    def post(self, request):
        req = json.loads(request.body)
        # {id: number, type: like, dislike}
        button_type = req['type']
        subject_id = req['id']

        subject = Subject.objects.get(id=subject_id)
        if button_type == 'like':
            subject.like = subject.like + 1
        else:
            subject.dislike = subject.dislike + 1
        subject.save()

        return JsonResponse({'id': subject_id, 'type': button_type})

