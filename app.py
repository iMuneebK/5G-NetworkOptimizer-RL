import streamlit as st
import pandas as pd
import time
from network_env import NetworkEnv
from visualizer import plot_network_metrics

st.set_page_config(page_title="5G Network Optimizer", layout="wide")
st.title("📡 AI-Powered 5G Network Optimization System")
st.markdown("Monitor and optimize 5G network resource allocation in real-time using Deep Reinforcement Learning.")

env = NetworkEnv()

col1, col2, col3 = st.columns(3)
m_throughput = col1.empty()
m_latency = col2.empty()
m_loss = col3.empty()

chart_placeholder = st.empty()

if st.button("Start Optimization Simulation"):
    history = []
    for i in range(100):
        state = env.step()
        history.append(state)
        df = pd.DataFrame(history)

        m_throughput.metric("Throughput", f"{state['throughput']:.2f} Gbps", f"{state['throughput'] - 10:.2f} Gbps")
        m_latency.metric("Latency", f"{state['latency']:.1f} ms", f"{5 - state['latency']:.1f} ms")
        m_loss.metric("Packet Loss", f"{state['packet_loss']:.3f} %", f"-0.001 %")

        chart_placeholder.plotly_chart(plot_network_metrics(df), use_container_width=True)
        time.sleep(0.5)\n