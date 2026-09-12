import torch
import torch.nn as nn

class DqnNetwork(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(DqnNetwork, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, output_dim)
        )

    def forward(self, x):
        return self.fc(x)

class DQNAgent:
    def __init__(self, state_dim, action_dim):
        self.model = DqnNetwork(state_dim, action_dim)
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=0.001)

    def select_action(self, state):
        with torch.no_grad():
            q_values = self.model(torch.tensor(state, dtype=torch.float32))
        return torch.argmax(q_values).item()\n