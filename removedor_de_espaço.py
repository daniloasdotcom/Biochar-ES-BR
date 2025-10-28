import os

def process_text_file(input_filepath, output_filepath):
    """
    Processa um arquivo de texto, removendo espaços iniciais de linhas específicas.

    Args:
        input_filepath (str): O caminho para o arquivo de entrada.
        output_filepath (str): O caminho para o arquivo de saída onde o texto processado será salvo.
    """
    try:
        with open(input_filepath, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

        processed_lines = []
        for line in lines:
            # Verifica se a linha começa com os padrões específicos e remove os espaços
            # Usamos strip() antes de startswith() para garantir que não haja espaços
            # invisíveis no final da linha que possam interferir.
            # Em seguida, usamos lstrip() para remover apenas os espaços iniciais.
            if line.strip().startswith(('Z9', 'U1', 'U2', 'J9', 'C1', 'C3')):
                processed_lines.append(line.lstrip())
            else:
                processed_lines.append(line)

        with open(output_filepath, 'w', encoding='utf-8') as outfile:
            outfile.writelines(processed_lines)

        print(f"Arquivo processado com sucesso! Saída salva em: {output_filepath}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{input_filepath}' não foi encontrado. Por favor, verifique o caminho.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# --- Exemplo de uso ---
if __name__ == "__main__":
    # Define o caminho completo para o arquivo de entrada
    input_file_name = "wos_filtered_by_title.txt"
    input_directory = r"C:\Users\Usuário\Desktop" # Use r"" para string raw para evitar problemas com backslashes
    input_full_path = os.path.join(input_directory, input_file_name)

    # Define o caminho completo para o arquivo de saída
    output_file_name = "wos_title_spaced_removed.txt" # Um novo nome para o arquivo de saída processado
    output_full_path = os.path.join(input_directory, output_file_name)

    # Chama a função para processar o arquivo
    process_text_file(input_full_path, output_full_path)

    # (Opcional) Você pode adicionar código aqui para verificar o conteúdo do arquivo de saída
    # se desejar, similar ao exemplo anterior, mas adaptado para o caminho completo.
    # print("\nConteúdo do arquivo de saída (wos_processed.txt):")
    # try:
    #     with open(output_full_path, "r", encoding="utf-8") as f:
    #         print(f.read())
    # except FileNotFoundError:
    #     print("Arquivo de saída não encontrado para leitura.")
    # except Exception as e:
    #     print(f"Erro ao ler o arquivo de saída: {e}")