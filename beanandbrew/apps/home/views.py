from django.shortcuts import render

# Create your views here.
from django.views.generic import View


class my_view(View):

    def get(self, request):
        return render(request, 'home/index.html', {
            'foo': 'bar',})