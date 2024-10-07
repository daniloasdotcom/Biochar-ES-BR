import streamlit as st
import pages.posts.potassium as PostPotassium  # Importa o gráfico de potássio

# Função do blog
def blog():
    st.sidebar.image("images/projectLogo.png", use_column_width=True)

    st.sidebar.markdown('**Coordenador Geral**: [Renato Ribeiro Passos](http://lattes.cnpq.br/3882320619443256)')
    st.sidebar.markdown('**Pesquisador Regional**: [Danilo Andrade](https://daniloas.com/)')

    # Título do blog e mensagem de boas-vindas
    st.title("🌿 Blog Interativo de Biocarvões")
    st.header("Bem-vindo ao Nosso Blog de Pesquisas!")

    # Descrição inicial
    st.write("""
            Explore nossas postagens para entender como os biocarvões podem impactar sistemas agrícolas e a retenção de nutrientes no solo.
            Nossos gráficos interativos proporcionam uma visão mais dinâmica sobre os efeitos dos biocarvões.
        """)

    # Postagem mais recente com subtítulo e conteúdo
    st.subheader("📅 Postagem mais recente")
    st.markdown("<h3><em>Biocarvões carregam nutrientes</em></h3>", unsafe_allow_html=True)
    st.write("""
            **Data:** 01/10/2024  
            Dependendo do material de origem do biocarvão, ele pode carregar diferentes quantidades de potássio.  
            Veja como diferentes toneladas de biocarvão influenciam a quantidade de potássio presente em cada aplicação...
        """)

    # Espaçamento antes do botão
    st.markdown("<br>", unsafe_allow_html=True)

    # Botão para ver o gráfico de potássio
    if st.button("🔍 Ver post completo"):
        st.session_state['page'] = 'grafico'  # Alterar o estado da página para 'grafico'

    # Separador entre postagens (se houver mais posts no futuro)
    st.markdown("---")

# Função principal para controlar a navegação
def main():
    # Inicializa a sessão se não estiver definida
    if 'page' not in st.session_state:
        st.session_state['page'] = 'blog'  # A página inicial é o blog

    # Verifica qual página exibir com base no estado
    if st.session_state['page'] == 'blog':
        blog()  # Mostra o blog
    elif st.session_state['page'] == 'grafico':
        PostPotassium.grafico_potassio()  # Mostra o gráfico de potássio

# Executar o aplicativo
if __name__ == "__main__":
    main()

