  ## Установка и запуск в PyCharm

    1. Клонируйте репозиторий:

        git clone https://github.com/xa202412xa/genetic_tests_project
        cd genetic_tests_project       

    2. Установите зависимости:
        
        pip install django djangorestframework psycopg2-binary  
        или pip install -r requirements.txt
    
    3. Настройте базу данных PostgreSQL в settings.py:

       settings.py
       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.postgresql',
               'NAME': 'your_db_name',  # Имя вашей базы данных
               'USER': 'your_db_user',  # Имя пользователя PostgreSQL
               'PASSWORD': 'your_password',  # Пароль пользователя PostgreSQL
               'HOST': 'localhost',  # Адрес сервера базы данных
               'PORT': '5432',  # Порт PostgreSQL (по умолчанию 5432)
           }
       }

    4. Создайте и примените миграции:
        
        python manage.py makemigrations
        python manage.py migrate       

    5. Запустите сервер:
        
        python manage.py runserver
        

    ## Примеры запросов в браузере, если сервер запущен по адресу http://127.0.0.1:8000/


    ### Добавление данных
    
    http://127.0.0.1:8000/api/tests

    Content-Type: application/json
    {
        "animal_name": "Буренка",
        "species": "корова",
        "test_date": "2024-11-18",
        "milk_yield": 28.5,
        "health_status": "good"
    }
    {
        "animal_name": "Мурка",
        "species": "овца",
        "test_date": "2024-11-19",
        "milk_yield": 15,
        "health_status": "poor"
    }
    

    ### Получение всех записей
    
    http://127.0.0.1:8000/api/tests
    

    ### Получение записей по виду
    
    http://127.0.0.1:8000/api/tests/species?species=корова
    

    ### Получение статистики
    
    http://127.0.0.1:8000/api/statistics
