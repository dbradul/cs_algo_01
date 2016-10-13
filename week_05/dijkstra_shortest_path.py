from heapq import *


REMOVED = "<item is removed>"
frontier_map = {}

class node_ref:
    def __init__(self, total_cost, node):
        self.total_cost = total_cost
        self.node = node

    # TODO: override other cmp functions
    def __lt__(self, other):
        return self.total_cost < other.total_cost


def extract_min(frontier):
    while frontier:
        item = heappop(frontier)
        if item.node != REMOVED:
            del frontier_map[item.node]
            return item


def update_frontier(adj_list, frontier, w, X):
    #print adj_list[v]
    for neighbor in adj_list[w]:
        node, cost = int(neighbor[0]), int(neighbor[1])
        if node not in X:
            item = node_ref(A[w] + cost, node)
            if node in frontier_map:
                if frontier_map[node].total_cost > item.total_cost:
                    frontier_map[node].node = REMOVED
                    frontier_map[node] = item
                    heappush(frontier, item)
            else:
                frontier_map[node] = item
                heappush(frontier, item)


def dijkstra_shortest_pathes(adj_list, A, frontier, X):
    while(len(X) < len(adj_list)):
        item = extract_min(frontier)
        w = item.node
        A[w] = item.total_cost
        X.append(w)
        update_frontier(adj_list, frontier, w, X)


if __name__ == '__main__':
    f = open("dijkstraData.txt")
    line_lists = [line.split() for line in f.readlines()]

    adj_list = {}
    for elem in line_lists:
        adj_list[int(elem[0])] = [pair.split(',') for pair in elem[1:]]

    # print adj_list
    # adj_list[1] = [[2,1],[3,13]]
    # adj_list[2] = [[3,2],[4,4],[5,7]]
    # adj_list[3] = [[4,1]]
    # adj_list[4] = [[5,2]]
    # adj_list[5] = []

    A = [0] * (len(adj_list)+1)
    s_node = 1
    frontier = []
    A[s_node] = 0
    X = [s_node]

    update_frontier(adj_list, frontier, s_node, X)
    dijkstra_shortest_pathes(adj_list, A, frontier, X)
    # print A
    result = "%d,%d,%d,%d,%d,%d,%d,%d,%d,%d" % \
          (A[7],A[37],A[59],A[82],A[99],A[115],A[133],A[165],A[188],A[197])
    print result
    assert result == "2599,2610,2947,2052,2367,2399,2029,2442,2505,3068"