from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    """
    Настройки приложения.

    Атрибуты:
        app_title (str): Заголовок приложения (по умолчанию 'QRKot').
        app_description (str): Описание приложения (по умолчанию
            'Кошачий благотворительный фонд').
        database_url (str): URL для подключения к базе данных
            (по умолчанию 'sqlite+aiosqlite:///./cat_charity_fund.db').
        secret (str): Секретный ключ для приложения (по умолчанию 'SECRET').
        first_superuser_email (Optional[EmailStr]): Электронная почта первого
            суперпользователя (может быть None).
        first_superuser_password (Optional[str]): Пароль первого
            суперпользователя (может быть None).
        type (Optional[str]): Тип учетных данных (может быть None).
        project_id (Optional[str]): ID проекта (может быть None).
        private_key_id (Optional[str]): ID закрытого ключа (может быть None).
        private_key (Optional[str]): Закрытый ключ (может быть None).
        client_email (Optional[str]): Email
            учетной записи клиента (может быть None).
        client_id (Optional[str]): ID клиента (может быть None).
        auth_uri (Optional[str]): URI для аутентификации (может быть None).
        token_uri (Optional[str]): URI для получения токенов (может быть None).
        auth_provider_x509_cert_url (Optional[str]): URL сертификата
            провайдера аутентификации (может быть None).
        client_x509_cert_url (Optional[str]): URL клиентского
            сертификата (может быть None).
        email (Optional[str]): Email,
            используемый в приложении (может быть None).
    """
    app_title: str = 'QRKot'
    app_description: str = 'Кошачий благотворительный фонд'
    database_url: str = 'sqlite+aiosqlite:///./cat_charity_fund.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    type: Optional[str] = None
    project_id: Optional[str] = None
    private_key_id: Optional[str] = None
    private_key: Optional[str] = None
    client_email: Optional[str] = None
    client_id: Optional[str] = None
    auth_uri: Optional[str] = None
    token_uri: Optional[str] = None
    auth_provider_x509_cert_url: Optional[str] = None
    client_x509_cert_url: Optional[str] = None
    email: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
