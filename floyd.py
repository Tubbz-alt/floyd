G = [
    [0, 133, float('inf'), float('inf'), float('inf')],
    [133, 0, float('inf'), float('inf'), 64],
    [float('inf'), float('inf'), 0, 64, 133],
    [float('inf'), float('inf'), 64, 0, float('inf')],
    [float('inf'), 64, 133, float('inf'), 0]
]


def printGraf(G):
    for row in (G):
        print(row)


prev = []


def floyd(G):
    distance = G
    switch = len(distance)
    print(switch)

    for i in range(1, switch + 1):
        prev.append([])
        for j in range(1, switch + 1):
            prev[i - 1].append(None)
            if not distance[i - 1][j - 1] == float('inf'):
                prev[i - 1][j - 1] = j

    for k in range(1,switch+1):
        for i in range(1,switch+1):
            for j in range(1,switch+1):
               if distance[i-1][j-1] > distance[i-1][k-1] + distance[k-1][j-1]:
                    distance[i-1][j-1] = distance[i-1][k-1] + distance[k-1][j-1]
                    prev[i-1][j-1] = prev[i-1][k-1]
    printGraf(distance)

    for src in range(1, switch + 1):
        for dst in range(1, switch + 1):
            print"shortest path from ", src, " to ", dst, ": ", Path(src - 1, dst - 1)


def Path(src, dst):
    if prev[src][dst] is None:
        return []
    path = [src + 1]
    while not src == dst:
        src = prev[src][dst] - 1
        path.append(src + 1)
    return path


def main():
    floyd(G)


if __name__ == "__main__":
    main()
