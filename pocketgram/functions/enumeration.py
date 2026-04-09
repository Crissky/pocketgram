from enum import Enum


def get_attr_name_from_enum(
    enum_value: Enum, prefix: str = "", sufix: str = ""
) -> str:
    """Retorna o nome do atributo de um Enum, em snake_case, formatado para
    ser usando como atributo de uma classe.
    """

    if not isinstance(enum_value, Enum):
        raise TypeError("O parâmetro deve ser um Enum.")

    return "{}{}{}".format(prefix, enum_value.name.lower(), sufix)


if __name__ == "__main__":
    from enum import IntEnum

    class TestEnum(IntEnum):
        TESTE = 1
        OUTRO_TESTE = 2

    print(get_attr_name_from_enum(TestEnum.TESTE))
    print(get_attr_name_from_enum(TestEnum.TESTE, prefix="__"))
    print(get_attr_name_from_enum(TestEnum.TESTE, sufix="__"))
    print(get_attr_name_from_enum(TestEnum.TESTE, prefix="__", sufix="__"))
