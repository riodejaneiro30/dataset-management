# Dataset Management System

Make sure you have installed Python 3 by using this command
```bash
python --version
```

After installing Python 3 and after you clone this repository now we recommend you to make virtual environment inside the root folder of the downloaded repo
```bash
python -m venv env
```


Activate virtual environment
```bash
source env\Scripts\activate
```

Install requirements in requirements.txt
```bash
pip install -r requirements.txt
```


Collect static files
```bash
python manage.py collectstatic --noinput
```

Migrate your app

```bash
python manage.py makemigrations
python manage.py migrate
```

Load dummy data

```bash
python manage.py loaddata db.json
```

Now you can access the app using your browser with the following link: `127.0.0.1:8000`