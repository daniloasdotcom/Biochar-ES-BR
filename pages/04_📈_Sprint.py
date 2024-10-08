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

    time = ["07/10", "08/10", "09/10", "10/10", "11/10",
            "14/10", "15/10", "16/10", "17/10", "18/10"]
    progress_desired = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    real_progress = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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

    with st.expander("Day 07/10 - Monday"):
        st.markdown("""

        - ~Day for reviewing the details of the FAPES Call for Proposals~

        """)
    with st.expander("Day 08/10 - Tuesday"):
        st.markdown("""    

        - 

        """)

    with st.expander("Day 09/10 - Wednesday"):
        st.markdown("""    

        - 

        """)

    with st.expander("Day 10/10 - Thursday"):
        st.markdown("""    

        - 

        """)

    with st.expander("Day 11/10 - Friday"):
        st.markdown("""    

        - 

        """)

    with st.expander("Day 14/10 - Monday"):
        st.markdown("""    

        - Day Off

        """)

    with st.expander("Day 15/10 - Tuesday"):
        st.markdown("""    

        - Day Off

        """)

    with st.expander("Day 16/10 - Wednesday"):
        st.markdown("""    

        - 

        """)

    with st.expander("Day 17/10 - Thursday"):
        st.markdown("""    

        - 

        """)

    with st.expander("Day 18/10 - Friday"):
        st.markdown("""    

        - 

        """, unsafe_allow_html=True)


sprints()
