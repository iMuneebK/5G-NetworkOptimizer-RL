class SpectrumManager:
    def __init__(self, total_bandwidth=100):
        self.total_bandwidth = total_bandwidth

    def allocate(self, demands):
        total_demand = sum(demands)
        if total_demand == 0:
            return [self.total_bandwidth / len(demands)] * len(demands)
        return [(d / total_demand) * self.total_bandwidth for d in demands]\n