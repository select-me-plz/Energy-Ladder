"""
Reusable layout components for the Streamlit dashboard.
"""

import streamlit as st


def create_header(title, subtitle=""):
    """
    Create a formatted header section.
    
    Args:
        title (str): Main title
        subtitle (str): Optional subtitle
    """
    st.markdown(f"# {title}")
    if subtitle:
        st.markdown(f"*{subtitle}*")


def create_section(title):
    """
    Create a formatted section header.
    
    Args:
        title (str): Section title
    """
    st.markdown(f"## {title}")


def create_sidebar_menu():
    """
    Create a sidebar menu for navigation.
    
    Returns:
        str: Selected menu item
    """
    with st.sidebar:
        st.title("Navigation")
        menu = st.radio(
            "Select Page",
            ["Dashboard", "Analytics", "Settings", "About"]
        )
    return menu


def create_info_box(title, content):
    """
    Create an information box.
    
    Args:
        title (str): Box title
        content (str): Box content
    """
    st.info(f"**{title}**\n\n{content}")
