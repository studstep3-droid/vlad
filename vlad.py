def greet(name: str) -> str:
    """

    Повертає привітальне повідомлення.

    Args:

        name (str): Ім'я користувача

    Returns:

        str: Текст вітання

    """

    return f"Привіт, {name}!"


if __name__ == "__main__":
    print(greet("Світ"))
