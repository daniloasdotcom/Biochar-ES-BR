import streamlit as st

my_variable = "From Mai App.py page"

def main():
    st.title("Streamlit Multipages")
    st.subheader("Main page")
    st.write(my_variable)

if __name__ == '__main__':
    main()