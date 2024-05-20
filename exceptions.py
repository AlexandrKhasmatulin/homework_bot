class EmptyAPIResponse(Exception):
    """Возвращается пустой словарь ответа API."""

    pass


class HomeworkStatusError(Exception):
    """Возвращается некорректный статус домашней работы."""

    pass


class HttpStatusNotOK(Exception):
    """Возвращается код, отличный от 200."""

    pass


class NoHomeworkNameKey(Exception):
    """Нет ключа `homework_name`."""

    pass


class RequestError(Exception):
    """Ошибка при запросе к эндпоинту."""

    pass


class TokensAccessError(Exception):
    """Переменные окружения недоступны."""

    pass


class JsonDecodeError(Exception):
    """Ошибка декодирования Json"""
    pass
