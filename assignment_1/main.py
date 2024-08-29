import random
import matplotlib.pyplot as plt

def DetermineProbability(M):
    if M <= 3:
        return M*0.2
    if M > 3:
        return 0.6 - (M-3)*0.2
    #if M == 4:
    #    return 0.8
    #if M == 5:
    #    return 0.8



class Tsetlin:
    def __init__(self, n):
        self.n = n

        self.state = random.choice([self.n, self.n + 1])
        #self.state = 6

    def determinePenalty(self, P):
        if random.random() <= P:
            self.reward()
            return
        else:
            self.penalize()
            return

    def penalize(self):
        if self.state <= self.n:
            self.state += 1
        elif self.state > self.n:
            self.state -= 1

    def reward(self):
        if self.state <= self.n and self.state > 1:
            self.state -= 1
        elif self.state > self.n and self.state < 2*self.n:
            self.state += 1

    def makeDecision(self):
        if self.state <= self.n:
            return 1
        else:
            return 2

ChartList = [0, 0, 0, 0, 0, 0]
AutoMataList = [0, 1, 2, 3, 4, 5]

TsetlinAutomata1 = Tsetlin(3)
TsetlinAutomata2 = Tsetlin(3)
TsetlinAutomata3 = Tsetlin(3)
TsetlinAutomata4 = Tsetlin(3)
TsetlinAutomata5 = Tsetlin(3)

for i in range(10000):
    TsetlinAutomataList = [TsetlinAutomata1, TsetlinAutomata2, TsetlinAutomata3, TsetlinAutomata4, TsetlinAutomata5]
    M = 0

    for tsetlin in TsetlinAutomataList:
        action = tsetlin.makeDecision()
        if action == 1:
            M += 1

    for tsetlin in TsetlinAutomataList:
        tsetlin.determinePenalty(DetermineProbability(M))

    ChartList[M] += 1

    for tsetlin in TsetlinAutomataList:
        print("#State: ", tsetlin.state)

    print("Simulation: ", i, "#Yes: ", M)

plt.bar(AutoMataList, ChartList)

plt.title('Bar Chart')
plt.xlabel('Counted Yes')
plt.ylabel('Amount of Counted Yes')

plt.show()
print(ChartList)

