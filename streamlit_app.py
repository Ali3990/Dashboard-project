import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import os
from job_report_dash.jolts_chart.jolts_unemp import create_jolts_unemp_chart

st.set_page_config(layout="wide")

fig = create_jolts_unemp_chart()
st.plotly_chart(fig, use_container_width=True)
