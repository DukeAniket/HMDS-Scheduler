class Graph:
    def __init__(self, tasks) -> None:
        self.daG = [[0]*tasks]*tasks
        return
    def insertEdge(self, T1, T2, edge):
        self.daG[T1-1][T2-1] = edge
        return
    def getDAG(self):
        return self.daG

_tasks = 3

g = Graph(_tasks)
g.insertEdge(1,3,56)
g.insertEdge(2,1, 34)
res = g.getDAG()
T_entry = 0
T_exit = 2
processors = 3
L = [0]*processors
b = [[1]*_tasks]*_tasks
c = [[[[0]*processors]*processors]*_tasks]*_tasks
w = [[0]*processors]*_tasks
# Value of w, L and b required

for i in range(_tasks):
    for j in range(_tasks):
        for m in range(processors):
            for n  in range(processors):
                c[i][j][m][n] = L[m] + res[i][j]/b[m][n]

pred = {}
succ = {}

for k in range(_tasks):
    pred[k] = []
    succ[k] = []

for i in range(_tasks):
    for j in range(_tasks):
        if(res[i][j] != 0):
            pred[j].append(i)
            succ[i].append(j)

def getSetup():
    return [g, T_entry, T_exit, processors, _tasks, pred, succ, c, w]