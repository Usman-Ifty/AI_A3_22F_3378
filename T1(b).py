variables = ['D', 'S', 'E', 'K', 'U', 'T', 'W', 'Z']
domains = {var: ['red', 'green', 'blue'] for var in variables}

neighbors = {
    'D': ['S', 'E'],
    'S': ['D', 'K', 'E'],
    'E': ['D', 'K', 'S'],
    'K': ['E', 'S', 'U', 'T'],
    'U': ['K', 'T', 'W'],
    'T': ['K', 'U', 'W'],
    'W': ['U', 'T', 'Z'],
    'Z': ['T', 'W']
}

def is_consistent(var, value, assignment):
    for neighbor in neighbors[var]:
        if neighbor in assignment and assignment[neighbor] == value:
            return False
    return True

def forward_check(domains, var, value):
    new_domains = {v: list(domains[v]) for v in domains}
    for neighbor in neighbors[var]:
        if value in new_domains[neighbor]:
            new_domains[neighbor].remove(value)
            if not new_domains[neighbor]:
                return None
    return new_domains

def backtrack(assignment, domains):
    if len(assignment) == len(variables):
        return assignment
    
    unassigned = [v for v in variables if v not in assignment]
    var = min(unassigned, key=lambda v: len(domains[v]))
    
    for value in domains[var]:
        if is_consistent(var, value, assignment):
            assignment[var] = value
            new_domains = forward_check(domains, var, value)
            if new_domains:
                result = backtrack(assignment, new_domains)
                if result:
                    return result
            del assignment[var]
    return None

solution = backtrack({}, domains)
print("Solution:", solution)