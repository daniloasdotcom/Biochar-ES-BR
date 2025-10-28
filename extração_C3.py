import pandas as pd

# Caminho do arquivo
arquivo_txt = r'C:\Users\Usuário\Desktop\wos_title_spaced_removed.txt'

# Lista final de dados
registros = []

# Variáveis temporárias
current_aus = []
current_c3 = []
current_di = "NA"

# Leitura do arquivo
with open(arquivo_txt, 'r', encoding='utf-8') as f:
    linhas = f.readlines()

i = 0
while i < len(linhas):
    linha = linhas[i]

    # Coletar autores
    if linha.startswith("AU "):
        current_aus.append(linha[3:].strip())

    # Coletar C3 (pode se estender por várias linhas)
    elif linha.startswith("C3 "):
        c3_linha = linha[3:].strip()
        current_c3.append(c3_linha)

        # Coleta linhas subsequentes que são continuações (sem tag no início)
        j = i + 1
        while j < len(linhas) and not linhas[j][:2].isalpha():
            current_c3.append(linhas[j].strip())
            j += 1
        i = j - 1  # ajusta o índice principal

    # Coletar DOI
    elif linha.startswith("DI "):
        current_di = linha[3:].strip()

    # Quando encontrar um RP, encerra o bloco atual
    elif linha.startswith("RP "):
        c3_final = " ".join(current_c3) if current_c3 else "NA"

        for au in current_aus:
            registros.append({
                'AU': au,
                'C3': c3_final,
                'DI': current_di
            })

        # Reinicia para o próximo bloco
        current_aus = []
        current_c3 = []
        current_di = "NA"

    i += 1

# Criar DataFrame
df = pd.DataFrame(registros)

# Salvar no Excel
arquivo_excel = r'C:\Users\Usuário\Desktop\au_c3_di_pareado_completo_title.xlsx'
df.to_excel(arquivo_excel, index=False)

# Estatísticas
print(f'Total de autores processados: {len(df)}')
print(f'Arquivo Excel salvo com sucesso em: {arquivo_excel}')
