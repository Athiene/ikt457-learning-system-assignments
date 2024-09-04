import random
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
from numpy.ma.extras import average


# Function to determine the probability for penalize or reward based on counted yes
def DetermineProbability(M):
    if M <= 3:
        return M*0.2
    if M > 3:
        return 0.6 - (M-3)*0.2
    #if M == 4:
    #    return 0.8
    #if M == 5:
    #    return 0.4


# Class that represents a Tsetlin automata
class Tsetlin:

    def __init__(self, n):
        self.n = n

        self.state = random.choice([self.n, self.n + 1])
        self.state = 6

    # Function to determine if the automata gets penelized or rewarded based on probability calculated
    def determinePenalty(self, P):
        if random.random() <= P:
            self.reward()
            return 1
        else:
            self.penalize()
            return 2

    # Function to penalize itself
    def penalize(self):
        if self.state <= self.n:
            self.state += 1
        elif self.state > self.n:
            self.state -= 1

    # Function to reward itself
    def reward(self):
        if self.state <= self.n and self.state > 1:
            self.state -= 1
        elif self.state > self.n and self.state < 2*self.n:
            self.state += 1

    # Function that coin flips decision of 1 or 2
    def makeDecision(self):
        if self.state <= self.n:
            return 1
        else:
            return 2

# Creating 2 lists for storing data and plotting
ChartList = [0, 0, 0, 0, 0, 0]
AutoMataList = [0, 1, 2, 3, 4, 5]

PenaltiesList1 = [0, 0, 0]
PenaltiesList2 = [0, 0, 0]
PenaltiesList3 = [0, 0, 0]
PenaltiesList4 = [0, 0, 0]
PenaltiesList5 = [0, 0, 0]
AutomataPenaltieList = [PenaltiesList1, PenaltiesList2, PenaltiesList3, PenaltiesList4, PenaltiesList5]

PenaltiesListX = [0, 1, 2]

TsetlinAutomata1List = [0, 0, 0, 0, 0, 0, 0]
TsetlinAutomata2List = [0, 0, 0, 0, 0, 0, 0]
TsetlinAutomata3List = [0, 0, 0, 0, 0, 0, 0]
TsetlinAutomata4List = [0, 0, 0, 0, 0, 0, 0]
TsetlinAutomata5List = [0, 0, 0, 0, 0, 0, 0]

# Creating the TsetlinAutomatas with 3 states
TsetlinAutomata1 = Tsetlin(3)
TsetlinAutomata2 = Tsetlin(3)
TsetlinAutomata3 = Tsetlin(3)
TsetlinAutomata4 = Tsetlin(3)
TsetlinAutomata5 = Tsetlin(3)

# Storing the created TsetlinAutomatas in a list
TsetlinAutomataList = [TsetlinAutomata1, TsetlinAutomata2, TsetlinAutomata3, TsetlinAutomata4, TsetlinAutomata5]
AutoMataListList = [TsetlinAutomata1List, TsetlinAutomata2List, TsetlinAutomata3List, TsetlinAutomata4List, TsetlinAutomata5List]

# List to store M values
M_values = []
average_M_values = []
cumulative_M = 0

Iterations = 1000

# MAIN LOOP
for i in range(Iterations):
    M = 0

    # Invoking the makeDecision function for each stored automata in TsetlinAutomataList
    # Then stores all the YES (1) results in M
    for tsetlin in TsetlinAutomataList:
        action = tsetlin.makeDecision()
        if action == 1:
            M += 1

    # Invokes the DetermineProbability function that calculates a probability based on its parameter M
    # Then using determinePenalty function to determines the penalty (penalize/reward) for each automata separately using the calculated probability.
    for k, tsetlin in enumerate(TsetlinAutomataList):
        AutomataPenaltieList[TsetlinAutomataList.index(tsetlin)][tsetlin.determinePenalty(DetermineProbability(M))] += 1

    ChartList[M] += 1

    # Store the current M value
    M_values.append(M)

    # Prints the states of each automata
    for j, tsetlin in enumerate(TsetlinAutomataList):
        AutoMataListList[j][tsetlin.state] += 1
        print("#State: ", tsetlin.state)

    # Prints the current iteration and the amount of YES for the iteration
    print("Simulation: ", i, "#Yes: ", M)

    # Calculate average
    cumulative_M += M
    temp = cumulative_M / (i+1)
    average_M_values.append(temp)

# Plot M values over iterations + Cumulative average
plt.plot(range(Iterations), M_values, color='b', label='M')
plt.plot(range(Iterations), average_M_values, color='r', label='Average')
plt.title('M Values over Iterations')
plt.xlabel('Iteration')
plt.ylabel('M')
plt.legend()
plt.show()

# Creates a bar plot based on 2 parameters: AutoMataList and ChartList for amount of YES
plt.bar(AutoMataList, ChartList)
plt.title('Bar Chart')
plt.xlabel('Counted Yes')
plt.ylabel('Amount of Counted Yes')
plt.show()

# Prints the cumulative amount of counted Yes for each counted YES
print(ChartList)

# Print graph of the states for different automatas
StatesList = [0, 1, 2, 3, 4, 5, 6]
for Tsetlin in AutoMataListList:
    plt.bar(StatesList, Tsetlin)

    # Implemented titles for the plot
    plt.title(f"{AutoMataListList.index(Tsetlin) + 1} Tsetlin Automata")
    plt.xlabel('States')
    plt.ylabel('Counted times')
    AutoMataListList.index(Tsetlin)
    plt.show()

# Plot a graph of counted rewards and penalize for each automata
for tsetlin in AutomataPenaltieList:
    plt.bar(PenaltiesListX, tsetlin)

    # Implemented titles for the plot
    plt.title(f"{AutomataPenaltieList.index(tsetlin) + 1} Automata: Rewards (1) VS Penalties (2)")
    plt.xlabel('')
    plt.ylabel('Counted times')
    plt.show()
    print(tsetlin)

