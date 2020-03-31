from collections import defaultdict

topo3 = {    1: {1: 0,  2: 133, 3:float('inf'), 4: 64, 5:float('inf')},
             2: {1: 133, 2 : 0, 3: float('inf'), 4: float('inf'), 5: 64},
             3: {1: float('inf'), 2 : float('inf'), 3 : 0, 4 : 64, 5: 133},
             4: {1: 64, 2 : float('inf'), 3: 64, 4 : 0, 5: float('inf')},
             5: {1: float('inf'), 2: 64, 3: 133, 4: float('inf'), 5:0}
         }

topo1 = {
            1 : { 1: 0, 2: 10, 3: float('inf'), 4: float('inf'), 5 : float('inf'), 6: float('inf'),7: 64, 8 : 133, 9 : float('inf'), 10 : float('inf')},
            2 : { 1 : 10, 2 : 0, 3: 10, 4: float('inf'), 5: float('inf'), 6:  133, 7: 133, 8 : float('inf'), 9: float('inf'), 10 : float('inf')},
            3 : { 1 : float('inf'), 2: 10, 3: 0, 4: 64, 5: 64, 6: float('inf'), 7: float('inf'), 8 : float('inf'), 9 : float('inf'), 10 : float('inf')},
            4 : { 1 : float('inf'), 2: float('inf'), 3: 64, 4: 0, 5: 133, 6: 10, 7: float('inf'), 8 : float('inf'), 9 : float('inf'), 10 : float('inf')},
            5 : { 1 : float('inf'), 2: float('inf'), 3: 64, 4: 133, 5: 0, 6: float('inf'), 7 : float('inf'), 8 : float('inf'), 9 : float('inf'), 10 : 10},
            6 : { 1 : float('inf'), 2: 133, 3: float('inf'), 4: 10, 5: float('inf'), 6:  0, 7 : 64, 8 : float('inf'), 9 : float('inf'), 10 : float('inf')},
            7 : { 1 : 64, 2: 133, 3: float('inf'), 4: float('inf'), 5: float('inf'), 6: 64, 7 : 0, 8: 133, 9: 64, 10 : float('inf')},
            8 : { 1 : 133, 2: float('inf'), 3: float('inf'), 4: float('inf'), 5: float('inf'), 6: float('inf'), 7: 133, 8: 0, 9 : 64, 10 : float('inf')},
            9 : { 1 : float('inf'), 2: float('inf'), 3: float('inf'), 4: float('inf'), 5: float('inf'), 6: float('inf'), 7: 64, 8: 133, 9 : 0, 10: float('inf')},
            10: { 1 : float('inf'), 2: float('inf'), 3: float('inf'), 4: float('inf'), 5: 10, 6: float('inf'), 7 : float('inf'), 8 : float('inf'), 9 : float('inf'), 10 : 0}
        }

topo2 = {
            1 : { 1 : 0, 2: float('inf'), 3 : float('inf'), 4 : float('inf'), 5: 64, 6: 133, 7 : float('inf')},
            2 : { 1 : float('inf'), 2: 0, 3 : float('inf'), 4 : float('inf'),5: 64, 6 : float('inf'), 7: 133},
            3 : { 1 : float('inf'), 2: float('inf'), 3 : 0, 4: 133, 5 : float('inf'), 6: 64, 7: 10},
            4 : { 1 : float('inf'), 2 : float('inf'), 3: 133, 4 : 0, 5 : float('inf'), 6 : float('inf'), 7: 133},
            5 : { 1 : 64, 2: 64, 3 : float('inf'), 4 : float('inf'), 5 : 0, 6 : float('inf'), 7 : float('inf')},
            6 : { 1 : 133, 2 : float('inf'), 3: 64, 4 : float('inf'), 5 : float('inf'), 6 : 0, 7 : float('inf')},
            7 : { 1 : float('inf'), 2: 133, 3: 10, 4: 133, 5 : float('inf'), 6 : float('inf'), 7 : 0}
        }



prev=defaultdict(lambda:defaultdict(lambda:None))

def floyd(G):
    distance = G
    switch = set(distance)


    for i in switch:
        for j in switch:
            if not distance[i][j] == float('inf'):
                prev[i][j] = j

    for k in switch:
        for i in switch:
            for j in switch:
               if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    prev[i][j] = prev[i][k]


    for src in switch:
        for dst in switch:
            print"shortest path from ", src, " to ", dst, ": ", Path(src, dst),"cost: ",distance[src][dst]

    print "\n\n----------Matriks distance------------------- \n",
    for src in switch:
        print  distance[src]


def Path(src, dst):
    if prev[src][dst] is None:
        return []
    path = [src]
    while not src == dst:
        src = prev[src][dst]
        path.append(src)
    return path


def main():
    floyd(topo1)


if __name__ == "__main__":
    main()

