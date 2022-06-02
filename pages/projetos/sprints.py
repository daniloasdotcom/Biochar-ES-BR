import streamlit as st
import matplotlib.pyplot as plt
import datetime


def sprints():
    today = st.date_input("Today is", datetime.datetime.now())

    st.text("Tempo para o final do projeto")
    st.progress(50)

    text01 = "<h1 style='text-align: center; line-height: 1.15'>Monitoramento do Progresso das Atividades da Sprint</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    time = ["02/06", "03/06", "04/06", "05/06", "06/06", "07/06", "08/06",
            "09/06", "10/06", "11/06", "12/06", "13/06", "14/06", "15/06"]
    progress_desired = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    real_progress = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

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
    - Coleta de folhas
    - Digestão foliar
    - Análises foliares
    - Medição das plantas
    - Masseração do solo para análise de COT e NT
    - Determinação da CC e PMP
    - Produção dos textos de PIIC
    - Avaliação dos dados da Duda
    
    # To do
    
    ### Day 02/06 - Quinta-feira
    - ~~Planejar as atividades da sprint~~
    - ~~Solicitar aos IC's que envie uma previsão de disponibilidade para as próximas duas semanas~~
    - ~~Atualizar as atividades e o gráfico~~
    
    ### Day 03/06 - Sexta-feira
    - Completar o plano da sprint
    - Organizar amostras para iniciar a determinações química na semana que vem
    - Organizar todos os dados (química e física)
    - Atualizar as atividades e o gráfico
    
    ### Day 04/06 - Sábado
    - Separar agregados para iniciar a análise por via úmida
    - Atualizar as atividades e o gráfico 
    
    ### Day 05/06 - Domingo
    - Descanso
    
    ### Day 06/06 - Segunda-feira
    - Agenda com o Carlos análise de Ca e Mg para 15/06
    - Determinação do pH do solo dos 3 anos
    - Cachimbagem e extração para análise de K, Na e P
    - Avaliar os cálculos realizados pelo Mateus
    - Atualizar as atividades e o gráfico
    
    ### Day 07/06 - Terça-feira
    - Determinação para análise de K, Na e P
    - Atualizar as atividades e o gráfico
    
    ### Day 08/06 - Quarta-feira
    - Cachimbagem e extração para análise de H+Al
    - Atualizar as atividades e o gráfico
    
    ### Day 09/06 - Quinta-feira
    - Determinação de H + Al
    - Atualizar as atividades e o gráfico
    
    ### Day 10/06 - Sexta-feira
    - Alocar as atividades da sprint
    - Atualizar as atividades e o gráfico
    
    ### Day 11/06 - Sábado
    - Descanso 
    - Atualizar as atividades e o gráfico
     
    ### Day 12/06 - Domingo
    - Descanso
    
    ### Day 13/06 - Segunda-feira
    - Cachimbagem e extração para análise de Ca e Mg
    - Alocar as atividades da sprint
    - Atualizar as atividades e o gráfico
    
    ### Day 14/06 - Terça-feira
    - Pipetagem de Ca e Mg
    - Determinação de Al
    - Alocar as atividades da sprint
    - Atualizar as atividades e o gráfico
    
    ### Day 15/06 - Quarta-feira
    - Determinação de Ca e Mg
    - Alocar as atividades da sprint
    - Atualizar as atividades e o gráfico
            
    """, unsafe_allow_html=True)


