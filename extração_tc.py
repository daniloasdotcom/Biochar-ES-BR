import openpyxl

# Caminho do arquivo de entrada e saída
input_file = r"C:\Users\Usuário\Desktop\wos_filtered_by_title.txt"
output_file = r"C:\Users\Usuário\Desktop\tc_values_title.xlsx"

# Lista para armazenar os valores de TC
tc_values = []

# Abrir e processar o arquivo
with open(input_file, encoding="utf-8") as f:
    content = f.read()

records = content.strip().split("\nER\n")

for record in records:
    lines = record.strip().split("\n")
    for line in lines:
        if line.startswith("TC "):
            tc_value = line[3:].strip()
            tc_values.append(tc_value)
            break  # só um TC por registro

# Criar arquivo .xlsx
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "TC Values"
sheet["A1"] = "Cited by (TC)"

# Preencher os dados
for i, value in enumerate(tc_values, start=2):
    sheet[f"A{i}"] = value

# Salvar arquivo
workbook.save(output_file)
print(f"Arquivo gerado com sucesso: {output_file}")
