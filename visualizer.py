import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_network_metrics(df):
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True,
                        subplot_titles=("Throughput (Gbps)", "Latency (ms)", "Packet Loss (%)"))

    fig.add_trace(go.Scatter(x=df['time'], y=df['throughput'], line=dict(color='blue')), row=1, col=1)
    fig.add_trace(go.Scatter(x=df['time'], y=df['latency'], line=dict(color='red')), row=2, col=1)
    fig.add_trace(go.Scatter(x=df['time'], y=df['packet_loss'], line=dict(color='green')), row=3, col=1)

    fig.update_layout(height=600, showlegend=False, template="plotly_white")
    return fig\n