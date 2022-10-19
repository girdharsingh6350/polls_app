from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse , Http404,HttpResponseRedirect
from requests import request
from .models import Question,choice
from django.urls import reverse
from django.views import generic
from .forms import sing_up
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        fm = sing_up(request.POST)
        if fm.is_valid():
            messages.success(request,"Account create successfully")
            fm.save()
    else:
        fm = sing_up()
    return render(request, 'polls/home.html',{'form':fm})             
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('Polls:results', args=(question.id,)))

