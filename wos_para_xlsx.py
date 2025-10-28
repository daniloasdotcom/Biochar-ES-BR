import pandas as pd
import os


def parse_wos_record(record_text):
    """
    Analisa um único registro de texto do Web of Science e retorna um dicionário.
    """
    record = {}
    lines = record_text.strip().split('\n')
    current_tag = ""
    for line in lines:
        if line.strip() == "ER":  # End of Record (fim do registro)
            break
        if line.strip() == "":  # Pula linhas vazias
            continue

        # Verifica se a linha começa com uma nova tag (duas letras maiúsculas seguidas de um espaço)
        if len(line) >= 3 and line[0:2].isalpha() and line[0:2].isupper() and line[2] == ' ':
            current_tag = line[0:2].strip()
            content = line[3:].strip()
            if current_tag in record:
                # Se a tag já existe, anexa o conteúdo (para campos multi-linha como AB, CR)
                record[current_tag] += " " + content
            else:
                record[current_tag] = content
        elif current_tag:
            # Se é uma continuação da tag anterior (linha indentada)
            content = line.strip()
            if current_tag in record:
                record[current_tag] += " " + content
            else:
                # Caso de fallback, embora não deva acontecer se as tags sempre começam no início
                record[current_tag] = content
    return record


def process_wos_text_file(file_path):
    """
    Processa um arquivo .text completo do Web of Science e retorna uma lista de dicionários.
    """
    print(f"Lendo o arquivo: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Registros são separados por "ER\n\n" ou "ER\n" no final do arquivo
    raw_records = content.split('ER\n')

    parsed_records = []
    for record_text in raw_records:
        if record_text.strip():  # Garante que não é uma string vazia após a divisão
            parsed_records.append(parse_wos_record(record_text))
    return parsed_records


def export_to_excel(data, output_filename="wos_data.xlsx"):
    """
    Exporta uma lista de dicionários (registros) para um arquivo XLSX.
    """
    if not data:
        print("Nenhum dado para exportar para o Excel.")
        return

    df = pd.DataFrame(data)

    # Exemplo de como reorganizar as colunas para uma melhor visualização (opcional)
    # Você pode personalizar esta lista com as tags que são mais importantes para você
    desired_columns_order = [
        'TI', 'AU', 'SO', 'PY', 'AB', 'DE', 'ID', 'LA', 'DT',
        'C1', 'FU', 'CR', 'NR', 'TC', 'Z9', 'U1', 'U2',
        'PU', 'PI', 'PA', 'SN', 'EI', 'J9', 'JI', 'PD', 'VL', 'IS',
        'AR', 'DI', 'PG', 'WC', 'WE', 'SC', 'GA', 'UT', 'PM', 'OA', 'DA',
        'RP', 'EM', 'RI', 'OI', 'FX', 'VR', 'PT', 'AF'  # Outras tags menos comuns ou que você queira no final
    ]

    # Reordena as colunas e adiciona quaisquer colunas não listadas no final
    existing_columns = df.columns.tolist()
    final_columns = [col for col in desired_columns_order if col in existing_columns]
    final_columns += [col for col in existing_columns if col not in final_columns]

    # Garante que todas as colunas no DataFrame final estão na ordem desejada,
    # e trata casos onde algumas colunas podem não existir em todos os registros.
    df = df.reindex(columns=final_columns, fill_value='')  # Preenche valores ausentes com string vazia

    df.to_excel(output_filename, index=False)
    print(f"Todos os dados foram exportados com sucesso para {output_filename}")


if __name__ == "__main__":
    # --- Caminhos absolutos definidos explicitamente ---
    base_directory = r"C:\Users\Usuário\Desktop"  # Usamos 'r' para "raw string"

    # Lista de todos os seus arquivos de entrada
    input_file_names = [
        #"wos1a500.txt",
        #"wos501a1000.txt",
        #"wos1001a1059.txt",
        "wos_filtered_by_doi.txt"
    ]

    output_file_name = "wos_dados_filtrados.xlsx"  # Nome do arquivo de saída consolidado

    output_file_path = os.path.join(base_directory, output_file_name)
    # ---------------------------------------------------

    all_records = []  # Lista para acumular todos os registros de todos os arquivos

    print(f"O script está configurado para trabalhar no diretório base: {base_directory}")
    print(f"Processando os seguintes arquivos: {', '.join(input_file_names)}")

    for file_name in input_file_names:
        input_file_path = os.path.join(base_directory, file_name)
        try:
            records_from_file = process_wos_text_file(input_file_path)
            all_records.extend(records_from_file)  # Adiciona os registros do arquivo atual à lista total
        except FileNotFoundError:
            print(f"\nAVISO: O arquivo '{input_file_path}' não foi encontrado e será ignorado.")
            print("Certifique-se de que todos os arquivos listados estão no diretório especificado.")
        except Exception as e:
            print(f"\nERRO ao processar o arquivo '{input_file_path}': {e}")

    # Após processar todos os arquivos, exporta os dados acumulados
    export_to_excel(all_records, output_file_path)