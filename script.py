def carregar_camada_satelite(lista_altitudes):
    """
    Filtra e simula o carregamento do Nível de Detalhe (LoD - Level of Detail)
    de acordo com a altitude da câmera virtual para o tema Regiões Litorâneas e Erosão Costeira.
    
    Parâmetros:
        lista_altitudes (list): Lista com valores de altitude em metros.
    """
    if len(lista_altitudes) < 5:
        print("Aviso: A lista deve conter no mínimo 5 valores de altitude.")
        return

    print("=== INICIANDO RENDERIZAÇÃO DE NÍVEL DE DETALHE (LoD) - DINÂMICA COSTEIRA ===\n")

    for idx, altitude in enumerate(lista_altitudes, start=1):
        print(f"Ponto {idx} | Altitude atual: {altitude:,.2f}m")

        if altitude > 10000:
            # Baixa Resolução: Visão macro do planeta / contorno continental
            print(
                " -> [LOD 0 - RAIZ] Carregando camada de BAIXA RESOLUÇÃO: "
                "Mosaico geral da Terra e contorno macro das bacias oceânicas e continentes.\n"
            )
        elif 1000 <= altitude <= 10000:
            # Média Resolução: Visão regional do litoral e estuários
            print(
                " -> [LOD 1 - REGIONAL] Carregando camada de MÉDIA RESOLUÇÃO: "
                "Mosaico regional do arco praial, plumas de sedimentos estuarinos e correntes de deriva litorânea.\n"
            )
        else:
            # Alta Resolução: Visão em detalhes da erosão e estruturas (altitude < 1000m)
            print(
                " -> [LOD 2 - DETALHADO] Carregando camada de ALTA RESOLUÇÃO: "
                "Detalhamento fino do recuo da linha de costa, marcas de escarpamento em falésias, espraiamento de ondas e estruturas de contenção (esporões e quebra-mares).\n"
            )


# --- EXECUÇÃO E TESTE DA FUNÇÃO ---
if __name__ == "__main__":
    # Lista com 6 valores de altitude simulando a aproximação da câmera sobre a zona costeira
    altitudes_simuladas = [18000, 10500, 7200, 2400, 850, 120]
    
    carregar_camada_satelite(altitudes_simuladas)