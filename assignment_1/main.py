import random
import matplotlib.pyplot as plt

# Function to determine the probability for penalize or reward based on counted yes
def DetermineProbability(M):
    if M <= 3:
        return M*0.2
    if M > 3:
        return 0.6 - (M-3)*0.2
    #if M == 4:
    #    return 0.8
    #if M == 5:
    #    return 0.8


# Class that represents a Tsetlin automata
class Tsetlin:

    def __init__(self, n):
        self.n = n

        self.state = random.choice([self.n, self.n + 1])
        #self.state = 6

    # Function to determine if the automata gets penelized or rewarded based on probability calculated
    def determinePenalty(self, P):
        if random.random() <= P:
            self.reward()
            return
        else:
            self.penalize()
            return

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

# Creating the TsetlinAutomatas with 3 states
TsetlinAutomata1 = Tsetlin(3)
TsetlinAutomata2 = Tsetlin(3)
TsetlinAutomata3 = Tsetlin(3)
TsetlinAutomata4 = Tsetlin(3)
TsetlinAutomata5 = Tsetlin(3)

# Storing the created TsetlinAutomatas in a list
TsetlinAutomataList = [TsetlinAutomata1, TsetlinAutomata2, TsetlinAutomata3, TsetlinAutomata4, TsetlinAutomata5]

# MAIN LOOP
for i in range(10000):
    M = 0

    # Invoking the makeDecision function for each stored automata in TsetlinAutomataList
    # Then stores all the YES (1) results in M
    for tsetlin in TsetlinAutomataList:
        action = tsetlin.makeDecision()
        if action == 1:
            M += 1

    # Invokes the DetermineProbability function that calculates a probability based on its parameter M
    # Then using determinePenalty function to determines the penalty (penalize/reward) for each automata separately using the calculated probability.
    for tsetlin in TsetlinAutomataList:
        tsetlin.determinePenalty(DetermineProbability(M))

    ChartList[M] += 1

    # Prints the states of each automata
    for tsetlin in TsetlinAutomataList:
        print("#State: ", tsetlin.state)

    # Prints the current iteration and the amount of YES for the iteration
    print("Simulation: ", i, "#Yes: ", M)

#Creates a bar plot based on 2 parameters: AutoMataList and ChartList
plt.bar(AutoMataList, ChartList)

#Implemented titles for the plot
plt.title('Bar Chart')
plt.xlabel('Counted Yes')
plt.ylabel('Amount of Counted Yes')

# Shows the plot
plt.show()

# Prints the cumulative amount of counted Yes for each counted YES
print(ChartList)

