"""
Reusable metrics components for the Streamlit dashboard.
"""

import streamlit as st
import pandas as pd


def metric_card(title, value, delta=None, delta_color="normal"):
    """
    Display a metric card with title, value, and optional delta.
    
    Args:
        title (str): Title of the metric
        value (str): Main value to display
        delta (str, optional): Change indicator
        delta_color (str): "normal" or "inverse"
    """
    st.metric(title, value, delta, delta_color=delta_color)


def status_indicator(status):
    """
    Display a status indicator (operational, warning, error).
    
    Args:
        status (str): "operational", "warning", or "error"
    """
    color_map = {
        "operational": "🟢",
        "warning": "🟡",
        "error": "🔴"
    }
    return f"{color_map.get(status, '❓')} {status.upper()}"


def progress_bar(value, max_value=100, label=""):
    """
    Display a progress bar with label.
    
    Args:
        value (float): Current value
        max_value (float): Maximum value
        label (str): Label for the progress bar
    """
    percentage = (value / max_value) * 100
    st.write(f"{label}: {percentage:.1f}%")
    st.progress(percentage / 100)
