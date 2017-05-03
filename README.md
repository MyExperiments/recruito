Recruito

## Dependencies
- Python 3.6
- PostgreSQL
- Python-Psycopg2 - Run: sudo apt-get install python-psycopg2

## Setup Instructions
- Create virtualenv: python3 -m venv env
- Activate env: source env/bin/activate
- clone project repository: git clone repo-url
- move to project root: cd recruito
- Run: pip install -r requirements.txt
- Run: cp recruito/settings/config.json.example recruito/settings/config.json
  config.json contains system level configurations. The settings files (settings.py and settings/development.py or settings/production.py) works on the basis of
  values configured in config.json
- Create database - Follow naming convention recruito_environment_name for
  database name (eg: recruito_development)
  For creating database in postgres - Run: sudo -u postgres createdb -O user_name database_name
- Run: python manage.py migrate
- Specify the settings file to be used while starting the server. For example:
  To start the application in development environment, Run:
  python manage.py runserver --settings=recruito.settings.development
  To start the application in production environment, Run:
  python manage.py runserver --settings=recruito.settings.production

## Coding Standards
- Follow pep-8 standards
- Use 4 spaces for indentation for all files (.py, .js, .css, .html etc)

