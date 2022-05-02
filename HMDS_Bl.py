import pft_rank
import numpy

pftRankres = pft_rank.pftRank()

pft = pftRankres[0]
rank = pftRankres[1]
procrs = pftRankres[2]
numTasks = pftRankres[3]
graph = pftRankres[4]
pred = pftRankres[5]
succ = pftRankres[6]
c = pftRankres[7]
w = pftRankres[8]
das = graph.getDAG()
tEntry = 0

AST = [0]*numTasks
AFT = [0]*numTasks
avail = [0]*procrs
allot = [0]*numTasks

s = numpy.array(rank)
taskList = numpy.argsort(s)
taskList.reverse()

EST = [[0]*procrs]*numTasks
EFT = [[0]*procrs]*numTasks
O_eft = [[0]*procrs]*numTasks


for task in taskList:
    for p in range(procrs):
        if(task == tEntry):
            EST[task][p] = 0
        else:
            z = 0
            for i in pred[task]:
                z += AFT[task] + c[i][task][allot[i]][p]
            EST[task][p] = max(avail[p], z)
        EFT[task][p] = EST[task][p] + w[task][p]
        O_eft[task][p] = EFT[task][p] + pft[task][p]

    processor = 0
    for i in range(procrs):
        if(O_eft[task][i] < O_eft[task][processor]):
            processor = i
    AST[task] = EST[task][processor]
    AFT[task] = EFT[task][processor]

    allot[task] = processor
    avail[processor] = AST[task] + AFT[task]

print(allot)
