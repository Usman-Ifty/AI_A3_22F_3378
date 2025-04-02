import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
domains = {var: ['red', 'green', 'blue'] for var in variables}
domains['WA'] = ['green']
domains['V'] = ['red']

neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

def ac3(domains, neighbors):
    queue = deque([(xi, xj) for xi in variables for xj in neighbors[xi]])
    while queue:
        xi, xj = queue.popleft()
        if revise(domains, xi, xj):
            if not domains[xi]:
                return False
            for xk in neighbors[xi]:
                if xk != xj:
                    queue.append((xk, xi))
    return True

def revise(domains, xi, xj):
    revised = False
    for x in domains[xi][:]:
        if not any(x != y for y in domains[xj]):
            domains[xi].remove(x)
            revised = True
    return revised

def show_graph(domains, neighbors):
    G = nx.Graph()
    for var in variables:
        for neighbor in neighbors[var]:
            G.add_edge(var, neighbor)

    color_map = {
        'red': '#e74c3c',
        'green': '#2ecc71',
        'blue': '#3498db'
    }

    node_colors = []
    for node in G.nodes:
        if len(domains[node]) == 1:
            node_colors.append(color_map[domains[node][0]])
        else:
            node_colors.append('#bdc3c7') 

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8, 6))
    nx.draw(
        G, pos, with_labels=True,
        node_color=node_colors,
        node_size=800,
        font_color='white',
        font_weight='bold'
    )
    plt.title("Australia Map Coloring CSP (Partial Assignment)")
    plt.show()

consistent = ac3(domains, neighbors)

if consistent:
    print("AC-3: The CSP is consistent with the partial assignment.")
else:
    print("AC-3: Inconsistency detected with the partial assignment!")

show_graph(domains, neighbors)
