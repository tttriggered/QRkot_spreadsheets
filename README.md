# QRKot(Проект Благотворительных Сборов) + Google Sheets
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-6C4F8B?style=for-the-badge&logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-4D63C1?style=for-the-badge&logo=pydantic&logoColor=white)
![Alembic](https://img.shields.io/badge/Alembic-3D3D3D?style=for-the-badge&logo=python&logoColor=white)
![Google Sheets](https://img.shields.io/badge/Google%20Sheets%20API-34A853?style=for-the-badge&logo=google&logoColor=white)
## Описание проекта
Этот проект представляет собой платформу для благотворительных сборов, разработанную на основе FastAPI и SQLAlchemy. Он позволяет пользователям создавать и управлять благотворительными проектами, делать пожертвования и отслеживать прогресс сбора средств. Также реализована возможность генерации отчёта в Google Sheets по закрытым проектам.
### Основные функции
* **Создание и управление благотворительными проектами:** Пользователи могут создавать благотворительные проекты, указывая необходимую сумму и предоставляя описание.
* **Внесение пожертвований:** Пользователи могут делать пожертвования в различные проекты, а их взносы автоматически учитываются и применяются к достижению цели проекта.
* **Генерация отчёта в Google Sheets:** Для суперпользователей доступна возможность формирования отчёта о закрытых благотворительных проектах с деталями их завершения, экспортируемого в Google Sheets.
* **Отслеживание прогресса сбора средств:** Приложение автоматически обновляет статус каждого проекта по мере поступления пожертвований, помечая проекты как полностью профинансированные, когда они достигают своей цели.
* **Валидация и безопасность:** Приложение включает в себя проверку ввода данных и безопасную обработку пользовательской информации.
### Используемые технологии
* **FastAPI:** Современный, быстрый веб-фреймворк для создания API с использованием Python 3.6+ на основе стандартных аннотаций типов Python.
* **SQLAlchemy:** Инструментарий SQL и библиотека Object-Relational Mapping (ORM) для Python.
* **Alembic:** Легкий инструмент для управления миграциями базы данных, используемый с SQLAlchemy.
* **Pydantic:** Валидация данных и управление настройками с использованием аннотаций типов Python.
* **Google Sheets API:** Для интеграции с Google Sheets и автоматической генерации отчётов.
### Установка и настройка
1. Клонирование репозитория:
   ```bash
   git clone https://github.com/tttriggered/QRkot_spreadsheets
   cd QRkot_spreadsheets
   ```
2. Создание и активация виртуального окружения:
   ```
   python3 -m venv venv  # для Windows:  python -m venv venv
   source venv/bin/activate  # для Windows: venv\Scripts\activate
   ```
3. Установка зависимостей:
   ```
   pip install -r requirements.txt
   ```
4. Настройка конфигурации:
   #### Создайте файл .env в корневом каталоге проекта и добавьте в него следующие переменные:
   ```
   APP_TITLE=QRKot
   APP_DESCRIPTION=Кошачий благотворительный фонд
   DATABASE_URL=sqlite+aiosqlite:///./cat_charity_fund.db
   SECRET=Secret
   FIRST_SUPERUSER_EMAIL=superuser@superuser.com
   FIRST_SUPERUSER_PASSWORD=superuser
   # Настройки для Google API
   TYPE=service_account
   PROJECT_ID=your_project_id
   PRIVATE_KEY_ID=your_private_key_id
   PRIVATE_KEY="your_private_key"
   CLIENT_EMAIL=your_client_email
   CLIENT_ID=your_client_id
   AUTH_URI=https://accounts.google.com/o/oauth2/auth
   TOKEN_URI=https://oauth2.googleapis.com/token
   AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
   CLIENT_X509_CERT_URL=your_client_x509_cert_url
   EMAIL=superuser_email_for_reports
   ```
### Запуск проекта
1. Применение миграций базы данных:
   ```
   alembic upgrade head
   ```
2. Запустите приложение:
   ```
   uvicorn main:app --reload
   ```
Документация Swagger будет доступно по адресу: http://127.0.0.1:8000/docs
Документация ReDoc будет доступно по адресу: http://127.0.0.1:8000/redoc
### Работа с отчётами Google Sheets
Для создания отчёта необходимо выполнить запрос на эндпоинт, доступный только для суперпользователей. В результате вы получите ссылку на отчёт, сгенерированный в Google Sheets, содержащий информацию о закрытых проектах.
## Автор
* [**Тищенко Данил**](https://github.com/tttriggered)
   
