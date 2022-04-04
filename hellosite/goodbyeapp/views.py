from django.shortcuts import render
from django.views import View

# Create your views here.
class GoodbyeWorldView(View):
  def get(self, request):
    return render(request=request, template_name='goodbye_world.html')

class GoodbyeView(View):
  def get(self, request, name='everyone'):
    context = {'name':name}
    return render(
      request=request, template_name='goodbye_name.html', 
      context=context
    )
