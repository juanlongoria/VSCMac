from collections import deque

# Define pipe connection logic
pipe_connections = {
    '═': [(0, 1), (0, -1)],
    '║': [(1, 0), (-1, 0)],
    '╔': [(0, 1), (1, 0)],
    '╗': [(0, 1), (-1, 0)],
    '╚': [(0, -1), (1, 0)],
    '╝': [(0, -1), (-1, 0)],
    '╠': [(1, 0), (0, -1)],
    '╣': [(1, 0), (0, 1)],
    '╦': [(0, 1), (-1, 0)],
    '╩': [(0, -1), (-1, 0)],
}

def parse_input(file_path):
    grid = {}
    source = None
    
    with open(file_path, 'r') as file:
        for line in file:
            char, x, y = line.split()
            x, y = int(x), int(y)
            grid[(x, y)] = char
            if char == '*':
                source = (x, y)
    
    return grid, source

def get_neighbors(x, y):
    return [(x+dx, y+dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]

def can_connect(pipe1, pipe2, direction1, direction2):
    if direction1 not in pipe_connections[pipe1]:
        return False
    if direction2 not in pipe_connections[pipe2]:
        return False
    return True

def bfs(grid, start):
    queue = deque([start])
    visited = set()
    visited.add(start)
    reachable_sinks = set()
    
    while queue:
        x, y = queue.popleft()
        if grid[(x, y)].isalpha() and grid[(x, y)] != '*':
            reachable_sinks.add(grid[(x, y)])
        
        for nx, ny in get_neighbors(x, y):
            if (nx, ny) in grid and (nx, ny) not in visited:
                if can_connect(grid[(x, y)], grid[(nx, ny)], (nx-x, ny-y), (x-nx, y-ny)):
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    
    return reachable_sinks

def find_sinks_connected_to_source(file_path):
    grid, source = parse_input(file_path)
    if source is None:
        return set()
    return bfs(grid, source)

# Example usage
if __name__ == "__main__":
    connected_sinks = find_sinks_connected_to_source('Users/juanlongoria/Downloads/coding_qual_input.txt')
    print("Sinks connected to the source:", connected_sinks)
