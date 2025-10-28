import pandas as pd
import os
import re


def parse_wos_record(record_text):
    """
    Analisa um único registro de texto da Web of Science e retorna um dicionário.
    Tags multi-linha são armazenadas como listas de strings.
    Melhorado para reconhecer tags que podem ter espaços iniciais no arquivo original,
    tratando-as como novas tags se corresponderem ao padrão TAG_CODE + espaço.
    """
    record = {}
    lines = record_text.strip().split('\n')
    current_tag = ""
    for line_idx, line in enumerate(lines):  # Adicionada line_idx para depuração
        if not line.strip():  # Pula linhas inteiramente em branco
            continue

        # Tenta identificar uma nova tag na linha, mesmo que haja espaços iniciais (indentação)
        # Usamos lstrip() para remover apenas os espaços/tabs à esquerda e verificar o padrão.
        line_content_after_lstrip = line.lstrip()

        is_new_tag_identified = False
        if len(line_content_after_lstrip) >= 3 and \
                line_content_after_lstrip[0:2].isalpha() and \
                line_content_after_lstrip[0:2].isupper() and \
                line_content_after_lstrip[2] == ' ':
            tag_candidate = line_content_after_lstrip[0:2]

            # --- ATENÇÃO: LINHAS DE DEPURACAO - DESCOMENTE SE PRECISAR DIAGNOSTICAR ESPAÇOS ---
            # print(f"DEBUG_PARSE: Registro L{line_idx+1}: Original='{line.strip()}'")
            # print(f"DEBUG_PARSE: -> Identificada NOVA TAG '{tag_candidate}'")
            # print(f"DEBUG_PARSE: -> Conteúdo após lstrip e tag: '{line_content_after_lstrip[3:]}'")
            # ---------------------------------------------------------------------------------

            current_tag = tag_candidate
            content_after_tag_code = line_content_after_lstrip[3:]
            record[current_tag] = [content_after_tag_code.strip()]  # Armazena o conteúdo limpado
            is_new_tag_identified = True

        # Se não identificamos uma nova tag, consideramos que é uma linha de continuação
        if not is_new_tag_identified:
            if current_tag:  # Garante que há uma tag para anexar
                # --- ATENÇÃO: LINHAS DE DEPURACAO - DESCOMENTE SE PRECISAR DIAGNOSTICAR ESPAÇOS ---
                # print(f"DEBUG_PARSE: Registro L{line_idx+1}: Original='{line.strip()}'")
                # print(f"DEBUG_PARSE: -> Identificada CONTINUACAO para TAG '{current_tag}'")
                # print(f"DEBUG_PARSE: -> Conteúdo da continuação: '{line.strip()}'")
                # ---------------------------------------------------------------------------------
                record[current_tag].append(line.strip())  # Anexa a linha (limpada de espaços nas pontas)
            else:
                # Caso de linha malformada no início ou entre registros
                # --- ATENÇÃO: LINHAS DE DEPURACAO - DESCOMENTE SE PRECISAR DIAGNOSTICAR ESPAÇOS ---
                # print(f"DEBUG_PARSE: Registro L{line_idx+1}: Original='{line.strip()}'")
                # print(f"DEBUG_PARSE: -> LINHA IGNORADA (sem tag atual ou nova tag): '{line.strip()}'")
                # ---------------------------------------------------------------------------------
                pass
    return record


