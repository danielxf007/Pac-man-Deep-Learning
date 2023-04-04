import retro

class Environment:
    """
    Class that is used as a wrapper for retro gym and
    to save the state which could be reference this class to get
    """
    def __init__(self, game_name):
        self.gym_env = retro.make(game=game_name)
        self.screen = self.gym_env.reset()
        self.reward = None
        self.done = False
        self.info = None
        self.ram = self.gym_env.get_ram()
    
    def enterInput(self, control_input):
        self.screen, self.reward, self.done, self.info = self.gym_env.step(control_input)
        
    def getScreen(self):
        return self.screen
    
    def getReward(self):
        return self.reward
    
    def isDone(self):
        return self.done
    
    def getInfo(self):
        return self.info
    
    def getRam(self):
        return self.ram
    
    def reset(self):
        self.screen = self.gym_env.reset()
        self.ram = self.gym_env.get_ram()
        
    def close(self):
        self.gym_env.close()
