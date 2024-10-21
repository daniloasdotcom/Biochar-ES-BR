import streamlit as st
import pages.posts.potassium as PostPotassium  # Importa o gráfico de potássio
from pages.others.sidebar_utils import configure_sidebar

st.set_page_config(
    page_title="Blgo Interativo",
    page_icon="✏️",
    layout="centered"
)

# Função do blog
def blog():
    configure_sidebar()  # Chama a função para configurar a barra lateral

    # Título do blog e mensagem de boas-vindas
    st.title("🌿 Blog Interativo de Biocarvões")
    st.header("Bem-vindo ao Nosso Blog de Pesquisas!")

    # Descrição inicial
    st.write("""
            Explore nossas postagens para entender como os biocarvões podem impactar sistemas agrícolas.
            Nossos gráficos interativos proporcionam uma visão dinâmica sobre os efeitos dos biocarvões.
        """)

    # Postagem mais recente com subtítulo e conteúdo
    st.subheader("📅 Postagem mais recente")
    st.markdown("---")
    st.markdown("<h3><em>Biocarvões de Palha de Café: Fonte de K</em></h3>", unsafe_allow_html=True)
    st.write("**Data:** 01/10/2024")
    st.write("""
            A depender do material orgânico do qual se produzirá o biocarvão haverá também diferentes quantidades de potássio.  
            Veja como diferentes toneladas de biocarvão de palha de café influenciam a quantidade de potássio presente em cada aplicação.
        """)

    # Espaçamento antes do botão
    st.markdown("<br>", unsafe_allow_html=True)

    # Botão para ver o gráfico de potássio
    if st.button("🔍 Ver post completo"):
        st.session_state['page'] = 'grafico'  # Alterar o estado da página para 'grafico'

    # Separador entre postagens (se houver mais posts no futuro)
    st.markdown("---")

# Função para o gráfico de potássio
def grafico_potassio():
    PostPotassium.grafico_potassio()

# Função principal para controlar a navegação
def main():
    # Inicializa a sessão se não estiver definida
    if 'page' not in st.session_state:
        st.session_state['page'] = 'blog'  # A página inicial é o blog

    # Verifica qual página exibir com base no estado
    if st.session_state['page'] == 'blog':
        blog()  # Mostra o blog
    elif st.session_state['page'] == 'grafico':
        grafico_potassio()  # Mostra o gráfico de potássio

# Executar o aplicativo
if __name__ == "__main__":
    main()