# Requirements
1. python3
2. docker
3. docker-compose
4. django 4.2

# Setup
A. Create virtual environment
1. python3 -m venv venv_coofis_assestment
2. pip install -r requirements/local.txt
3. docker-compose -f docker-compose.local.yaml up -d
4. python3 manage.py migrate
5. python3 manage.py runserver