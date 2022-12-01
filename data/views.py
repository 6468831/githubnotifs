from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='post')
class GitCommitView(View):
    def post(self, request):
        print(request.body)
        print('hello world')
        return request.body