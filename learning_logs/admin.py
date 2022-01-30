from django.contrib import admin

from .models import Topic, Entry #importuje moja klase Topic z modeli (.models wyszukuje plik models.py w katalogu gdzie jest admin.py)

admin.site.register(Topic) #rejestruje klase Topic w witrynie administracyjnej 
admin.site.register(Entry) #to samo dla klasy Entry