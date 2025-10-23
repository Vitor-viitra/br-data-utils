from .formatters import clean_cpf

def is_valid_cpf(cpf: str) -> bool:
    """Verifica se um CPF tem 11 dígitos (validação simples)."""
    return len(clean_cpf(cpf)) == 11