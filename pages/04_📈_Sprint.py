import streamlit as st
import matplotlib.pyplot as plt
import datetime
from pages.others.load_css import local_css
from pages.others.sidebar_utils import configure_sidebar

# Usando nosso recursos css
local_css("pages/others/style.css")


def sprints():
    configure_sidebar()  # Chama a função para configurar a barra lateral

    st.date_input("Today is", datetime.datetime.now())

    # Adding message about new project for funding
    st.markdown(
        "<p style='text-align: center; font-size: 1.2em; color: #FF6347;'><strong>We are currently preparing a new project for funding. Stay tuned for updates!</strong></p>",
        unsafe_allow_html=True)

    text01 = "<h1 style='text-align: center; line-height: 1.15'>Monitoring the Progress of Sprint Activities</h1> "

    st.markdown(text01, unsafe_allow_html=True)

    time = ["11/11", "12/11", "13/11", "14/11", "15/11",
            "18/11", "19/11", "20/11", "21/11", "22/11"]
    progress_desired = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    real_progress = [1, 2, 0, 0, 0, 0, 0, 0, 0, 0]

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
        - ~Read the Edital~
        - ~Set the task for each day~        
        """)

    with col2.expander("Others"):
        st.markdown("""
        -         
        """)

    st.markdown("""
                # To do
    """)

    with st.expander("Day 11/11 - Monday"):
        st.markdown("""

        - ~Day off~

        """)
    with st.expander("Day 12/10 - Tuesday"):
        st.markdown("""    

        - To complete the text of project

        """)

    with st.expander("Day 13/10 - Wednesday"):
        st.markdown("""    

        - ~Meeting with Renato discussion about the project

        """)

    with st.expander("Day 14/10 - Thursday"):
        st.markdown("""    

        - ~Insertion of the first informations for the project in SIGFAPES

        """)

    with st.expander("Day 15/11 - Friday"):
        st.markdown("""    

        - 

        """)

    with st.expander("Day 18/11 - Monday"):
        st.markdown("""    

        - Day Off

        """)

    with st.expander("Day 19/11 - Tuesday"):
        st.markdown("""    

        - Day Off

        """)

    with st.expander("Day 20/11 - Wednesday"):
        st.markdown("""    

        - 

        """)

    with st.expander("Day 21/11 - Thursday"):
        st.markdown("""    

        - 

        """)

    with st.expander("Day 22/11 - Friday"):
        st.markdown("""    

        - 

        """, unsafe_allow_html=True)


sprints()
