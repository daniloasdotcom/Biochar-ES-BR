import requests
import base64
import json
import time

# --- Configurações ---
TOKEN_URL = "https://api.cnptia.embrapa.br/token"
API_BASE_URL = "https://api.cnptia.embrapa.br/bioinsumos/v2"  # Mesma base
# ATENÇÃO: Substitua pelas suas credenciais reais!
CONSUMER_KEY = 'hxEyqNW2fcw4HbTJf7RfPKUSD9Ia'
CONSUMER_SECRET = '61KbVuAXaARpwmsRdeTw5Ax_LWEa'

# Novo endpoint e nome do arquivo de saída
DATA_ENDPOINT_PATH = "/search/inoculantes"  # <--- MUDANÇA PRINCIPAL AQUI
OUTPUT_FILENAME = 'todos_inoculantes.json'  # <--- Novo nome de arquivo

REQUEST_DELAY = 0.5  # Ajuste conforme necessário


# --- Função para obter o token de acesso (permanece a mesma) ---
def get_access_token(token_url, consumer_key, consumer_secret):
    """Obtém o token de acesso da API."""
    try:
        credentials = f"{consumer_key}:{consumer_secret}"
        basic_auth_header = base64.b64encode(credentials.encode()).decode()
        headers = {
            'Authorization': f'Basic {basic_auth_header}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        payload = {
            'grant_type': 'client_credentials'
        }
        response = requests.post(token_url, headers=headers, data=payload)
        response.raise_for_status()
        token_data = response.json()
        print("Token de acesso obtido com sucesso!")
        return token_data.get('access_token')
    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP ao obter token: {http_err}")
        print(f"Resposta do servidor: {response.text}")
    except requests.exceptions.RequestException as req_err:
        print(f"Erro de requisição ao obter token: {req_err}")
    except Exception as e:
        print(f"Um erro inesperado ocorreu ao obter o token: {e}")
    return None


# --- Função para buscar uma página de dados (modificada para usar DATA_ENDPOINT_PATH) ---
def fetch_data_page(api_url_base, endpoint_path, access_token, page_number=1, other_params=None):
    """Busca uma página de dados do endpoint especificado da API."""
    full_endpoint_url = f"{api_url_base}{endpoint_path}"  # Constrói a URL completa
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    params = {'page': page_number}
    if other_params:
        params.update(other_params)

    try:
        print(f"Buscando página {page_number} de {full_endpoint_url} com parâmetros: {params}...")
        response = requests.get(full_endpoint_url, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        total_records = response.headers.get('X-Records-Count')
        total_pages = response.headers.get('X-Pages')
        page_size = response.headers.get('X-Page-Size')

        pagination_info = {
            'total_records': int(total_records) if total_records else None,
            'total_pages': int(total_pages) if total_pages else None,
            'page_size': int(page_size) if page_size else None
        }

        return data, pagination_info
    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP ao buscar dados (página {page_number}) de {full_endpoint_url}: {http_err}")
        print(f"Resposta do servidor: {response.text}")
    except requests.exceptions.RequestException as req_err:
        print(f"Erro de requisição ao buscar dados (página {page_number}) de {full_endpoint_url}: {req_err}")
    except Exception as e:
        print(f"Um erro inesperado ocorreu ao buscar dados (página {page_number}) de {full_endpoint_url}: {e}")
    return None, None


# --- Script Principal (modificado para usar as novas constantes e a função atualizada) ---
if __name__ == "__main__":
    if CONSUMER_KEY == 'SEU_CONSUMER_KEY_AQUI' or CONSUMER_SECRET == 'SEU_CONSUMER_SECRET_AQUI':
        print(
            "ERRO: Por favor, substitua 'SEU_CONSUMER_KEY_AQUI' e 'SEU_CONSUMER_SECRET_AQUI' pelas suas credenciais reais no script.")
    else:
        access_token = get_access_token(TOKEN_URL, CONSUMER_KEY, CONSUMER_SECRET)

        if access_token:
            all_data_items = []  # Nome genérico para os itens
            current_page = 1
            total_pages_to_fetch = 1

            print(f"Fazendo a primeira chamada para {DATA_ENDPOINT_PATH} para determinar a paginação...")
            # Passa API_BASE_URL e DATA_ENDPOINT_PATH para a função
            items_data, pagination = fetch_data_page(API_BASE_URL, DATA_ENDPOINT_PATH, access_token,
                                                     page_number=current_page)

            if items_data and pagination and pagination.get('total_pages'):
                all_data_items.extend(items_data)
                total_pages_to_fetch = pagination['total_pages']
                print(f"Total de registros encontrados: {pagination.get('total_records', 'N/A')}")
                print(f"Total de páginas a serem buscadas: {total_pages_to_fetch}")
                print(f"Registros por página: {pagination.get('page_size', 'N/A')}")

                for page_num in range(current_page + 1, total_pages_to_fetch + 1):
                    time.sleep(REQUEST_DELAY)
                    # Passa API_BASE_URL e DATA_ENDPOINT_PATH para a função
                    items_data, _ = fetch_data_page(API_BASE_URL, DATA_ENDPOINT_PATH, access_token,
                                                    page_number=page_num)
                    if items_data:
                        all_data_items.extend(items_data)
                    else:
                        print(f"Não foi possível obter dados da página {page_num}. Interrompendo.")
                        break

                try:
                    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
                        json.dump(all_data_items, f, ensure_ascii=False, indent=4)
                    print(f"Todos os {len(all_data_items)} itens foram salvos em '{OUTPUT_FILENAME}'")
                except IOError:
                    print(f"Erro ao salvar os dados no arquivo '{OUTPUT_FILENAME}'.")

            elif items_data:
                all_data_items.extend(items_data)
                print(
                    "A API não retornou cabeçalhos de paginação claros ('X-Pages'). Apenas a primeira página foi baixada.")
                try:
                    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
                        json.dump(all_data_items, f, ensure_ascii=False, indent=4)
                    print(f"Os {len(all_data_items)} itens da primeira página foram salvos em '{OUTPUT_FILENAME}'")
                except IOError:
                    print(f"Erro ao salvar os dados no arquivo '{OUTPUT_FILENAME}'.")
            else:
                print("Não foi possível obter dados da primeira página.")
        else:
            print("Não foi possível obter o token de acesso. Verifique as credenciais e a conexão.")