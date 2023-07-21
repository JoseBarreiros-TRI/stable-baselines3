import os

def not_loaded(name):
    raise ImportError(f"{name} not in Drake's internal stable_baselines3")

def make_not_loaded(name):
    return lambda *args, **kwargs: not_loaded(name)

A2C = make_not_loaded("A2C")
get_system_info = make_not_loaded("get_system_info")
DDPG = make_not_loaded("DDPG")
DQN = make_not_loaded("DQN")
HerReplayBuffer = make_not_loaded("HerReplayBuffer")
PPO = make_not_loaded("PPO")
SAC = make_not_loaded("SAC")
TD3 = make_not_loaded("TD3")

# Read version from file
version_file = os.path.join(os.path.dirname(__file__), "version.txt")
with open(version_file) as file_handler:
    __version__ = file_handler.read().strip()


def HER(*args, **kwargs):
    raise ImportError(
        "Since Stable Baselines 2.1.0, `HER` is now a replay buffer class `HerReplayBuffer`.\n "
        "Please check the documentation for more information: https://stable-baselines3.readthedocs.io/"
    )


__all__ = [
    "A2C",
    "DDPG",
    "DQN",
    "PPO",
    "SAC",
    "TD3",
    "HerReplayBuffer",
    "get_system_info",
]
