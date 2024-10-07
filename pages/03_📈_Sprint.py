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
    st.sidebar.markdown('**General coordinator**: [Renato Ribeiro Passos](http://lattes.cnpq.br/3882320619443256)')
    st.sidebar.markdown('**Regional Researcher**: [Danilo Andrade](https://daniloas.com/)')

    st.sidebar.write("##")
    st.sidebar.write("##")

    st.date_input("Today is", datetime.datetime.now())

    text01 = "<h1 style='text-align: center; line-height: 1.15'>Monitoring the Progress of Sprint Activities</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    time = ["07/10", "08/10", "09/10", "10/10", "11/10",
            "14/10", "15/10", "16/10", "17/10", "18/10"]
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
        - Read the Edital
        - Set the task for each day        
        """)

    with col2.expander("Others"):
        st.markdown("""
        -         
        """)

    st.markdown("""
                # To do
    """)

    with st.expander("Day 14/08 - Segunda-feira"):
        st.markdown("""
        
        - 
            
        """)
    with st.expander("Day 15/08 - Terça-feira"):
        st.markdown("""    
        
        - 

        """)

    with st.expander("Day 16/08 - Quarta-feira"):
        st.markdown("""    

        - 

        """)

    with st.expander("Day 17/08 - Quinta-feira"):
        st.markdown("""    

        - 

        """)

    with st.expander("Day 18/08 - Sexta-feira"):
        st.markdown("""    

        - 

        """)

    with st.expander("Day 21/08 - Segunda-feira"):
        st.markdown("""    

        - 

        """)

    with st.expander("Day 22/08 - Terça-feira"):
        st.markdown("""    

        - 

        """)

    with st.expander("Day 23/08 - Quarta-feira"):
        st.markdown("""    

        - 

        """)

    with st.expander("Day 24/08 - Quinta-feira"):
        st.markdown("""    

        - 

        """)

    with st.expander("Day 25/08 - Sexta-feira"):
        st.markdown("""    

        - 

        """, unsafe_allow_html=True)

sprints()