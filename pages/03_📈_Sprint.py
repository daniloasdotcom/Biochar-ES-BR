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

    text01 = "<h1 style='text-align: center; line-height: 1.15'>Monitoring the Progress of Sprint Activities</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    time = ["12/09", "13/09", "14/09", "15/09", "16/09",
            "19/09", "20/09", "21/09", "22/09", "23/09"]
    progress_desired = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    real_progress =    [0, 0, 0, 0, 0, 0, 0, 0, 0,  0]

    fig02 = plt.figure(figsize=(10, 5))

    plt.plot(time, progress_desired, marker='o', label="Planned")
    plt.plot(time, real_progress, marker='o', label="Delivered")
    plt.title('Sprint Activity Progress Chart')
    plt.xlabel('Time')
    plt.ylabel('Progress')
    plt.grid(True)
    plt.legend(loc="upper left")
    plt.show()

    st.pyplot(fig02)

    st.markdown("""
        # Product backlog
        """)

    col1, col2 = st.columns([1, 1])

    with col1.expander("Priorities"):
        st.markdown("""
        # Priorities
        - Allocate sprint meetings
        - Testar o aparelho de Nitrogênio Total
        - Avaliar o extrator de Richards e a Mudança de posição dele
        - Bem como planejar as determinações de CC e PMP
        
        """)

    with col2.expander("Others"):
        st.markdown("""
        - Criar uma lista de eventos de divulgação dos nossos trabalhos
        
        """)

    st.markdown("""
                # To do
    """)

    with st.expander("Day 22/08 - Segunda-feira - Concluído"):
        st.markdown("""
        
        - ~Iniciar a separação do agregados~   
        - ~Alocar as atividades da Sprint~
        - ~Atualizar o trello~
        - ~Fazer anotações de desempenho dos IC's~
        - ~Atualizar as atividades e o gráfico~
            
        """)
    with st.expander("Day 23/08 - Terça-feira - Concluído"):
        st.markdown("""    
        
        - ~Continuar a separação do agregados (atrás da quadra)~
        - ~Alocar as atividades da Sprint~
        - ~Atualizar o trello~
        - ~Fazer anotações de desempenho dos IC's~
        - ~Atualizar as atividades e o gráfico~

        """)

    with st.expander("Day 24/08 - Quarta-feira - Concluído"):
        st.markdown("""    

        - ~Seminário da FAPES~
        - ~Atualizar as atividades e o gráfico~

        """)

    with st.expander("Day 25/08 - Quinta-feira"):
        st.markdown("""    

        - ~Seminário da FAPES~
        - ~Atualizar as atividades e o gráfico~

        """)

    with st.expander("Day 26/08 - Sexta-feira"):
        st.markdown("""    

        - Finalizar a separação de agregados
        - Preparo da Argila Dispersa em Água
        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 29/08 - Segunda-feira"):
        st.markdown("""    

        - Análise de Estabilidade de Agregados
        - Análise de Argila Dispersa em Água
        - Pesar materiais para Carbono Orgânico Total
        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 30/08 - Terça-feira"):
        st.markdown("""    

        - Análise de Estabilidade de Agregados
        - Análise de Argila Dispersa em Água
        - Determinação do Carbono Orgânico Total
        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 31/08 - Quarta-feira"):
        st.markdown("""    

        - Análise de Estabilidade de Agregados
        - Análise de Argila Dispersa em Água
        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 01/08 - Quinta-feira"):
        st.markdown("""    

        - Análise de Estabilidade de Agregados
        - Análise de Argila Dispersa em Água
        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """)

    with st.expander("Day 02/08 - Sexta-feira"):
        st.markdown("""    

        - Análise de Estabilidade de Agregados
        - Análise de Argila Dispersa em Água
        - Alocar as atividades da Sprint
        - Atualizar o trello
        - Fazer anotações de desempenho dos IC's
        - Atualizar as atividades e o gráfico

        """, unsafe_allow_html=True)

sprints()