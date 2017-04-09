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
- Run: cp local_settings.py.example local_settings.py
- Modify local_settings.py to reflect your system level configurations
- Create database - Follow naming convention recruito_environment_name for
  database name (eg: recruito_development)
  For creating database in postgres - Run: sudo -u postgres createdb -O user_name database_name
- Run: python manage.py migrate

## Coding Standards
- Follow pep-8 standards
- Use 4 spaces for indentation for all files (.py, .js, .css, .html etc)

