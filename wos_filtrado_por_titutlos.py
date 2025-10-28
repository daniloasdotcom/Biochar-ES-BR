import os
import re

def parse_wos_record(record_text):
    record = {}
    lines = record_text.strip().split('\n')
    current_tag = ""
    for line in lines:
        if not line.strip():
            continue
        line_content_after_lstrip = line.lstrip()
        is_new_tag_identified = False
        if len(line_content_after_lstrip) >= 3 and \
                line_content_after_lstrip[0:2].isalpha() and \
                line_content_after_lstrip[0:2].isupper() and \
                line_content_after_lstrip[2] == ' ':
            tag_candidate = line_content_after_lstrip[0:2]
            current_tag = tag_candidate
            content_after_tag_code = line_content_after_lstrip[3:]
            record[current_tag] = [content_after_tag_code.strip()]
            is_new_tag_identified = True
        if not is_new_tag_identified:
            if current_tag:
                record[current_tag].append(line.strip())
    return record

def reconstruct_wos_record(record_dict):
    reconstructed_lines = []
    wos_tag_order = [
        "FN", "VR", "PT", "AU", "AF", "TI", "SO", "LA", "DT", "DE", "ID", "AB",
        "C1", "C3", "RP", "EM", "RI", "OI", "FU", "FX", "CR", "NR", "TC", "Z9",
        "U1", "U2", "PU", "PI", "PA", "SN", "EI", "J9", "JI", "PD", "PY", "VL",
        "AR", "DI", "EA", "PG", "WC", "WE", "SC", "GA", "UT", "PM", "OA", "DA", "ER"
    ]
    for tag in wos_tag_order:
        if tag in record_dict and record_dict[tag]:
            lines_for_tag = record_dict[tag]
            reconstructed_lines.append(f"{tag} {lines_for_tag[0]}")
            for i in range(1, len(lines_for_tag)):
                if lines_for_tag[i].strip():
                    reconstructed_lines.append(f"    {lines_for_tag[i]}")
    reconstructed_lines.append("ER")
    return "\n".join(reconstructed_lines) + "\n\n"

def process_wos_text_file(file_path):
    print(f"Lendo o arquivo: {file_path}")
    all_parsed_records = []
    current_record_lines_buffer = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.strip()
                if stripped_line == "ER":
                    if current_record_lines_buffer:
                        record_text = "".join(current_record_lines_buffer)
                        all_parsed_records.append(parse_wos_record(record_text))
                    current_record_lines_buffer = []
                elif line.startswith("PT "):
                    if current_record_lines_buffer:
                        record_text = "".join(current_record_lines_buffer)
                        all_parsed_records.append(parse_wos_record(record_text))
                    current_record_lines_buffer = [line]
                else:
                    current_record_lines_buffer.append(line)
        if current_record_lines_buffer:
            record_text = "".join(current_record_lines_buffer)
            all_parsed_records.append(parse_wos_record(record_text))
    except UnicodeDecodeError:
        print(f"ERRO: Não foi possível decodificar o arquivo '{file_path}' com UTF-8.")
        raise
    return all_parsed_records

def normalize_title(title_string):
    if not isinstance(title_string, str):
        return None
    return title_string.replace(" ", "").lower()

