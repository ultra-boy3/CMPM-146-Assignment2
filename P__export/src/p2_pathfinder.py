import heapq

def find_path (source_point, destination_point, mesh):
    #Mesh is a dictionary with box dimensions and lists of adjacent boxes

    """
    Searches for a path from source_point to destination_point through the mesh

    Args:
        source_point: starting point of the pathfinder
        destination_point: the ultimate goal the pathfinder must reach
        mesh: pathway constraints the path adheres to

    Returns:

        A path (list of points) from source_point to destination_point if exists
        A list of boxes explored by the algorithm
    """

    #First thing we want to try is returning a list of boxes

    """
    Pseudocode

    create a priority queue, push source_point
    create a dictionary came_from containing previous locations

    while priority queue is not empty:
        current_box = queue.pop

        if current_box = destination
            create list path_taken
            using came_from, starting at the desintation, 
                add boxes to path_taken
            return path_taken
        
        for each neighbor of current_box (using mesh)
            (There are no distances so we don't have to worry about that rn)
            if neighbor is not in came_from:
                came_from.append(neighbor)
                queue.push(neighbor)
    
    (did not find a path)
    return None
    """

    frontier = []
    heapq.heapify(frontier) #Not sure but a different queue type might be better?
    heapq.heappush(frontier, source_point)

    came_from = {}
    came_from[source_point] = None

    while(len(frontier) > 0):
        current_box = heapq.heappop(frontier)

        if current_box = destination_point:
            path_taken = []
            add_this = destination_point
            while(add_this != None):
                path_taken.append(add_this)
                add_this = came_from[add_this]


    path = []
    boxes = {}

    return path, boxes.keys()
