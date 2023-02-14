from agent import Agent
from helper import getStockData, getState, formatPrice
import sys

window_size = 50
batch_size = 32

agent = Agent(window_size, batch_size)
data= getStockData()

l = len(data) - 1
episode_count = 300

for e  in range(episode_count):
    print("Episode " + str(e) + "/" + str(episode_count))
    state = getState(data, 0 , window_size + 1)
    
    agent.inventory = []
    
    total_profit = 0
    done = False
    for t in range(l):
        action = agent.act(state)
        action_prob = agent.actor_local.model.predit(state)
        
        next_state = getState(data, t + 1, window_size + 1)
        reward = 0
        
        if action ==1:
            agent.inventory.append(data[t])
            print("Buy: " + formatPrice(data[t]))
        elif action ==2 and len(agent.inventory) > 0:
            bought_price = agent.inventory.pop(0)
            reward = max(data[t]-bought_price, 0)
            total_profit += data[t] - bought_price
            print("sell: " + formatPrice(data[t]) + "| profit: " + formatPrice(data[t] - bought_price))
            
        if t ==l-1:
            done = True
        agent.step(action_prob, reward, next_state, done)
        state = next_state
        
        if done:
            print("----------------------------")
            print(f"Total Profit: + {formatPrice(total_profit)}")
            print("-------------------------------")
            