import numpy as np

class NetworkEnv:
    def __init__(self, num_slices=3):
        self.num_slices = num_slices
        self.time_step = 0

    def step(self):
        self.time_step += 1
        # Simulate network dynamics optimized by RL
        base_throughput = 10 + np.log(self.time_step + 1)
        latency = max(1.0, 5 - np.log(self.time_step + 1) + np.random.normal(0, 0.2))

        return {
            "time": self.time_step,
            "throughput": np.random.normal(base_throughput, 0.5),
            "latency": latency,
            "packet_loss": max(0, np.random.normal(0.01, 0.002))
        }\n