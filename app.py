#!/usr/bin/env python3
"""
ALPHA SPIKE TRADING - LOCAL VERSION
==================================
Simplified version for local testing
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.graph_objects as go

st.set_page_config(
    page_title="Alpha Spike Trading",
    page_icon="🚀",
    layout="wide"
)

def main():
    st.title("🚀 Alpha Spike Trading Platform")
    st.markdown("**Local Development Version**")
    
    # Sidebar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select Page", ["Dashboard", "Trading", "Analytics"])
    
    if page == "Dashboard":
        st.header("📊 Trading Dashboard")
        
        # Sample metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Portfolio Value", "$204,273", "+$1,234")
        with col2:
            st.metric("Daily P&L", "+$567", "2.3%")
        with col3:
            st.metric("Active Positions", "3", "+1")
        with col4:
            st.metric("Win Rate", "75%", "+5%")
        
        # Sample chart
        dates = pd.date_range(start='2025-09-01', end='2025-09-15', freq='D')
        values = np.random.randn(len(dates)).cumsum() + 100
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=values, mode='lines', name='Portfolio'))
        fig.update_layout(title="Portfolio Performance", height=400)
        st.plotly_chart(fig, use_container_width=True)
        
    elif page == "Trading":
        st.header("💹 Trading Interface")
        st.info("Trading interface - Connect to your APIs")
        
        # API Configuration
        with st.expander("API Configuration"):
            kraken_key = st.text_input("Kraken API Key", type="password")
            kraken_secret = st.text_input("Kraken Secret", type="password")
            
            if st.button("Test Connection"):
                if kraken_key and kraken_secret:
                    st.success("✅ API keys configured (test connection needed)")
                else:
                    st.error("❌ Please enter API keys")
    
    elif page == "Analytics":
        st.header("📈 Analytics")
        st.info("Analytics dashboard - Connect data sources")
        
        # Sample analysis
        st.subheader("Market Analysis")
        symbols = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'ADA-USD']
        
        for symbol in symbols:
            with st.expander(f"{symbol} Analysis"):
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(f"{symbol} Price", f"${np.random.randint(1000, 50000)}")
                with col2:
                    st.metric("24h Change", f"{np.random.uniform(-5, 5):.2f}%")

if __name__ == "__main__":
    main()