if __name__ == "__main__":
    base_directory = r"C:\Users\Usuário\Desktop"
    input_wos_file_names = [
        "wos1a500.txt",
        "wos501a1000.txt",
        "wos1001a1059.txt"
    ]

    titles_of_interest = [
        "fermentationanddryingmethodforthebenefitofobtainingwhitechocolatefromcriollocacao(theobromacacaol.),ecuadorian",
        "operatingparametersmoreappropriateintheprocessofroastedcocoaalmonds",
        "effectoftheturningonthesensoryprofilesofthefermentedcocoa",
        "theeffectsofroastingtimeofunfermentedcocoaliquorusingtheoilbathmethodsonphysicochemicalpropertiesandvolatilecompoundprofiles",
        "theindigenouslacticacidbacteriafromfermentedcocoabeananditsroleincocoabeanfermentation.",
        "overviewoftheacrylamidecontentofcocoaandchocolate",
        "physicalandchemicalpropertiesofcacaocultivars(theobromacacaol.)fromecuadorandperu",
        "studyofthespontaneouscocoafermentation(theobromacacaoi.)andevaluationofbeanqualityinaproductiveunitinsmall-scale",
        "sensorialqualitiesofportuguesa'scocoaduringfermentationfortwodifferentseasonsandedaphoclimaticconditions",
        "understandingthechemistryandevolutionofchocolateflavor",
        "qualityandsafetyofcocoabeans",
        "analysingsensoryandprocessingqualityofcocoa",
        "biochemistryofcocoafermentation",
        "trackingdownthecocoaflavourstandardizationofthefermentationofcocoabeans",
        "candidaspasastartercultureforcocoa(theobromacacaol.)beansfermentation",
        "fermentationofcacaocriolloandccn-51:lactobacillusfermentumbacteriumandsaccharomycescerevisiaeyeast",
        "elaborationofanalcoholicdrinkfromtheaerobicfermentationofmucilageofcocoa(theobromacacaol.)",
        "evolutionofprocianidinas'scontentinbeansofcriollococoa(theobromacocoal.)",
        "cultivationofpenicilliumroquefortiincocoashelltoproduceandcharacterizeitslipaseextract",
        "identificationandquantificationof(+)-catechinsandprocyanidinsincocoafromocumaredelacosta,venezuela",
        "physicalqualityofalmondsintwenty-oneinterconnectionalcrossesofcocoa(theobromacacaol.)inecuador",
        "effectofthepost-harvesttreatmentonthepolyphenolspresentinporcelaincreolecacaoofzuliastate",
        "understandingtheheatstabilityandsolubilityofcocoabeanshellextractasantioxidantandantibacterialfunctionalingredients",
        "chemicalprofileof12nationaltypecocoa(theobromacacaol.)",
        "bibliometricvisualizationandresearchtrendsinthecocoaareaworldwide.period2011-2016",
        "effectofpostharvesttreatmentincocoapolyphenolsbiscucuyandchabasquen,portuguesa",
        "physicochemicalandsensorydiversityof60elitetreesoftheobromacacaol.,fromsouthernecuador",
        "methodsofcocoafermentationanddrying",
        "microbialactivitiesduringcocoafermentation",
        "thefunctionalroleoflacticacidbacteriaincocoabeanfermentation"
    ]

    normalized_titles_of_interest = {normalize_title(t) for t in titles_of_interest if t}

    output_filtered_wos_file_name = "wos_filtered_by_title.txt"
    output_filtered_wos_path = os.path.join(base_directory, output_filtered_wos_file_name)

    all_parsed_wos_records = []

    print(f"O script está configurado para trabalhar no diretório base: {base_directory}")
    print(f"Processando os seguintes arquivos da Web of Science: {', '.join(input_wos_file_names)}")

    for file_name in input_wos_file_names:
        input_file_path = os.path.join(base_directory, file_name)
        try:
            records_from_file = process_wos_text_file(input_file_path)
            all_parsed_wos_records.extend(records_from_file)
        except FileNotFoundError:
            print(f"\nAVISO: O arquivo '{input_file_path}' não foi encontrado e será ignorado.")
        except Exception as e:
            print(f"\nERRO ao processar o arquivo '{input_file_path}': {e}")

    if not all_parsed_wos_records:
        print("Nenhum registro encontrado nos arquivos de entrada. Encerrando.")
    else:
        print(f"\nTotal de registros lidos: {len(all_parsed_wos_records)}")
        print(f"Procurando por {len(normalized_titles_of_interest)} TÍTULOS de interesse.")

        filtered_wos_records = []
        found_titles = set()

        for record_dict in all_parsed_wos_records:
            record_title_lines = record_dict.get('TI')
            if record_title_lines and isinstance(record_title_lines, list):
                full_title = " ".join(record_title_lines).strip()
                normalized_title = normalize_title(full_title)
                if normalized_title in normalized_titles_of_interest:
                    filtered_wos_records.append(record_dict)
                    found_titles.add(normalized_title)

        if not filtered_wos_records:
            print("Nenhum artigo encontrado com os TÍTULOS de interesse fornecidos.")
        else:
            print(f"Encontrados {len(filtered_wos_records)} registros correspondentes para {len(found_titles)} títulos.")

            # Verificar títulos duplicados
            title_counts = {}
            for record_dict in filtered_wos_records:
                record_title_lines = record_dict.get('TI', [])
                full_title = " ".join(record_title_lines).strip()
                normalized_title = normalize_title(full_title)
                title_counts[normalized_title] = title_counts.get(normalized_title, 0) + 1

            duplicated_titles = {t: c for t, c in title_counts.items() if c > 1}
            if duplicated_titles:
                print("\nATENÇÃO: Títulos duplicados encontrados entre os registros:")
                for title, count in duplicated_titles.items():
                    print(f"- '{title}' apareceu {count} vezes")
            else:
                print("Nenhum título duplicado encontrado entre os registros filtrados.")

            reconstructed_wos_content = ""
            for record_dict in filtered_wos_records:
                reconstructed_wos_content += reconstruct_wos_record(record_dict)

            try:
                with open(output_filtered_wos_path, 'w', encoding='utf-8') as f:
                    f.write(reconstructed_wos_content)
                print(f"\nArquivo Web of Science filtrado gerado com sucesso em: {output_filtered_wos_path}")

                not_found_titles = normalized_titles_of_interest - found_titles
                if not_found_titles:
                    print("\nOs seguintes TÍTULOS de interesse não foram encontrados nos arquivos:")
                    for title in sorted(list(not_found_titles)):
                        print(f"- {title}")

            except Exception as e:
                print(f"\nERRO ao salvar o arquivo filtrado: {e}")
