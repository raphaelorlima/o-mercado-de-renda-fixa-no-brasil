
def taxa_interna_retorno(
    preco_aquisicao: float,
    taxa_cupom: float,
    valor_face: float,
    numero_fluxos_caixa: int,
) -> float:
    if numero_fluxos_caixa and isinstance(numero_fluxos_caixa, float):
        for n in range(1, numero_fluxos_caixa+1):
            return float(n)

    else:
        raise ValueError(
            f"O número do fluxo de caixa não pode ser {type(numero_fluxos_caixa)}, precisa ser float."
        )

    # Todo: (continuação)
    ...
