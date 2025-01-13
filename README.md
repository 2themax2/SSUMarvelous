# SSUMarvelous

Dit is de repository voor het vak Software Startup, voor het project 'ProjectHUB'.

*Geschreven door B. Mellens, M. Nijman, K. Noordhof & M. Reneman*

## Setup
Voor de eerste keer is het nodig om de requirements te installeren, voer de volgende commands uit:
```
pip install -r requirements.txt
```

Verder is het belangrijk om een bestand `.env` te maken dat de structuur van example.env volgt.

cd naar ProjectHUB en voer de volgende commands uit om de database op te zetten:
```
python manage.py makemigrations
python manage.py migrate
```

Om testdata in de databse te laden voer je de volgende commands uit:
```
python manage.py load_questions
python manage.py load_users
```

## Server starten
Om de backend op te starten voer uit:
```
python manage.py runserver
```

Om de front-end op te starten voer uit:
```
cd frontend
npm install
npm run dev
```

# Problem solving
In het geval van een error over één van onze database modellen kan het nodig zijn om de volgende commands uit te voeren:
```
python manage.py makemigrations projects
python manage.py migrate
```
