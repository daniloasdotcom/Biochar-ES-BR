import streamlit as st
import pages.posts.potassium as PostPotassium  # Importa o gráfico de potássio

# Função do blog
def blog():
    st.sidebar.image("images/projectLogo.png", use_column_width=True)

    st.sidebar.markdown('**Coordenador Geral**: [Renato Ribeiro Passos](http://lattes.cnpq.br/3882320619443256)')
    st.sidebar.markdown('**Pesquisador Regional**: [Danilo Andrade](https://daniloas.com/)')

    st.title("Blog")
    st.header("Bem-vindo ao Nosso Blog Interativo!")

    st.write("""
        Através de nossas postagens você poderá interagir com nossos gráficos e ter uma visão dinâmica
        dos efeitos dos biocarvões em sistemas de produção agrícola
    """)

    st.subheader("Postagem mais recente")
    st.write("""
        **Título do Post:** Biocarvões carregão nutrientes  
        **Data:** 01/10/2024  
        À depender do material que deu origem ao biocarvão este pode conter maior ou menor quantidade de potássio
        veja a segui como diferentes toneladas de biocarvões carregam quantidades diferentes de potássio....
    """)

    # Botão para ver o gráfico de potássio
    if st.button("Veja o gráfico de Potássio nos Biocarvões"):
        st.session_state['page'] = 'grafico'  # Alterar o estado da página para 'grafico'

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

