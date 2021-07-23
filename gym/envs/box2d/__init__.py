try:
    import Box2D
    from mygym.gym.envs.box2d.lunar_lander import LunarLander
    from mygym.gym.envs.box2d.lunar_lander import LunarLanderContinuous
    from mygym.gym.envs.box2d.bipedal_walker import BipedalWalker, BipedalWalkerHardcore
    from mygym.gym.envs.box2d.car_racing import CarRacing
except ImportError:
    Box2D = None