def reconstruct_wos_record(record_dict):
    """
    Reconstrói um único registro da Web of Science no formato de texto original
    a partir de seu dicionário, garantindo a ordem e a indentação corretas.
    Assume que os valores em record_dict são listas de strings (linhas).
    """
    reconstructed_lines = []
    # Ordem das tags para reconstrução (conforme sua última solicitação)
    wos_tag_order = [
        "FN", "VR", "PT", "AU", "AF", "TI", "SO", "LA", "DT", "DE", "ID", "AB",
        "C1", "C3", "RP", "EM", "RI", "OI", "FU", "FX", "CR", "NR", "TC", "Z9",
        "U1", "U2", "PU", "PI", "PA", "SN", "EI", "J9", "JI", "PD", "PY", "VL",
        "AR", "DI", "EA", "PG", "WC", "WE", "SC", "GA", "UT", "PM", "OA", "DA", "ER"
    ]

    for tag in wos_tag_order:
        if tag in record_dict and record_dict[tag]:  # Verifica se a tag existe e tem conteúdo
            lines_for_tag = record_dict[tag]

            # Adiciona a primeira linha da tag (TAG seguido do conteúdo)
            # Esta linha NÃO deve ter indentação extra, pois é a linha principal da tag.
            reconstructed_lines.append(f"{tag} {lines_for_tag[0]}")

            # Adiciona as linhas subsequentes com indentação (4 espaços)
            # Isso só acontece se houver mais de uma linha para o conteúdo da tag (ex: resumo longo).
            for i in range(1, len(lines_for_tag)):
                if lines_for_tag[i].strip():  # Ignora linhas vazias ou apenas com espaço
                    reconstructed_lines.append(f"    {lines_for_tag[i]}")

    reconstructed_lines.append("ER")  # Fim do registro
    # Adiciona uma linha em branco extra para separar registros no arquivo de saída
    return "\n".join(reconstructed_lines) + "\n\n"


def process_wos_text_file(file_path):
    """
    Processa um arquivo .text completo da Web of Science linha por linha,
    identificando registros com base nas tags "PT " (início) e "ER" (fim).
    Isso é mais robusto contra variações de formatação e delimitação.
    """
    print(f"Lendo o arquivo: {file_path}")
    all_parsed_records = []
    current_record_lines_buffer = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):  # Começa a contar de 1
                stripped_line = line.strip()

                if stripped_line == "ER":
                    # Fim de um registro. Se o buffer não estiver vazio, processe.
                    if current_record_lines_buffer:
                        record_text = "".join(current_record_lines_buffer)
                        all_parsed_records.append(parse_wos_record(record_text))
                    current_record_lines_buffer = []  # Reinicia o buffer para o próximo registro
                elif line.startswith("PT "):  # detecta o início de um novo registro pela tag "PT "
                    # Início de um novo registro.
                    # Se há algo no buffer, isso significa que o registro anterior não terminou com "ER"
                    # (ou havia dados antes do primeiro PT). Processa o que está no buffer.
                    if current_record_lines_buffer:
                        record_text = "".join(current_record_lines_buffer)
                        all_parsed_records.append(parse_wos_record(record_text))
                    current_record_lines_buffer = [line]  # Começa a coletar linhas para o novo registro
                else:
                    # Acumula a linha atual para o registro em construção
                    current_record_lines_buffer.append(line)

        # Processa o último registro do arquivo, caso ele não termine com "ER" seguido de um novo "PT"
        # Isso é importante para o caso do último registro no arquivo.
        if current_record_lines_buffer:
            record_text = "".join(current_record_lines_buffer)
            parsed_record = parse_wos_record(record_text)
            all_parsed_records.append(parsed_record)

    except UnicodeDecodeError:
        print(f"ERRO: Não foi possível decodificar o arquivo '{file_path}' com UTF-8. Tente 'latin-1' ou 'cp1252'.")
        raise  # Re-lança o erro para interromper a execução

    return all_parsed_records


def normalize_doi(doi_string):
    """Normaliza uma string DOI para comparação consistente (remove prefixos e converte para minúsculas)."""
    if not isinstance(doi_string, str):
        return None
    # Remove prefixos comuns de URL de DOI
    doi_string = doi_string.replace("https://doi.org/", "").replace("http://doi.org/", "").strip()
    # Converte para minúsculas para comparação case-insensitive
    return doi_string.lower()


