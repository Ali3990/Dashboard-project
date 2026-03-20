import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import os

def create_jolts_unemp_chart():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, 'job_report_dash','jolts_unemp','data', 'jolts_ue_data.xlsx')

    df = pd.read_excel(file_path, header=None)
    df = df.drop(index=list(range(0, 6))).reset_index(drop=True)
    df.rename(columns={0: 'Date', 1: 'Job Openings', 2: 'Unemployment Rate'}, inplace=True)

    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Job Openings'] = pd.to_numeric(df['Job Openings'], errors='coerce')
    df['Unemployment Rate'] = pd.to_numeric(df['Unemployment Rate'], errors='coerce')

    df['Job Openings'] /= 1000
    df['Unemployment Rate'] /= 100
    # print(df.head(10))


    # Build line and column combo chart 
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x = df['Date'],
            y = df['Job Openings'],
            name = 'Job Openings (Millions)',
            yaxis= 'y1'
        )
    )

    fig.add_trace(
        go.Scatter(
            x = df['Date'],
            y = df['Unemployment Rate'],
            name = 'Unemployment Rate (%)',
            mode = 'lines',
            yaxis = 'y2',
            line = dict(width=3)
        )
    )

    fig.update_layout(
        title = dict(
            text = 'Job Openings & Unemployment Rate',
            x = 0.5,
            xanchor = 'center',
            font = dict(size=16)
        ),
        yaxis = dict(
            title = 'Job Openings (Millions)',
            side = 'left',
            tickformat = '.1f',
            showgrid = False
        ),
        yaxis2 = dict(
            title = 'Unemployment Rate (%)',
            overlaying = 'y',
            side = 'right',
            tickformat = '.1%',
            showgrid = False
        ),
        barmode = 'group',
        legend = dict(x=0.3, y=0.95),
        template = 'plotly_white' 
    )

    return fig

