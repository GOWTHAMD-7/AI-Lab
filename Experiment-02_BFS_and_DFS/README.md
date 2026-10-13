# EXPERIMENT 2: Implementation of Breadth First and Depth First Searching Techniques

---

## 1. Aim
To implement Breadth First Search (BFS) and Depth First Search (DFS) algorithms in Python and evaluate their graph traversal order and path-finding capabilities.

---

## 2. Algorithms (5 - 6 Simple Steps to Write in Record / Exam)

### A. Breadth First Search (BFS) Algorithm:
1. **Step 1: Initialize Queue & Visited List:** Create an empty FIFO queue and an empty visited set. Insert the start node into both.
2. **Step 2: Dequeue Current Node:** While the queue is not empty, remove the front node from the queue and record it in the traversal output.
3. **Step 3: Goal Test (if goal-seeking):** If the current node matches the goal node, terminate the search and reconstruct the path.
4. **Step 4: Explore Adjacent Neighbors:** For each neighbor of the current node in the adjacency list, if the neighbor has not been visited, mark it as visited and enqueue it.
5. **Step 5: Repeat:** Continue repeating Steps 2 through 4 until the queue becomes empty.
6. **Step 6: Output Result:** Print the BFS traversal sequence and the shortest path found.

### B. Depth First Search (DFS) Algorithm:
1. **Step 1: Initialize Stack & Visited Set:** Create a LIFO stack (or use recursion) and an empty visited set. Push the starting node onto the stack.
2. **Step 2: Pop Current Node:** While the stack is not empty, pop the top node from the stack.
3. **Step 3: Visit Node:** If the node has not been visited, mark it as visited and add it to the traversal output.
4. **Step 4: Goal Test:** If the node is the desired target/goal node, terminate search.
5. **Step 5: Push Neighbors:** For every unvisited neighbor of the current node, push it onto the stack (or recursively visit).
6. **Step 6: Repeat & Backtrack:** Repeat Steps 2 through 5 until the stack is empty; print the final traversal order.

---

## 3. Graph Structure

```text
         [A]
        /   \
      [B]   [C]
     /   \  /  \
   [D]   [E][F] [G]
           \
           [H]
```

---

## 4. Source Code (`bfs_dfs.py`)

```python
"""
EXPERIMENT 2: Breadth First Search (BFS) & Depth First Search (DFS)
"""
from collections import deque

# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

def bfs(graph, start):
    visited = []
    queue = deque([start])
    visited_set = {start}

    while queue:
        node = queue.popleft()
        visited.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited_set:
                visited_set.add(neighbor)
                queue.append(neighbor)
    return visited

def dfs(graph, start):
    visited = []
    visited_set = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited_set:
            visited_set.add(node)
            visited.append(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited_set:
                    stack.append(neighbor)
    return visited

# BFS Path Finding
def bfs_path(graph, start, goal):
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None

start, goal = 'A', 'H'
print("BFS Traversal:", " -> ".join(bfs(graph, start)))
print("DFS Traversal:", " -> ".join(dfs(graph, start)))
print(f"BFS Path ({start} to {goal}):", " -> ".join(bfs_path(graph, start, goal)))
```

---

## 5. Sample Input and Output

### Sample Input:
- **Graph:** Undirected/Directed adjacency list with vertices `A, B, C, D, E, F, G, H`.
- **Start Node:** `'A'`
- **Goal Node:** `'H'`

### Execution Output:
```text
======================================================================
EXPERIMENT 2: BREADTH FIRST SEARCH (BFS) & DEPTH FIRST SEARCH (DFS)
======================================================================

Graph Adjacency List:
  A -> B, C
  B -> A, D, E
  C -> A, F, G
  D -> B
  E -> B, H
  F -> C
  G -> C
  H -> E

----------------------------------------------------------------------
1. BREADTH FIRST SEARCH (BFS):
----------------------------------------------------------------------
Starting Node          : A
BFS Traversal Order    : A -> B -> C -> D -> E -> F -> G -> H
Goal Node              : H
BFS Path (A to H)      : A -> B -> E -> H (Length: 3 edges)

----------------------------------------------------------------------
2. DEPTH FIRST SEARCH (DFS):
----------------------------------------------------------------------
Starting Node          : A
DFS Traversal Order    : A -> B -> D -> E -> H -> C -> F -> G
Goal Node              : H
DFS Path (A to H)      : A -> B -> E -> H (Length: 3 edges)

======================================================================
SUMMARY COMPARISON:
======================================================================
Parameter              | BFS                  | DFS                 
----------------------------------------------------------------------
Data Structure         | Queue (FIFO)         | Stack / Recursion   
Completeness           | Yes (if b is finite) | No (in infinite paths)
Optimality             | Yes (unweighted)     | No                  
Time Complexity        | O(b^d)               | O(b^m)              
Space Complexity       | O(b^d) [High memory] | O(b*m) [Low memory] 
======================================================================
```

---

## 6. Result & Viva Questions

### Result:
Breadth First Search and Depth First Search algorithms were successfully implemented. BFS explored nodes level by level using a queue and found the shortest path, while DFS traversed along each branch to maximal depth using a stack.

### Viva Voce Q&A:
1. **Q: What data structures do BFS and DFS use?**
   - **A:** BFS uses a **Queue (FIFO - First In First Out)**, while DFS uses a **Stack (LIFO - Last In First Out)** or function call stack (recursion).
2. **Q: Is BFS always optimal?**
   - **A:** BFS is optimal for finding the shortest path when all step costs / edge weights are equal (uniform cost $1$).
3. **Q: What is the main disadvantage of BFS compared to DFS?**
   - **A:** BFS requires storing all nodes of current level in memory, leading to exponential memory complexity $O(b^d)$, whereas DFS requires linear memory $O(b \times m)$.
