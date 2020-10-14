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

    path = []
    boxes = {}
    path_taken = []

    frontier = []
    heapq.heapify(frontier) #Not sure but a different queue type might be better?
    heapq.heappush(frontier, source_point)

    boxes[source_point] = None

    while(len(frontier) > 0):
        current_box = heapq.heappop(frontier)

        if current_box == destination_point:
            # Insert current_box into boxes, w/ previous as value
            while(current_box != None):
                path_taken.append(current_box)
                current_box = boxes[current_box] #destination point should already have something in boxes
            break

        neighbors = mesh(current_box)[1] #Hopefully this gets the neighbor list?
        for neighbor in neighbors:
            if(neighbor not in boxes):
                boxes[neighbor] = current_box #Add neighbor to list of boxes
                heapq.heappush(frontier, neighbor)

    print(path_taken)
    return path, path_taken #Replaced boxes.keys() w/ path_taken
