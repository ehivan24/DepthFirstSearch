__author__ = 'edwingsantos'

from DepthFirstSearch.Node import Node

import DFS

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("F")
node6 = Node("G")

node1.adjacentList.append(node2)
node1.adjacentList.append(node3)
node2.adjacentList.append(node4)
node4.adjacentList.append(node5)
node6.adjacentList.append(node1)

DFS.dfs(node1)
