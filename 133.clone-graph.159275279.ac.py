#
# [133] Clone Graph
#
# https://leetcode.com/problems/clone-graph/description/
#
# algorithms
# Medium (25.16%)
# Total Accepted:    155.7K
# Total Submissions: 619K
# Testcase Example:  '{}'
#
# 
# Clone an undirected graph. Each node in the graph contains a label and a list
# of its neighbors.
# 
# 
# 
# 
# OJ's undirected graph serialization:
# 
# 
# Nodes are labeled uniquely.
# 
# 
# We use # as a separator for each node, and , as a separator for node label
# and each neighbor of the node.
# 
# 
# 
# 
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
# 
# 
# 
# The graph has a total of three nodes, and therefore contains three parts as
# separated by #.
# 
# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a
# self-cycle.
# 
# 
# 
# 
# Visually, the graph looks like the following:
# 
# ⁠      1
# ⁠     / \
# ⁠    /   \
# ⁠   0 --- 2
# ⁠        / \
# ⁠        \_/
# 
# 
# 
# 
#
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return
        nodeCopy = UndirectedGraphNode(node.label)
        dic = {node: nodeCopy}
        queue = [node]
        
        while queue:
            node = queue.pop(0)
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy
        
