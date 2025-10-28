import csv
import os
import re

# Lista completa de colunas exigidas pelo formato Scopus
SCOPUS_COLUMNS = [
    "Authors", "Author full names", "Author(s) ID", "Title", "Year",
    "Source title", "Volume", "Issue", "Art. No.", "Page start", "Page end",
    "Page count", "Cited by", "DOI", "Link", "Affiliations",
    "Authors with affiliations", "Abstract", "Author Keywords", "Index Keywords",
    "Molecular Sequence Numbers", "Chemicals/CAS", "Tradenames", "Manufacturers",
    "Funding Details", "Funding Texts", "References", "Correspondence Address",
    "Editors", "Publisher", "Sponsors", "Conference name", "Conference date",
    "Conference location", "Conference code", "ISSN", "ISBN", "CODEN", "PubMed ID",
    "Language of Original Document", "Abbreviated Source Title", "Document Type",
    "Publication Stage", "Open Access", "Source", "EID"
]

# Função para extrair e mapear campos
def parse_wos_txt(file_path):
    with open(file_path, encoding="utf-8") as f:
        content = f.read()

    records = content.strip().split("\nER\n")
    all_data = []

    for record in records:
        row = {col: "NA" for col in SCOPUS_COLUMNS}
        row["Source"] = "Web of Science"

        lines = record.strip().split("\n")
        current_key = ""

        for line in lines:
            if re.match(r"^[A-Z]{2} ", line):
                current_key, value = line[:2], line[3:].strip()
            else:
                value = line.strip()

            if current_key == "AU":
                row["Authors"] = row["Authors"] + "; " + value if row["Authors"] != "NA" else value
            elif current_key == "AF":
                row["Author full names"] = row["Author full names"] + "; " + value if row["Author full names"] != "NA" else value
            elif current_key == "RI" or current_key == "OI":
                row["Author(s) ID"] = row["Author(s) ID"] + "; " + value if row["Author(s) ID"] != "NA" else value
            elif current_key == "TI":
                row["Title"] = row["Title"] + " " + value if row["Title"] != "NA" else value
            elif current_key == "PY":
                row["Year"] = value
            elif current_key == "SO":
                row["Source title"] = value
            elif current_key == "VL":
                row["Volume"] = value
            elif current_key == "AR":
                row["Art. No."] = value
            elif current_key == "PG":
                row["Page count"] = value
            elif current_key == "DI":
                row["DOI"] = value
            elif current_key == "C3":
                row["Affiliations"] = row["Affiliations"] + "; " + value if row["Affiliations"] != "NA" else value
            elif current_key == "AB":
                row["Abstract"] = row["Abstract"] + " " + value if row["Abstract"] != "NA" else value
            elif current_key == "DE":
                row["Author Keywords"] = value
            elif current_key == "ID":
                row["Index Keywords"] = value
            elif current_key == "FU":
                row["Funding Details"] = value
            elif current_key == "FX":
                row["Funding Texts"] = value
            elif current_key == "CR":
                row["References"] = row["References"] + "; " + value if row["References"] != "NA" else value
            elif current_key == "TC":
                row["Cited by"] = value
            elif current_key == "U2":
                pass  # Ignora U2 para evitar sobrescrever "Cited by"
            elif current_key == "RP":
                row["Correspondence Address"] = value
            elif current_key == "PU":
                row["Publisher"] = value
            elif current_key == "SN":
                row["ISSN"] = value
            elif current_key == "PM":
                row["PubMed ID"] = value
            elif current_key == "LA":
                row["Language of Original Document"] = value
            elif current_key == "JI":
                row["Abbreviated Source Title"] = value
            elif current_key == "DT":
                row["Document Type"] = value
            elif current_key == "OA":
                row["Open Access"] = value
            elif current_key == "UT":
                row["EID"] = value

        all_data.append(row)

    return all_data

# Função para escrever CSV
def write_csv_scopus_format(data, output_path):
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=SCOPUS_COLUMNS)
        writer.writeheader()
        writer.writerows(data)

# Caminho do arquivo
input_file = r"C:\Users\Usuário\Desktop\wos_title_spaced_removed.txt"
output_file = r"C:\Users\Usuário\Desktop\scopus_format_final_title.csv"

# Execução
parsed_data = parse_wos_txt(input_file)
write_csv_scopus_format(parsed_data, output_file)
print("Arquivo gerado com sucesso:", output_file)
