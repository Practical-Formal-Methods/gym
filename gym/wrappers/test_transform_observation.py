import pytest

import numpy as np

import mygym
from mygym.wrappers import TransformObservation


@pytest.mark.parametrize('env_id', ['CartPole-v1', 'Pendulum-v0'])
def test_transform_observation(env_id):
    affine_transform = lambda x: 3*x + 2
    env = mygym.make(env_id)
    wrapped_env = TransformObservation(mygym.make(env_id), lambda obs: affine_transform(obs))

    env.seed(0)
    wrapped_env.seed(0)

    obs = env.reset()
    wrapped_obs = wrapped_env.reset()
    assert np.allclose(wrapped_obs, affine_transform(obs))

    action = env.action_space.sample()
    obs, reward, done, _ = env.step(action)
    wrapped_obs, wrapped_reward, wrapped_done, _ = wrapped_env.step(action)
    assert np.allclose(wrapped_obs, affine_transform(obs))
    assert np.allclose(wrapped_reward, reward)
    assert wrapped_done == done
