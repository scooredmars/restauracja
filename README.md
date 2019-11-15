# Mój Projekt

## Instalacja django i compressor do środowiska

- pip install django
- pip install django-compressor
- pip install django-libsass

## Uruchamianie wirtualnego środowiska

- pipenv shell
- . env/bin/activate (Linux)

## Aktualizacja pip

- pipenv update

## Uruchamianie serwera WWW

- python app\manage.py runserver

- python app/manage.py runserver (Linux)

## Tworzenie migracji

- python app\manage.py makemigrations portfolio

## Migrowanie plików do bazy danych

- python app\manage.py migrate

## Jeśli nic nie działa użyj tego

- python app\manage.py migrate --run-syncdb

## Tworzenie konta administartora

- python app\manage.py createsuperuser

## Komendy do gita

- git status
- git add --all .
- git commit -m "info comment"
- git push
