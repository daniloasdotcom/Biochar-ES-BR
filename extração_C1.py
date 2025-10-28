import pandas as pd
import re

# Caminho do arquivo de entrada
arquivo_txt = r'C:\Users\Usuário\Desktop\wos_processed_spaced_removed.txt'

# Lista para armazenar listas de países por C1
lista_paises_por_c1 = []

# Leitura do arquivo
with open(arquivo_txt, 'r', encoding='utf-8') as f:
    linhas = f.readlines()

i = 0
while i < len(linhas):
    linha = linhas[i]

    # Detectar início de novo registro (tag "PT ") ou "ER"
    if linha.startswith("PT "):
        bloco = []
        while i < len(linhas) and not linhas[i].strip() == "ER":
            bloco.append(linhas[i])
            i += 1
        bloco.append("ER")  # Adiciona o fim do registro
        registro = bloco

        # Extrair C1
        bloco_c1 = ""
        j = 0
        while j < len(registro):
            if registro[j].startswith("C1 "):
                bloco_c1 = registro[j][3:].strip()
                j += 1
                while j < len(registro) and not re.match(r'^[A-Z]{2,3} ', registro[j]):
                    bloco_c1 += ' ' + registro[j].strip()
                    j += 1
                break
            j += 1

        # Extrair países do C1 (se houver)
        if bloco_c1:
            matches = re.findall(r',\s*([A-Z][a-zA-Z\s&-]+)\.', bloco_c1)
            if matches:
                paises_formatados = [f", {pais.strip()}" for pais in matches]
                lista_paises_por_c1.append("; ".join(paises_formatados))
            else:
                lista_paises_por_c1.append("NA")
        else:
            # C1 ausente → buscar autores (AU)
            autores = []
            j = 0
            while j < len(registro):
                if registro[j].startswith("AU "):
                    autores.append(registro[j][3:].strip())
                    j += 1
                    while j < len(registro) and not re.match(r'^[A-Z]{2,3} ', registro[j]):
                        autores.append(registro[j].strip())
                        j += 1
                    break
                j += 1

            lista_paises_por_c1.append("NA")

            # Exibir os autores no terminal
            if autores:
                print("\n[C1 AUSENTE] Autores do artigo:")
                for a in autores:
                    print(f" - {a}")
            else:
                print("\n[C1 AUSENTE] Nenhum autor encontrado no registro.")

    i += 1

# Criar DataFrame e salvar no Excel
df = pd.DataFrame({'Paises por C1': lista_paises_por_c1})
arquivo_excel = r'C:\Users\Usuário\Desktop\paises_por_c1_formatado.xlsx'
df.to_excel(arquivo_excel, index=False)

# Exibir contagem no terminal
print(f'\nTotal de entradas C1 processadas: {len(lista_paises_por_c1)}')
print(f'Arquivo Excel salvo em: {arquivo_excel}')
