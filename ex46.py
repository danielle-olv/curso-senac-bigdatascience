import re

def validar_cpf_mensagem(cpf: str) -> str:
    #Remove quaisquer caracteres que não sejam números
    cpf_limpo = re.sub(r'\D', '', cpf)

    #