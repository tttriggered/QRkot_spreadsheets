from typing import Final

# Сообщения об ошибках, связанных с проектами

PROJECT_NOT_FOUND: Final[str] = 'Проект не найден!'

DUPLICATE_PROJECT_NAME: Final[str] = 'Проект с таким именем уже существует!'

INVESTMENT_AMOUNT_TOO_LOW: Final[str] = (
    'Новая сумма меньше, чем уже проинвестировано!'
)

PROJECT_HAS_FUNDING: Final[str] = ('Проект уже финансировался, '
                                   'удаление невозможно!')

CLOSED_PROJECT_EDIT: Final[str] = ('Редактирование закрытого '
                                   'проекта невозможно!')
