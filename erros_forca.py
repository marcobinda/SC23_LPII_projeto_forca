
# Cria função que desenha a forca conforme número de erros
def desenha_forca(num_erros):
    erros = ["""
    |-------
    |      |
    |
    |
    |
    |
    |
    ___|___
    """,
    """
    |-------
    |      |
    |      _
    |     |_|
    |
    |
    |
    ___|___
    """,
    """
    |-------
    |      |
    |      _
    |     |_|
    |      |
    |      |
    |
    ___|___
    """,
    """
    |-------
    |      |
    |      _
    |     |_|
    |    --|
    |      |
    |
    ___|___
    """,
    """
    |-------
    |      |
    |      _
    |     |_|
    |    --|--
    |      |
    |
    ___|___
    """,
    """
    |-------
    |      |
    |      _
    |     |_|
    |    --|--
    |      |
    |     /
    ___|___
    """,
    """
    |-------
    |      |
    |      _
    |     |_|
    |    --|--
    |      |
    |     / \\
    ___|___
    """]

    print(erros[num_erros])

