import requests
import base64
import json
import time

# --- Configurações ---
TOKEN_URL = "https://api.cnptia.embrapa.br/token"
API_BASE_URL = "https://api.cnptia.embrapa.br/bioinsumos/v2"
# ATENÇÃO: Substitua pelas suas credenciais reais!
CONSUMER_KEY = 'hxEyqNW2fcw4HbTJf7RfPKUSD9Ia'
CONSUMER_SECRET = '61KbVuAXaARpwmsRdeTw5Ax_LWEa'

OUTPUT_FILENAME = 'todos_bioinsumos.json'
# Delay entre as requisições de página (em segundos) para não sobrecarregar a API
REQUEST_DELAY = 0.5  # Ajuste conforme necessário


# --- Função para obter o token de acesso ---
def get_access_token(token_url, consumer_key, consumer_secret):
    """Obtém o token de acesso da API."""
    try:
        # Codifica as credenciais para Basic Auth
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
        response.raise_for_status()  # Levanta um erro para status HTTP 4xx/5xx

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


# --- Função para buscar uma página de produtos ---
def fetch_products_page(api_url, access_token, page_number=1, other_params=None):
    """Busca uma página de produtos da API."""
    search_endpoint = f"{api_url}/search/produtos-biologicos"
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    params = {'page': page_number}
    if other_params:
        params.update(other_params)

    try:
        print(f"Buscando página {page_number} com parâmetros: {params}...")
        response = requests.get(search_endpoint, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        # Os cabeçalhos de paginação que você encontrou
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
        print(f"Erro HTTP ao buscar produtos (página {page_number}): {http_err}")
        print(f"Resposta do servidor: {response.text}")
    except requests.exceptions.RequestException as req_err:
        print(f"Erro de requisição ao buscar produtos (página {page_number}): {req_err}")
    except Exception as e:
        print(f"Um erro inesperado ocorreu ao buscar produtos (página {page_number}): {e}")
    return None, None


# --- Script Principal ---
if __name__ == "__main__":
    if CONSUMER_KEY == 'SEU_CONSUMER_KEY_AQUI' or CONSUMER_SECRET == 'SEU_CONSUMER_SECRET_AQUI':
        print(
            "ERRO: Por favor, substitua 'SEU_CONSUMER_KEY_AQUI' e 'SEU_CONSUMER_SECRET_AQUI' pelas suas credenciais reais no script.")
    else:
        access_token = get_access_token(TOKEN_URL, CONSUMER_KEY, CONSUMER_SECRET)

        if access_token:
            all_products = []
            current_page = 1
            total_pages_to_fetch = 1  # Inicializa, será atualizado após a primeira chamada

            # Faz a primeira chamada para obter informações de paginação
            print("Fazendo a primeira chamada para determinar a paginação...")
            products_data, pagination = fetch_products_page(API_BASE_URL, access_token, page_number=current_page)

            if products_data and pagination and pagination.get('total_pages'):
                all_products.extend(products_data)  # Adiciona os produtos da primeira página
                total_pages_to_fetch = pagination['total_pages']
                print(f"Total de registros encontrados: {pagination.get('total_records', 'N/A')}")
                print(f"Total de páginas a serem buscadas: {total_pages_to_fetch}")
                print(f"Registros por página: {pagination.get('page_size', 'N/A')}")

                # Itera pelas páginas restantes, se houver
                for page_num in range(current_page + 1, total_pages_to_fetch + 1):
                    time.sleep(REQUEST_DELAY)  # Adiciona um delay para ser gentil com a API
                    products_data, _ = fetch_products_page(API_BASE_URL, access_token, page_number=page_num)
                    if products_data:
                        all_products.extend(products_data)
                    else:
                        print(f"Não foi possível obter dados da página {page_num}. Interrompendo.")
                        break

                # Salva todos os produtos em um arquivo JSON
                try:
                    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
                        json.dump(all_products, f, ensure_ascii=False, indent=4)
                    print(f"Todos os {len(all_products)} produtos foram salvos em '{OUTPUT_FILENAME}'")
                except IOError:
                    print(f"Erro ao salvar os dados no arquivo '{OUTPUT_FILENAME}'.")

            elif products_data:  # Se a primeira chamada retornou dados mas não info de paginação clara
                all_products.extend(products_data)
                print(
                    "A API não retornou cabeçalhos de paginação claros ('X-Pages'). Apenas a primeira página foi baixada.")
                try:
                    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
                        json.dump(all_products, f, ensure_ascii=False, indent=4)
                    print(f"Os {len(all_products)} produtos da primeira página foram salvos em '{OUTPUT_FILENAME}'")
                except IOError:
                    print(f"Erro ao salvar os dados no arquivo '{OUTPUT_FILENAME}'.")
            else:
                print("Não foi possível obter dados da primeira página.")
        else:
            print("Não foi possível obter o token de acesso. Verifique as credenciais e a conexão.")