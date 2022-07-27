import streamlit as st
import matplotlib.pyplot as plt
import datetime
from pages.others.load_css import local_css

# Usando nosso recursos css
local_css("pages/others/style.css")

def sprints():
    st.sidebar.image("images/projectLogo.png", use_column_width=True)

    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('**Coordinator**: [Danilo Andrade](https://daniloas.com/)')
    st.sidebar.markdown('**Supervisor**: [Renato Ribeiro Passos](http://lattes.cnpq.br/3882320619443256)')

    st.sidebar.markdown('**----- Volunteer team -----**')

    st.sidebar.markdown('**Technical support**: [Amanda Gomes](https://www.linkedin.com/in/amanda-g-3449349b/)')
    st.sidebar.markdown('**Junior Researcher**: [Mateus Hastenreiter](http://lattes.cnpq.br/4351826031776108)')
    st.sidebar.markdown('**Junior Researcher**: [Maria Eduarda](http://lattes.cnpq.br/1801516731947159)')
    st.sidebar.markdown('**Junior Researcher**: [Aurélio Martins](http://lattes.cnpq.br/2155060458456586)')
    st.sidebar.markdown('**Junior Researcher**: Ueslei Machado')

    st.sidebar.write("##")
    st.sidebar.write("##")

    st.date_input("Today is", datetime.datetime.now())

    text01 = "<h1 style='text-align: center; line-height: 1.15'>Monitoramento do Progresso das Atividades da " \
             "Sprint</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    time = ["01/08", "02/08", "03/08", "04/08", "05/08",
            "08/08", "09/08", "10/08", "11/08", "12/08"]
    progress_desired = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    real_progress =    [0, 0, 0, 0, 0, 0, 0, 0, 0,  0]

    fig02 = plt.figure(figsize=(10, 5))

    plt.plot(time, progress_desired, marker='o', label="Planejado")
    plt.plot(time, real_progress, marker='o', label="Entregue")
    plt.title('Gráfico de Progresso das Atividades da Sprint')
    plt.xlabel('Tempo')
    plt.ylabel('Progresso')
    plt.grid(True)
    plt.legend(loc="upper left")
    plt.show()

    st.pyplot(fig02)

    st.markdown("""
        # Product backlog
        """)

    col1, col2 = st.columns([1, 1])

    with col1.expander("Prioridades"):
        st.markdown("""
        # Prioridades
        - Alocar as reuniões da sprint
        - Realizar o treinamento em agregados e ADA
        - Avaliar e organizar os dados da Duda e do Mateus
        - Solicitar a agenda deles para o período entre 18 e 29 de julho
        
        """)

    with col2.expander("Demais"):
        st.markdown("""
        - Criar uma lista de eventos de divulgação dos nossos trabalhos
        
        """)

    st.markdown("""
                # To do
    """)

    with st.expander("Day 01/08 - Segunda-feira - Em Progresso"):
        st.markdown("""
        
        - Agendar para sábado a medição das plantas na área experimental
        - ~~Solicitar o podão à professsora e agendar para sabádo a coletar foliar~~
        - Agendar para sexta-feria o uso da estufa para secagem do material
        - Agendar para domingo/segunda-feira que vem a digestão
        - Verificar solução nitroperclórica
        - ~~Iniciar a masseração do solo do 4º ano (NT e COT)~~
        
        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico
            
        """)
    with st.expander("Day 02/08 - Terça-feira"):
        st.markdown("""    

        - Testar o aparelho de Nitrogênio Total
        - Avaliar o extrator de Richards e a Mudança de posição dele
        - Bem como planejar as determinações de CC e PMP
        - Iniciar a separação do agregados (atrás da quadra)
        
        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 03/08 - Quarta-feira"):
        st.markdown("""    

        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 04/08 - Quinta-feira"):
        st.markdown("""    

        - Planejar a digestão foliar e as determinações para o Aurélio
        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 05/08 - Sexta-feira"):
        st.markdown("""    

        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 08/08 - Segunda-feira"):
        st.markdown("""    

        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 09/08 - Terça-feira"):
        st.markdown("""    

        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 10/08 - Quarta-feira"):
        st.markdown("""    

        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 11/08 - Quinta-feira"):
        st.markdown("""    

        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 12/08 - Sexta-feira"):
        st.markdown("""    

        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """, unsafe_allow_html=True)

sprints()