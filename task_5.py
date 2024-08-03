import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        """
        Initialize a Node object with a key, color, and unique ID.
        """
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, highlight_nodes=[]):
    """
    Draw the binary tree with node colors and labels.
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [tree.nodes[node]["color"] for node in tree.nodes()]
    labels = {node: tree.nodes[node]["label"] for node in tree.nodes()}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos, labels=labels, node_color=colors, with_labels=True, node_size=2500
    )
    plt.show()


def bfs(root):
    """
    Perform breadth-first search (BFS) traversal and return the node order.
    """
    queue = [root]
    order = []
    while queue:
        current = queue.pop(0)
        order.append(current)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return order


def dfs(root):
    """
    Perform depth-first search (DFS) traversal and return the node order.
    """
    stack = [root]
    order = []
    while stack:
        current = stack.pop()
        order.append(current)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return order


def assign_colors(nodes):
    """
    Assign a unique color to each node based on its order in the traversal.
    """
    num_nodes = len(nodes)
    for i, node in enumerate(nodes):
        r = int(255 * (i / (num_nodes - 1)))
        g = int(128 + 127 * (i / (num_nodes - 1)))
        b = 255 - r
        color = f"#{r:02x}{g:02x}{b:02x}"
        node.color = color


# Create the binary tree
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Visualize BFS traversal
bfs_order = bfs(root)
assign_colors(bfs_order)
draw_tree(root)

# Reset node colors for DFS visualization
for node in bfs_order:
    node.color = "skyblue"

# Visualize DFS traversal
dfs_order = dfs(root)
assign_colors(dfs_order)
draw_tree(root)