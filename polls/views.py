from django.shortcuts import render

from .models import Question,Choice

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = {'latest_question_list': latest_question_list}
  return render(request,'polls/index.html', context)
  

def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404('question does not exist')
  return render(request, 'result.html',{'question':question})
  
  
def result(request, question_id):
  question = get_object_or_404(question, question_id)
  return render(request, 'result.html',{'question':question})
