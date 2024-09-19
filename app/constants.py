from app.core.config import settings

# Формат даты и времени для использования в отчетах
FORMAT: str = '%Y/%m/%d %H:%M:%S'

# Константы для настройки таблицы в Google Sheets
SPREADSHEET_ROWCOUNT_DRAFT: int = 100  # Количество строк в таблице по умолч.
SPREADSHEET_COLUMN_COUNT_DRAFT: int = 11  # Кол-во колонок в таблице по умолч.

# Константы для проверки длины имени и длины пароля
MAX_LENGTH_FOR_NAME: int = 100  # Максимальная длина имени
MIN_LENGTH_FOR_NAME: int = 1  # Минимальная длина имени
MIN_LENGTH_FOR_PASSWORD: int = 3  # Минимальная длина пароля

# Константы для настройки приложений
DEFAULT_INVESTED_AMOUNT: int = 0  # Значение по умолч. для инвест-ой суммы
TOKEN_LIFETIME: int = 3600  # Время жизни токена в секундах
PASSWORD_MIN_LENGTH: int = 3  # Минимальная длина пароля

# URL для доступа к Google Sheets
GOOGLE_SHEETS_URL: str = 'https://docs.google.com/spreadsheets/d/'

# Права доступа к Google API
SCOPES: tuple[str, str] = (
    'https://www.googleapis.com/auth/spreadsheets',  # Доступ к Google Sheets
    'https://www.googleapis.com/auth/drive',  # Доступ к Google Drive
)

# Конфигурация для авторизации в Google API
INFO: dict[str, str] = {
    'type': settings.type,
    'project_id': settings.project_id,
    'private_key_id': settings.private_key_id,
    'private_key': settings.private_key,
    'client_email': settings.client_email,
    'client_id': settings.client_id,
    'auth_uri': settings.auth_uri,
    'token_uri': settings.token_uri,
    'auth_provider_x509_cert_url': settings.auth_provider_x509_cert_url,
    'client_x509_cert_url': settings.client_x509_cert_url
}

# Шаблон тела документа Google Sheets
SPREADSHEET_BODY: dict = {
    'properties': {
        'title': 'Отчет на ',  # Заголовок документа
        'locale': 'ru_RU',  # Локализация документа
    },
    'sheets': [{
        'properties': {
            'sheetType': 'GRID',  # Тип листа
            'sheetId': 0,  # Идентификатор листа
            'title': 'Лист1',  # Название листа
            'gridProperties': {
                'rowCount': SPREADSHEET_ROWCOUNT_DRAFT,  # Количество строк
                'columnCount': SPREADSHEET_COLUMN_COUNT_DRAFT  # Кол-во колонок
            }
        }
    }]
}

# Шаблон значений таблицы
TABLE_VALUES_DRAFT: tuple[tuple[str, ...], ...] = (
    ('Отчет от',),  # Заголовок отчета
    ('Топ проектов по скорости закрытия',),  # Название отчета
    ('Название проекта', 'Время сбора', 'Описание')  # Заголовки колонок
)
