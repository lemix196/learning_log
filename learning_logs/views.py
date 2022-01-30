from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

from .models import Topic, Entry 
from .forms import TopicForm, EntryForm


def index(request):
	"""Strona glowna dla aplikacji Learning Log."""
	return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
	"""Wyswietlenie wszystkich tematow."""
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
	"""Wyswietla pojedynczy temat i wszystkie powiazane  nim wpisy."""
	topic = Topic.objects.get(id=topic_id)
	# Upewniamy sie ze temat nalezy do biezacego uzytkownika
	if topic.owner != request.user:
		raise Http404

	entries = topic.entry_set.order_by('-date_added')
	context = {'topic':topic, 'entries':entries}
	return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
	"""Dodaj nowy temat."""
	if request.method != 'POST':
		#Nie przekazano zadnych danych, nalezy utworzyc pusty formularz
		form = TopicForm()
	else:
		#Przekazano dane za pomoca zadania POST, nalezy je przetworzyc
		form = TopicForm(data=request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			form.save()
			return redirect('learning_logs:topics')

	#Wyswietlenie pustego formularza
	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
	"""Dodanie nowego wpisu dla okreslonego tematu."""
	topic = Topic.objects.get(id=topic_id)

	if request.method != 'POST':
		# Nie przekazano zadnych danych, nalezy utworzyc pusty formularz
		form = EntryForm()
	else:
		# Przekazano dane za pomoca zadania POST, nalezy je przetworzyc
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return redirect('learning_logs:topic', topic_id=topic_id)

		# Wyswietlenie pustego formularza
	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
	"""Edycja istniejacego wpisu."""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic

	if topic.owner != request.user:
		raise Http404

	if request.method != 'POST':
		# Zadanie poczatkowe, wypelnienie formularza aktualna trescia wpisu
		form = EntryForm(instance=entry)
	else:
		# PRzekazano dane za pomoca zadania POST, nalezy je przetworzyc
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('learning_logs:topic', topic_id=topic.id)

	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)




