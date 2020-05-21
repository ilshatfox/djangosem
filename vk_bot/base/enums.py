from typing import Dict, Union, Any, Tuple, Optional


class BaseEnum:
    """
    Базовый класс для перечислений
    """
    values: Dict[Union[str, int], Any] = {}

    @classmethod
    def choices(cls) -> Tuple[Tuple[Union[str, int], Any], ...]:
        """
        Перечисление списка элементов для использовании в django моделях
        """
        return tuple(cls.values.items())

    @classmethod
    def has(cls, value: Optional[Union[int, str]]) -> bool:
        """
        Проверка наличия значения в перечислении
        """
        return value in cls.values.keys()
