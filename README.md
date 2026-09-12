# 📡 AI-Powered 5G Network Optimizer

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-RL-red.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B.svg)

An intelligent system for dynamically optimizing 5G network resource allocation using Deep Reinforcement Learning (DQN) and time-series forecasting (LSTM).

## 🌟 Features
- **Reinforcement Learning (DQN)**: Optimizes 5G network resource allocation and dynamic spectrum management.
- **Traffic Forecasting**: Predicts network congestion using LSTM time-series forecasting.
- **Network Slicing**: Demonstrates intelligent slicing for eMBB, URLLC, and mMTC.
- **Real-Time Dashboard**: Streamlit interface showing network KPIs (throughput, latency, packet loss).

## 🏗️ Architecture
- **5G NR Environment Simulator**: Mocks realistic network behavior, massive MIMO, and beamforming effects.
- **DQN Agent**: Learns optimal bandwidth allocation policies.
- **LSTM Predictor**: Forecasts upcoming traffic surges.

## 🚀 Usage
```bash
pip install -r requirements.txt
streamlit run app.py
```\n