if __name__ == "__main__":
    # --- Configurações de Diretório e Arquivos ---
    base_directory = r"C:\Users\Usuário\Desktop"

    # Seus arquivos de entrada da Web of Science
    input_wos_file_names = [
        "wos1a500.txt",
        "wos501a1000.txt",
        "wos1001a1059.txt"
    ]

    # --- SUA LISTA DE DOIs DE INTERESSE ---
    dois_of_interest = [
        "10.22146/agritech.10454",
        "10.15446/rev.colomb.quim.v1n49.77811",
        "10.1016/j.jfca.2020.103448",  # O DOI de exemplo que estava falhando
        "10.1111/joss.12864",
        "10.1021/acs.jafc.8b06456",
        "10.22146/agritech.35412",
        "10.3390/metabo10080311",
        "10.1007/s13197-024-05998-y",
        "10.3390/molecules25163648",
        "10.1016/j.foodchem.2020.127904",
        "10.25100/iyc.v23i2.10885",
        "10.1016/j.foodchem.2023.137893",
        "10.17268/sci.agropecu.2016.02.04",
        "10.1111/jfq.12200",
        "10.1016/j.foodres.2018.07.017",
        "10.1016/j.foodres.2019.108943",
        "10.18271/ria.2022.419",
        "10.22146/agritech.17113",
        "10.23850/24220582.5460",
        "10.3390/agriculture10050141",
        "10.3390/molecules28093805",
        "10.3390/s18082570",
        "10.1016/j.lwt.2020.110202",
        "10.3390/antiox8080283",
        "10.1007/s12161-018-1379-7",
        "10.1016/j.foodres.2022.111618",
        "10.3390/molecules26092502",
        "10.1080/07373937.2020.1817933",
        "10.1111/ijfs.17059",
        "10.3390/foods13071031",
        "10.1016/j.foodcont.2016.01.013",
        "10.3390/nu11050985",
        "10.1016/j.foodres.2016.05.001",
        "10.1155/2016/7428515",
        "10.3390/molecules24050825",
        "10.1021/acs.jafc.0c04633",
        "10.31908/19098367.2829",
        "10.1021/acs.jafc.7b02167",
        "10.1111/jfpp.15748",
        "10.3390/foods12051065",
        "10.1016/j.foodchem.2015.08.126",
        "10.22146/agritech.16764",
        "10.1155/2022/9741120",
        "10.1016/j.foodres.2020.109164",
        "10.17268/sci.agropecu.2016.04.01",
        "10.1016/j.foodres.2024.115109",
        "10.1016/j.foodres.2020.109212",
        "10.3389/fpls.2019.01599",
        "10.1007/s00253-017-8126-7",
        "10.25100/iyc.v26i2.13296",
        "10.3390/foods12224144",
        "10.1016/j.crfs.2024.100909",
        "10.25518/1780-4507.20656",
        "10.3389/fnut.2024.1467282",
        "10.3390/app11219964",
        "10.25100/iyc.V25i2",
        "10.3390/toxins15010021",
        "10.1016/j.lwt.2019.108598",
        "10.1038/s41598-020-71822-0",
        "10.1002/jsfa.13016",
        "10.1016/j.foodres.2017.09.096",
        "10.29019/enfoque.v11n3.609",
        "10.1007/s00217-019-03364-3",
        "10.1016/j.foodres.2019.108743",
        "10.1016/j.jfca.2022.104886",
        "10.9755/ejfa.2023.v35.i5.3092",
        "10.1080/07373937.2016.1276072",
        "10.1007/s13197-019-03749-y",
        "10.3390/metabo10030091",
        "10.3390/agronomy11081637",
        "10.1016/j.foodchem.2019.125244",
        "10.1080/19476337.2015.1092052",
        "10.29019/enfoque.v11n4.602",
        "10.1016/j.foodchem.2018.02.045",
        "10.1016/j.talanta.2023.124310",
        "10.1007/s12161-015-0245-0",
        "10.3390/molecules26247618",
        "10.1007/s13197-019-04067-z",
        "10.1007/s13197-023-05838-5",
        "10.1039/c7ja00354d",
        "10.1016/j.foodchem.2022.134209",
        "10.1016/j.fbio.2023.102526",
        "10.3390/molecules29133194",
        "10.1016/j.lwt.2022.113077",
        "10.1016/j.infrared.2022.104092",
        "10.1080/19476337.2017.1297963",
        "10.1016/j.foodchem.2017.03.050",
        "10.22037/afb.v%vi%i.19155",
        "10.3390/foods12132442",
        "10.3390/agronomy11020401",
        "10.1002/jsfa.9359",
        "10.1590/fst.09917",
        "10.1021/acs.jafc.7b04490",
        "10.1016/j.fbp.2022.10.008",
        "10.3390/fermentation9090843",
        "10.3390/foods11070915",
        "10.1016/j.heliyon.2024.e29900",
        "10.1094/PHYTOFR-08-23-0104-R",
        "10.1002/agr.21730",
        "10.1007/s11295-021-01490-2",
        "10.3390/molecules28093755",
        "10.1016/j.foodres.2020.109983",
        "10.19136/era.a4n12.1274",
        "10.5073/JABFQ.2020.093.039",
        "10.1021/acsomega.1c06085"
    ]
    # -----------------------------------------------

    # Nome do arquivo de saída com os registros WoS filtrados
    output_filtered_wos_file_name = "wos_filtered_by_doi.txt"

    output_filtered_wos_path = os.path.join(base_directory, output_filtered_wos_file_name)

    # Normaliza os DOIs de interesse para comparação (maior eficiência com um set)
    normalized_dois_of_interest = {normalize_doi(d) for d in dois_of_interest if d}
    normalized_dois_of_interest.discard(None)  # Remove qualquer DOI 'None' (se houver entradas vazias)

    all_parsed_wos_records = []  # Lista para acumular todos os registros parseados de todos os arquivos

    print(f"O script está configurado para trabalhar no diretório base: {base_directory}")
    print(f"Processando os seguintes arquivos da Web of Science: {', '.join(input_wos_file_names)}")

    # 1. Ler e parsear todos os arquivos da Web of Science
    for file_name in input_wos_file_names:
        input_file_path = os.path.join(base_directory, file_name)
        try:
            records_from_file = process_wos_text_file(input_file_path)
            all_parsed_wos_records.extend(records_from_file)
        except FileNotFoundError:
            print(f"\nAVISO: O arquivo '{input_file_path}' não foi encontrado e será ignorado.")
            print("Certifique-se de que todos os arquivos listados estão no diretório especificado.")
        except Exception as e:
            print(f"\nERRO inesperado ao processar o arquivo '{input_file_path}': {e}")

    if not all_parsed_wos_records:
        print("Nenhum registro encontrado nos arquivos de entrada. Encerrando.")
    else:
        print(f"\nTotal de registros lidos: {len(all_parsed_wos_records)}")
        print(f"Procurando por {len(normalized_dois_of_interest)} DOIs de interesse.")

        # 2. Filtrar os registros com base nos DOIs de interesse
        filtered_wos_records = []
        found_dois = set()

        for record_dict in all_parsed_wos_records:
            # O DOI está na tag 'DI'. O parser retorna uma lista de linhas para cada tag.
            record_dois_lines = record_dict.get('DI')

            # Pega a primeira linha do DOI, que deve conter o valor, e normaliza
            if record_dois_lines and isinstance(record_dois_lines, list) and record_dois_lines[0].strip():
                current_record_doi = normalize_doi(record_dois_lines[0])

                if current_record_doi in normalized_dois_of_interest:
                    filtered_wos_records.append(record_dict)
                    found_dois.add(current_record_doi)

        if not filtered_wos_records:
            print("Nenhum artigo encontrado com os DOIs de interesse fornecidos.")
        else:
            print(f"Encontrados {len(filtered_wos_records)} registros correspondentes para {len(found_dois)} DOIs.")

            # 3. Reconstruir os registros filtrados no formato WoS
            reconstructed_wos_content = ""
            for record_dict in filtered_wos_records:
                reconstructed_wos_content += reconstruct_wos_record(record_dict)

            # 4. Salvar o conteúdo reconstruído em um novo arquivo .txt
            try:
                with open(output_filtered_wos_path, 'w', encoding='utf-8') as f:
                    f.write(reconstructed_wos_content)
                print(f"Arquivo Web of Science filtrado gerado com sucesso em: {output_filtered_wos_path}")

                # Opcional: Relatar DOIs não encontrados
                not_found_dois = normalized_dois_of_interest - found_dois
                if not_found_dois:
                    print("\nOs seguintes DOIs de interesse não foram encontrados nos arquivos:")
                    for doi in sorted(list(not_found_dois)):
                        print(f"- {doi}")

            except Exception as e:
                print(f"\nERRO ao salvar o arquivo filtrado: {e}")