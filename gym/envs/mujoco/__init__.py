from mygym.envs.mujoco.mujoco_env import MujocoEnv
# ^^^^^ so that user gets the correct error
# message if mujoco is not installed correctly
from mygym.envs.mujoco.ant import AntEnv
from mygym.envs.mujoco.half_cheetah import HalfCheetahEnv
from mygym.envs.mujoco.hopper import HopperEnv
from mygym.envs.mujoco.walker2d import Walker2dEnv
from mygym.envs.mujoco.humanoid import HumanoidEnv
from mygym.envs.mujoco.inverted_pendulum import InvertedPendulumEnv
from mygym.envs.mujoco.inverted_double_pendulum import InvertedDoublePendulumEnv
from mygym.envs.mujoco.reacher import ReacherEnv
from mygym.envs.mujoco.swimmer import SwimmerEnv
from mygym.envs.mujoco.humanoidstandup import HumanoidStandupEnv
from mygym.envs.mujoco.pusher import PusherEnv
from mygym.envs.mujoco.thrower import ThrowerEnv
from mygym.envs.mujoco.striker import StrikerEnv
