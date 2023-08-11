# keip_tech_test

Для запуска проекта:

1. Разархивировать проект

2. Запустить Docker Desktop

3. Перейти в директорию infra/

4. Собрать образы и запустить контейнеры с помощью команды:  
```docker-compose up -d```

5. После успешной сборки открыть Bash

6. Ввести команду для входа в контейнер infra-web-1:  
```docker exec -it infra-web-1 bash```

7. Ввести команду для сбора статики админ панели  
```python manage.py collectstatic --no-input```

8. Закрыть или выйти из контейнера с помощью  
```exit```

9. логин: admin  пароль: 1

10. Проект принимает запросы по следующему адресу:  
```http://localhost/```