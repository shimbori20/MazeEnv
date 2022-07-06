import gym
import numpy as np
class Maze(gym.Env):
    def __init__(self):
        self.action_space = gym.spaces.Discrete(4) 
        self.X = 10
        self.Y = 10
        self.V_X = 10
        self.V_Y = 10
        self.MAX_STEP = 100
        self.pos = [0,0]
        self.mode = 0
        self.actions = [[0,1],[1,0],[-1,0],[0,-1]]
        LOW= np.zeros((4,self.V_X,self.V_Y))
        HIGH= np.ones((4,self.V_X,self.V_Y))
        self.observation_space = gym.spaces.Box(low=LOW, high=HIGH)
        self.reset()

    def step(self, action):
        add = self.actions[action]
        self.count += 1
        self.add_visited(self.pos)
        if (not self.on_board(self.pos[0] + add[0],self.pos[1] + add[1]) )or self.on_wall(self.pos[0] + add[0],self.pos[1] + add[1]):
            if self.count > self.MAX_STEP:
                return self.get_arr(self.pos), 0 , True, {}
            return self.get_arr(self.pos), -1, False, {}
        self.pos = [self.pos[0] + add[0],self.pos[1] + add[1]]
        if self.on_goal(self.pos[0],self.pos[1]):
            return self.get_arr(self.pos), 100 , True, {}
        if self.count > self.MAX_STEP:
            return self.get_arr(self.pos), 0 , True, {}

        if self.on_minus(self.pos[0],self.pos[1]):
            return self.get_arr(self.pos), -0.1, False, {}
        if not self.is_visited(self.pos[0],self.pos[1]):
            return self.get_arr(self.pos), 1, False, {}

        return self.get_arr(self.pos), 0, False, {}

    def render(self):
        if self.count == 1:
            state1 = np.zeros((self.V_X,self.V_Y)).tolist()
            for i in range(self.X):
                for j in range(self.Y):
                    if not self.on_board(i,j):
                        state1[i][j] = 'w'
                    elif self.on_wall(i,j):
                        state1[i][j] = 'w'
                    elif self.on_goal(i,j):
                        state1[i][j] = 'g'
                    elif self.on_minus(i,j):
                        state1[i][j] = 'm'
                    elif self.is_visited(i,j):
                        state1[i][j] = '+'
                    else:
                        state1[i][j] = '-'
                print(state1[i])
        print(self.pos)
    def is_visited(self,x,y):
        for i in self.visited:
            if i[0] == x and i[1] == y:
                return True
        return False
    def add_visited(self,pos):
        self.visited += [pos]
    def reset(self):
        self.visited = []
        self.count = 0
        self.pos = [0,0]
        self.mode = np.random.randint(0, 2)
        return  self.get_arr(self.pos)
    def on_board(self,x,y):
        return (x >= 0 and x < self.X and y >= 0 and y < self.Y)
    def on_wall(self,x,y):
        if self.mode == 0:
            return self.on_wallA(x,y)
        else:
            return self.on_wallB(x,y)
    def on_wallA(self,x,y):
        if (x == 1 or x == 5) and ((y >=0 and y < 3) or (y >= 6 and y < 9)):
            return True
        if (x == 3 or x == 7) and ((y >=0  and y < 3) or (y >= 6 and y < 9)):
            return True
        if y == 4 and not x == 5:
            return True
        return False
    
    def on_wallB(self,x,y):
        if (x == 1 or x == 5) and y >=0 and y < 8:
            return True
        if (x == 3 or x == 7) and y >=2 and y < 10:
            return True
        return False
    def on_minus(self,x,y):
        if y == 9:
            return True
        return False
    def on_goal(self,x,y):
        if x == 9 and  y == 8:
            return True
        return False
    def get_arr(self,pos):
        self.state = np.zeros((4,self.V_X,self.V_Y))

        for i in range(0,self.V_X):
            for j in range(0,self.V_Y):
                if not self.on_board(self.pos[0]+i-self.V_X/2,self.pos[1]+j-self.V_Y/2):
                    self.state[0][i][j] = 1
                elif self.on_wall(self.pos[0]+i-self.V_X/2,self.pos[1]+j-self.V_Y/2):
                    self.state[0][i][j] = 1
                if self.on_goal(self.pos[0]+i-self.V_X/2 ,self.pos[1]+j-self.V_Y/2):
                    self.state[2][i][j] = 1
                if self.on_minus(self.pos[0]+i-self.V_X/2 ,self.pos[1]+j-self.V_Y/2):
                    self.state[1][i][j] = 1
                if self.is_visited(self.pos[0]+i-self.V_X/2 ,self.pos[1]+j-self.V_Y/2):
                    self.state[3][i][j] = 1
        return self.state