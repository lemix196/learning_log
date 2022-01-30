"""Definiuje wzorce adresow URL dla learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
	#Strona glowna
	path('', views.index, name='index'),
	#Wyswietlanie wszystkich tematow
	path('topics/', views.topics, name='topics'),
	#Strona szczegolowa dotyzaca pojedynczego tematu
	path('topics/(<int:topic_id>)/', views.topic, name='topic'),
	#Strona do dodawania tematow przez uzytkownika
	path('new_topic/', views.new_topic, name='new_topic'),
	#Strona do dodawania wpisow przez uzytkownika
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
	# Strona przeznaczona do edycji wpisu
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),



]