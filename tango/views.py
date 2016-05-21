from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone


from .models import Choice, Question

class IndexView(generic.ListView):
	template_name = 'tango/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		#Return the last 5 published questions
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'tango/detail.html'

	def get_queryset(self):
		#Excludes any questions that arent published yet
		return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
	model = Question
	template_name = 'tango/results.html'

def about(request):
	return HttpResponse("This is the about page")	

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		#Redisplay the question voting form
		return render(request, 'tango/detail.html', {
			'question': question,
			'error_message': 'You didnt select a choice.',
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
		return HttpResponseRedirect(reverse('tango:results', args=(question.id,)))


def get_queryset(self):
	#Return the last 5 published questions
	return Question.objects.filter(
			pub_date__lte=timezone.now()
	).order_by('-pub_date')[:5]






