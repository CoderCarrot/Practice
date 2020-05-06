rectangle = {
    # Coordinates of bottom-left corner
    'left_x'   : 1,
    'bottom_y' : 1,

    # Width and height
    'width'    : 6,
    'height'   : 3,

} 

def find_rectangular_intersection(rectangle1, rectangle2):



    left_x1 = rectangle1[left_x]
    bottom_y1 = rectangle1[bottom_y]

    left_x2 = rectangle2[left_x]
    bottom_y2 = rectangle2[bottom_y]
   

    x_coords1 = [left_x1]
    for num in range(rectangle1[width]):
        x_coords1.append(left_x1 + num + 1)
    
    y_coords1 = [bottom_y1]
    for num in range(rectangle1[height]):
        x_coords1.append(bottom_y1 + num + 1)

    x_coords2 = [left_x2]
    for num in range(rectangle2[width]):
        x_coords2.append(left_x2 + num + 1)

    y_coords2 = [bottom_y2]
    for num in range(rectangle2[height]):
        x_coords1.append(bottom_y2 + num + 1)

    overlap_rectangle = {
        # Coordinates of bottom-left corner
        'left_x'   : None,
        'bottom_y' : None,

        # Width and height
        'width'    : None,
        'height'   : None,
    }

    if overlap in x_coords1 and x_coords2:

        left_x_overlap = lowest number x coords overlap
        width_overlap = highest number x coords overlap - left_x_overlap
    
    if overlap in y_coords1 and y_coords2:

        bottom_y_overlap = lowest number y coords overlap
        height_overlap = highest number y coords overlap - bottom_y_overlap

    return overlap_rectangle
    