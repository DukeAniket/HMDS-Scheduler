import setup

def pftRank():
    imp = setup.getSetup()
    gra = imp[0]
    tEntry = imp[1]
    tExit = imp[2]
    procrs = imp[3]
    numTasks = imp[4]
    pred = imp[5]
    succ = imp[6]
    c = imp[7]
    w = imp[8]
    rank = [1]*numTasks

    PFT = [[0]*procrs]*numTasks

    queue = []
    queue.append(tExit)

    for z in range(numTasks-1, -1, -1):
        for i in range(procrs):
            if(z == tExit):
                PFT[z][i] = 0
            else:
                k = 0
                for _k in succ[z]:
                    l = PFT[z][0] + c[z][_k][i][0] + w[_k][0]
                    for processor in range(procrs):
                        l = min(l, PFT[z][processor] + c[z][_k][i][processor] + w[_k][processor])
                    k = max(k, l)
                PFT[z][i] = k
                continue
        k = 0
        for i in PFT[z]:
            k += i
        k = k/(numTasks)

        rank[z] = k

        MSR = 0

        for i in range(numTasks):
            if(gra.getDAG()[z][i]!=0):
                MSR = max(MSR, rank[z])
        
        if(rank[z] <= MSR):
            for i in range(procrs):
                PFT[z][i] *= (MSR + 0.1)/rank[z]
            k = 0
            for i in PFT[z]:
                k += i
            k = k/(numTasks)

            rank[z] = k

    return [PFT, rank, procrs, numTasks, gra, pred, succ, c, w]