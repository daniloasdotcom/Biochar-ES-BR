import streamlit as st
import pandas as pd
import plotly.graph_objects as go


def atributos():
    st.title("Caracterização dos biocarvões")
    st.markdown("Os gráficos abaixo ajudam a visualizar as atributos dos biocarvões")

    col1, col2 = st.columns([1, 1])

    chart_visual = col1.selectbox('Select Charts/Plot type',
                                        ('Bar Chart', 'Bubble Chart'))

    selected_status = col2.selectbox('Select o atributo desejado',
                                           options=['pH',
                                                    'Cálcio',
                                                    'Magnésio',
                                                    'Fósforo'])

    data = pd.read_csv("dados.csv")
    fig = go.Figure()

    if chart_visual == 'Bar Chart':
        if selected_status == 'pH':
            fig.add_trace(go.Bar(x=data.biocar,
                                 y=data.pH))
            fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
            fig.update_yaxes(showline=True, linewidth=2, linecolor='black', ticks="outside", tickwidth=2)
            fig.update_layout(xaxis_title="Biocarvões", yaxis_title="pH")

        if selected_status == 'Cálcio':
            fig.add_trace(go.Bar(x=data.biocar,
                                 y=data.Ca))
            fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
            fig.update_yaxes(showline=True, linewidth=2, linecolor='black', ticks="outside", tickwidth=2)
            fig.update_layout(xaxis_title="Biocarvões", yaxis_title="Cálcio (dag/kg)")

        if selected_status == 'Magnésio':
            fig.add_trace(go.Bar(x=data.biocar,
                                 y=data.Mg))
            fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
            fig.update_yaxes(showline=True, linewidth=2, linecolor='black', ticks="outside", tickwidth=2)
            fig.update_layout(xaxis_title="Biocarvões", yaxis_title="Magnésio (dag/kg)")

        if selected_status == 'Fósforo':
            fig.add_trace(go.Bar(x=data.biocar,
                                 y=data.P))
            fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
            fig.update_yaxes(showline=True, linewidth=2, linecolor='black', ticks="outside", tickwidth=2)
            fig.update_layout(xaxis_title="Biocarvões", yaxis_title="Fósforo (dag/kg)")

    elif chart_visual == 'Bubble Chart':
        if selected_status == 'pH':
            fig.add_trace(go.Scatter(x=data.biocar,
                                     y=data.pH,
                                     mode='markers',
                                     marker_size=[40, 60, 80, 60, 40, 50]))
            fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
            fig.update_yaxes(showline=True, linewidth=2, linecolor='black', ticks="outside", tickwidth=2)
            fig.update_layout(xaxis_title="Biocarvões", yaxis_title="pH")

        if selected_status == 'Cálcio':
            fig.add_trace(go.Scatter(x=data.biocar,
                                     y=data.Ca,
                                     mode='markers',
                                     marker_size=[40, 60, 80, 60, 40, 50]))
            fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
            fig.update_yaxes(showline=True, linewidth=2, linecolor='black', ticks="outside", tickwidth=2)
            fig.update_layout(xaxis_title="Biocarvões", yaxis_title="Cálcio (dag/kg)")

        if selected_status == 'Magnésio':
            fig.add_trace(go.Scatter(x=data.biocar,
                                     y=data.Mg,
                                     mode='markers',
                                     marker_size=[40, 60, 80, 60, 40, 50]))
            fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
            fig.update_yaxes(showline=True, linewidth=2, linecolor='black', ticks="outside", tickwidth=2)
            fig.update_layout(xaxis_title="Biocarvões", yaxis_title="Magnésio (dag/kg)")

        if selected_status == 'Fósforo':
            fig.add_trace(go.Scatter(x=data.biocar,
                                     y=data.P,
                                     mode='markers',
                                     marker_size=[40, 60, 80, 60, 40, 50]))
            fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
            fig.update_yaxes(showline=True, linewidth=2, linecolor='black', ticks="outside", tickwidth=2)
            fig.update_layout(xaxis_title="Biocarvões", yaxis_title="Fósforo (dag/kg)")

    st.plotly_chart(fig, use_container_width=True)