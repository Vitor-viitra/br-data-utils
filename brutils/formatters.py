def clean_cpf(cpf: str) -> str:
    """Remove pontuação de um CPF e retorna apenas dígitos."""
    return "".join(filter(str.isdigit, str(cpf)))

def clean_cnpj(cnpj: str) -> str:
    """Remove pontuação de um CNPJ e retorna apenas dígitos."""
    return "".join(filter(str.isdigit, str(cnpj)))