import csv
import os


def transformar_csv(caminho_entrada, caminho_saida):
    """
    Transforma um arquivo CSV:
    - Muda o delimitador de ';' para ','
    - Adiciona aspas em torno de cada título do cabeçalho

    Args:
        caminho_entrada (str): O caminho para o arquivo CSV de entrada.
        caminho_saida (str): O caminho para o arquivo CSV de saída.
    """
    try:
        # Tenta abrir com 'latin-1', que é uma codificação comum para arquivos brasileiros
        with open(caminho_entrada, 'r', newline='', encoding='latin-1') as infile:
            reader = csv.reader(infile, delimiter=';')

            # Lê o cabeçalho
            header = next(reader)

            # Adiciona aspas a cada elemento do cabeçalho
            new_header = [f'"{col}"' for col in header]

            # O arquivo de saída pode continuar sendo 'utf-8' para melhor compatibilidade
            with open(caminho_saida, 'w', newline='', encoding='utf-8') as outfile:
                writer = csv.writer(outfile, delimiter=',')

                # Escreve o novo cabeçalho
                writer.writerow(new_header)

                # Escreve as demais linhas
                for row in reader:
                    writer.writerow(row)

        print(f"Arquivo transformado com sucesso! Salvo em: {caminho_saida}")

    except FileNotFoundError:
        print(
            f"Erro: O arquivo de entrada '{caminho_entrada}' não foi encontrado. Verifique o caminho e o nome do arquivo.")
    except UnicodeDecodeError:
        print(f"Erro de decodificação: Não foi possível ler o arquivo '{caminho_entrada}' com a codificação 'latin-1'.")
        print("Tente verificar a codificação real do arquivo. Outras opções comuns são 'windows-1252' ou 'cp1252'.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


# --- Caminhos dos arquivos ---
diretorio_desktop = r'C:\Users\Usuário\Desktop'

nome_arquivo_entrada = 'pasta3.csv'
caminho_arquivo_entrada = os.path.join(diretorio_desktop, nome_arquivo_entrada)

nome_arquivo_saida = 'pasta3_transformado.csv'
caminho_arquivo_saida = os.path.join(diretorio_desktop, nome_arquivo_saida)

# Chama a função para transformar o CSV
transformar_csv(caminho_arquivo_entrada, caminho_arquivo_saida)