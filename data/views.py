from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='post')
class GitCommitView(View):
    def post(self, request):
        print('hello world')

        print(request.body)
        context = {
            'result': request.body,
            'method': 'post'
        }
        return render(request, 'index.html', context=context)

    def get(self, request):
        print('! method=get')
        x = 1
        context = {
            'result': request.body,
            'method': 'get'
        }
        return render(request, 'index.html', context=context)