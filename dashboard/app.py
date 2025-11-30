"""
Smart Energy Lader - Factory I/O Dashboard
Streamlit application for real-time energy monitoring and AI optimization
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import sys
import os

# Configure page
st.set_page_config(
    page_title="Smart Energy Lader Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

def create_factory_layout():
    """Create interactive factory layout visualization."""
    fig = go.Figure()
    
    # Add conveyors (14)
    conveyor_y_positions = [0, 0.5, 1, 1.5, 2, 2.5, 3]
    for i in range(14):
        y_pos = conveyor_y_positions[i % 7]
        x_start = (i // 7) * 5
        fig.add_trace(go.Scatter(
            x=[x_start, x_start + 4], y=[y_pos, y_pos],
            mode='lines+markers',
            name=f'Conveyor {i+1}',
            line=dict(color='blue', width=6),
            marker=dict(size=8)
        ))
    
    # Add pushers (4)
    pusher_positions = [(2, 3.5), (7, 3.5), (2, 4.5), (7, 4.5)]
    for i, pos in enumerate(pusher_positions):
        fig.add_trace(go.Scatter(
            x=[pos[0]], y=[pos[1]],
            mode='markers+text',
            name=f'Pusher {i+1}',
            marker=dict(size=20, color='orange', symbol='square'),
            text=f'P{i+1}',
            textposition='top center'
        ))
    
    # Add robots (3)
    robot_positions = [(1.5, 5.5), (4.5, 5.5), (7.5, 5.5)]
    for i, pos in enumerate(robot_positions):
        fig.add_trace(go.Scatter(
            x=[pos[0]], y=[pos[1]],
            mode='markers+text',
            name=f'Robot {i+1}',
            marker=dict(size=25, color='green', symbol='diamond'),
            text=f'R{i+1}',
            textposition='top center'
        ))
    
    fig.update_layout(
        title='Factory I/O Layout - Component Distribution',
        xaxis_title='X Position',
        yaxis_title='Y Position',
        height=600,
        hovermode='closest',
        showlegend=True
    )
    
    return fig

def generate_mock_data(duration_minutes=60):
    """Generate mock real-time data for demonstration."""
    timestamps = pd.date_range(
        start=datetime.now() - timedelta(minutes=duration_minutes),
        end=datetime.now(),
        freq='10s'
    )
    
    data = {
        'timestamp': timestamps,
        'power': np.random.normal(45, 8, len(timestamps)),
        'efficiency': np.random.normal(0.85, 0.05, len(timestamps)),
        'throughput': np.random.normal(800, 100, len(timestamps)),
        'ai_confidence': np.random.normal(0.92, 0.05, len(timestamps))
    }
    
    df = pd.DataFrame(data)
    df['power'] = df['power'].clip(20, 80)
    df['efficiency'] = df['efficiency'].clip(0.7, 1.0)
    df['throughput'] = df['throughput'].clip(500, 1000)
    df['ai_confidence'] = df['ai_confidence'].clip(0.75, 1.0)
    
    return df

def create_power_timeline(df):
    """Create power consumption timeline visualization."""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df['timestamp'],
        y=df['power'],
        mode='lines',
        name='Power Consumption',
        fill='tozeroy',
        line=dict(color='#FF6B6B', width=3)
    ))
    
    fig.update_layout(
        title='Power Consumption Timeline',
        xaxis_title='Time',
        yaxis_title='Power (kW)',
        hovermode='x unified',
        height=400
    )
    
    return fig

def create_efficiency_chart(df):
    """Create efficiency visualization."""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df['timestamp'],
        y=df['efficiency'] * 100,
        mode='lines+markers',
        name='System Efficiency',
        line=dict(color='#4ECDC4', width=2),
        marker=dict(size=4)
    ))
    
    fig.update_layout(
        title='System Efficiency Over Time',
        xaxis_title='Time',
        yaxis_title='Efficiency (%)',
        yaxis=dict(range=[70, 100]),
        hovermode='x unified',
        height=300
    )
    
    return fig

def main():
    """Main dashboard application."""
    
    # Header
    st.markdown("# ⚡ Smart Energy Lader - Factory I/O Dashboard")
    st.markdown("AI-powered energy optimization for industrial automation")
    
    # Key metrics
    st.markdown("## 📊 Real-Time Metrics")
    
    # Generate mock data
    df = generate_mock_data(duration_minutes=60)
    latest = df.iloc[-1]
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Current Power",
            f"{latest['power']:.1f} kW",
            f"-{np.random.randint(5, 15)}%",
            delta_color="inverse"
        )
    
    with col2:
        st.metric(
            "Energy Saved",
            f"₹{np.random.randint(1000, 5000):,}",
            f"+{np.random.randint(10, 25)}%"
        )
    
    with col3:
        st.metric(
            "AI Confidence",
            f"{latest['ai_confidence']*100:.0f}%",
            f"+{np.random.randint(1, 8)}%"
        )
    
    with col4:
        st.metric(
            "System Efficiency",
            f"{latest['efficiency']*100:.1f}%",
            f"-{np.random.randint(1, 5)}%",
            delta_color="inverse"
        )
    
    # Factory layout
    st.markdown("## 🏭 Factory Layout")
    factory_fig = create_factory_layout()
    st.plotly_chart(factory_fig, use_container_width=True)
    
    # Time series data
    st.markdown("## 📈 Performance Trends")
    
    col1, col2 = st.columns(2)
    
    with col1:
        power_fig = create_power_timeline(df)
        st.plotly_chart(power_fig, use_container_width=True)
    
    with col2:
        efficiency_fig = create_efficiency_chart(df)
        st.plotly_chart(efficiency_fig, use_container_width=True)
    
    # AI Control Panel
    st.markdown("## 🤖 AI Control Panel")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("AI Configuration")
        ai_enabled = st.toggle("Enable AI Optimization", value=True)
        power_limit = st.slider("Power Limit (kW)", 20, 100, 60, step=5)
        optimization_mode = st.selectbox(
            "Optimization Strategy",
            ["Energy Minimization", "Throughput Maximization", "Balanced", "Custom"]
        )
    
    with col2:
        st.subheader("Manual Override")
        if st.button("Override AI Decision"):
            st.success("Manual override activated!")
        
        if st.button("Emergency Stop"):
            st.error("Emergency stop triggered!")
        
        if st.button("Reset AI Model"):
            st.info("AI model reset to initial state")
    
    # Detailed statistics
    st.markdown("## 📋 Detailed Statistics")
    
    stats_col1, stats_col2, stats_col3 = st.columns(3)
    
    with stats_col1:
        st.subheader("Power Statistics")
        st.write(f"**Mean:** {df['power'].mean():.2f} kW")
        st.write(f"**Min:** {df['power'].min():.2f} kW")
        st.write(f"**Max:** {df['power'].max():.2f} kW")
        st.write(f"**Std Dev:** {df['power'].std():.2f} kW")
    
    with stats_col2:
        st.subheader("Efficiency Statistics")
        st.write(f"**Mean:** {df['efficiency'].mean()*100:.1f}%")
        st.write(f"**Min:** {df['efficiency'].min()*100:.1f}%")
        st.write(f"**Max:** {df['efficiency'].max()*100:.1f}%")
    
    with stats_col3:
        st.subheader("Throughput Statistics")
        st.write(f"**Mean:** {df['throughput'].mean():.0f} units/hr")
        st.write(f"**Total:** {df['throughput'].sum():.0f} units")
    
    # Machine component breakdown
    st.markdown("## ⚙️ Machine Component Status")
    
    components = {
        'Conveyors': {'count': 14, 'status': 'operational', 'power': 14, 'efficiency': 0.92},
        'Pushers': {'count': 4, 'status': 'operational', 'power': 4, 'efficiency': 0.88},
        'Robots': {'count': 3, 'status': 'operational', 'power': 12, 'efficiency': 0.90}
    }
    
    component_data = []
    for name, info in components.items():
        component_data.append({
            'Component': name,
            'Count': info['count'],
            'Status': info['status'],
            'Power (kW)': info['power'],
            'Efficiency': f"{info['efficiency']*100:.0f}%"
        })
    
    st.dataframe(pd.DataFrame(component_data), use_container_width=True)
    
    # Export functionality
    st.markdown("## 💾 Data Export")
    
    if st.button("Export Current Data as CSV"):
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name=f"factory_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
    
    # Footer
    st.markdown("---")
    st.markdown("""
    **Smart Energy Lader** | AI-Powered Factory Optimization
    
    Developed for intelligent energy management in Factory I/O environments
    """)

if __name__ == "__main__":
    main()
