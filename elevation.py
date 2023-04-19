'''CSC108: Assignment 2
Author: Ossama Benaini
Student number: 1006092933
'''

from typing import List
import math

THREE_BY_THREE = [[1, 2, 1],
                  [4, 6, 5],
                  [7, 8, 9]]

FOUR_BY_FOUR = [[1, 2, 6, 5],
                [4, 5, 3, 2],
                [7, 9, 8, 1],
                [1, 2, 1, 4]]

UNIQUE_3X3 = [[1, 2, 3],
              [9, 8, 7],
              [4, 5, 6]]

UNIQUE_4X4 = [[10, 2, 3, 30],
              [9, 8, 7, 11],
              [4, 5, 6, 12],
              [13, 14, 15, 16]]


def compare_elevations_within_row(elevation_map: List[List[int]], map_row: int,
                                  level: int) -> List[int]:
    '''Return a new list containing three counts: the number of elevations 
    from row number map_row of elevation_map that are less than, equal to, 
    and greater than elevation level.

    Precondition: elevation_map is a valid elevation map.
                  0 <= map_row < len(elevation_map).

    >>> compare_elevations_within_row(THREE_BY_THREE, 1, 5)
    [1, 1, 1]
    >>> compare_elevations_within_row(FOUR_BY_FOUR, 1, 2)
    [0, 1, 3]
    '''
    new_list = []
    greater_count = 0
    less_count = 0
    equal_count = 0
    for j in elevation_map[map_row]:
        if j > level:
            greater_count += 1
        elif j == level:
            equal_count += 1
        else:
            less_count += 1
    new_list.extend([less_count, equal_count, greater_count])
    return new_list

def update_elevation(elevation_map: List[List[int]], start: List[int],
                     stop: List[int], delta: int) -> None:
    '''Modify elevation_map so that the elevation of each cell 
    between cells start and stop, inclusive, changes by amount  delta.

    Precondition: elevation_map is a valid elevation map.
                  start and stop are valid cells in elevation_map.
                  start and stop are in the same row or column or both.
                  If start and stop are in the same row,
                      start's column <=  stop's column.
                  If start and stop are in the same column,
                      start's row <=  stop's row.
                  elevation_map[i, j] + delta >= 1
                      for each cell [i, j] that will change.

    >>> THREE_BY_THREE_COPY = [[1, 2, 1],
    ...                        [4, 6, 5],
    ...                        [7, 8, 9]]
    >>> update_elevation(THREE_BY_THREE_COPY, [1, 0], [1, 1], -2)
    >>> THREE_BY_THREE_COPY
    [[1, 2, 1], [2, 4, 5], [7, 8, 9]]
    >>> FOUR_BY_FOUR_COPY = [[1, 2, 6, 5],
    ...                      [4, 5, 3, 2],
    ...                      [7, 9, 8, 1],
    ...                      [1, 2, 1, 4]]
    >>> update_elevation(FOUR_BY_FOUR_COPY, [1, 2], [3, 2], 1)
    >>> FOUR_BY_FOUR_COPY
    [[1, 2, 6, 5], [4, 5, 4, 2], [7, 9, 9, 1], [1, 2, 2, 4]]

    '''
    l = start[0]
    t = start[-1]
    x = stop[0]
    y = stop[-1]
    if l == x:
        elevation_map[l][t] = elevation_map[l][t] + delta
        elevation_map[x][y] = elevation_map[x][y] + delta
    elif l != x:
        difference = abs(l - x)
        count = 0
        elevation_map[x][y] = elevation_map[x][y] + delta
        while count < difference:
            elevation_map[l + count][t] = elevation_map[l + count][t] + delta
            count += 1


def get_average_elevation(elevation_map: List[List[int]]) -> float:
    '''Return the average elevation across all cells in elevation_map.

    Precondition: elevation_map is a valid elevation map.

    >>> get_average_elevation(UNIQUE_3X3)
    5.0
    >>> get_average_elevation(FOUR_BY_FOUR)
    3.8125
    '''
  
    total_avg_sublist = 0
    for sublist in elevation_map:
        avg_sublist = sum(sublist)/len(sublist)
        total_avg_sublist += avg_sublist
    return total_avg_sublist / len(sublist)
        

def find_peak(elevation_map: List[List[int]]) -> List[int]:
    '''Return the cell that is the highest point in the elevation_map.

    Precondition: elevation_map is a valid elevation map.
                  Every elevation value in elevation_map is unique.

    >>> find_peak(UNIQUE_3X3)
    [1, 0]
    >>> find_peak(UNIQUE_4X4)
    [0, 3]
    ''' 
    peak = [0, 0]
    for i in range(len(elevation_map)):
        for j in range(len(elevation_map)):
            if elevation_map[i][j] > elevation_map[peak[0]][peak[1]]:
                peak.clear()
                peak.append(i)
                peak.append(j)
    return peak
            
            
def is_sink(elevation_map: List[List[int]], cell: List[int]) -> bool:
    '''Return True if and only if cell exists in the elevation_map
    and cell is a sink.

    Precondition: elevation_map is a valid elevation map.
                  cell is a 2-element list.

    >>> is_sink(THREE_BY_THREE, [0, 5])
    False
    >>> is_sink(THREE_BY_THREE, [0, 2])
    True
    >>> is_sink(THREE_BY_THREE, [1, 1])
    False
    >>> is_sink(FOUR_BY_FOUR, [2, 3])
    True
    >>> is_sink(FOUR_BY_FOUR, [3, 2])
    True
    >>> is_sink(FOUR_BY_FOUR, [1, 3])
    False
    '''
    sink = True
    if cell[0] > len(elevation_map):
        return False
    if cell[1] > len(elevation_map):
        return False
    for i in range(len(elevation_map)):
        for j in range(len(elevation_map)):
        
            if cell[0] == len(elevation_map) - 1 and cell[1] == len(elevation_map) - 1:
                if elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] - 1][cell[1] - 1] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] - 1][cell[1]] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0]][cell[1] - 1]:
                    sink = False
            elif cell[0] == 0 and cell[1] == 0:
                if elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] + 1][cell[1] + 1] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] + 1][cell[1]] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0]][cell[1] + 1]:
                    sink = False   
            elif cell[0] == (len(elevation_map) - 1):
                if elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] - 1][cell[1] - 1] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] - 1][cell[1]] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] - 1][cell[1] + 1] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0]][cell[1] - 1] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0]][cell[1] + 1]:
                    sink = False
            elif cell[0] == 0:
                if elevation_map[cell[0]][cell[1]] > elevation_map[cell[0]][cell[1] - 1] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0]][cell[1] + 1] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] + 1][cell[1] - 1] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] + 1][cell[1]] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] + 1][cell[1] + 1]:
                    sink = False      
            elif cell[1] == (len(elevation_map) - 1):
                if elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] - 1][cell[1] - 1] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] - 1][cell[1]] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0]][cell[1] - 1] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] + 1][cell[1] - 1] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] + 1][cell[1]]:
                    sink = False
            elif cell[1] == 0:
                if elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] - 1][cell[1]] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] - 1][cell[1] + 1] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0]][cell[1] + 1] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] + 1][cell[1]] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] + 1][cell[1] + 1]:
                    sink = False
            else:
                if elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] - 1][cell[1] - 1] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] - 1][cell[1]] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] - 1][cell[1] + 1] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0]][cell[1] - 1] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0]][cell[1] + 1] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] + 1][cell[1] - 1] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] + 1][cell[1]] or elevation_map[cell[0]][cell[1]] > elevation_map[cell[0] + 1][cell[1] + 1]:
                    sink = False
    return sink

def find_local_sink(elevation_map: List[List[int]],
                    cell: List[int]) -> List[int]:
    '''Return the local sink of cell cell in elevation_map.

    Precondition: elevation_map is a valid elevation map.
                  elevation_map contains no duplicate elevation values.
                  cell is a valid cell in elevation_map.

    >>> find_local_sink(UNIQUE_3X3, [1, 1])
    [0, 0]
    >>> find_local_sink(UNIQUE_3X3, [2, 0])
    [2, 0]
    >>> find_local_sink(UNIQUE_4X4, [1, 3])
    [0, 2]
    >>> find_local_sink(UNIQUE_4X4, [2, 2])
    [2, 1]
    '''
    small = 9090919019019
    row_map_up = cell[0] - 1
    row_map_down = cell[0] + 1
    column_map_up = cell[1] - 1
    column_map_down = cell[1] + 1
    if cell[0] == 0:
        row_map_up = 0
    if cell[0] == len(elevation_map) - 1:
        row_map_down = len(elevation_map) - 1
    if cell[1] == 0:
        column_map_up = 0
    if cell[1] == len(elevation_map) - 1:
        column_map_down = len(elevation_map) - 1

    for i in range(row_map_up, row_map_down + 1):
        for j in range(column_map_up, column_map_down + 1):
            if elevation_map[i][j] < small:
                small = elevation_map[i][j]
                is_sink = [i, j]
    return is_sink
   
def can_hike_to(elevation_map: List[List[int]], start: List[int],
                dest: List[int], supplies: int) -> bool:
    '''Return True if and only if a hiker can move from start to dest in
    elevation_map without running out of supplies.

    Precondition: elevation_map is a valid elevation map.
                  start and dest are valid cells in elevation_map.
                  dest is North-West of start.
                  supplies >= 0

    >>> map = [[1, 6, 5, 6],
    ...        [2, 5, 6, 8],
    ...        [7, 2, 8, 1],
    ...        [4, 4, 7, 3]]
    >>> can_hike_to(map, [3, 3], [2, 2], 10)
    True
    >>> can_hike_to(map, [3, 3], [2, 2], 8)
    False
    >>> can_hike_to(map, [3, 3], [3, 0], 7)
    True
    >>> can_hike_to(map, [3, 3], [3, 0], 6)
    False
    >>> can_hike_to(map, [3, 3], [0, 0], 18)
    True
    >>> can_hike_to(map, [3, 3], [0, 0], 17)
    False
    '''
    curr_pos = start
    supplies_left = supplies

    is_row = False
    is_column = False 

    while curr_pos != dest:
        if curr_pos[0] == dest[0]:
            is_row = True
        elif curr_pos[1] == dest[1]:
            is_column = True

        if (abs(elevation_map[curr_pos[0]][curr_pos[1]] -
                elevation_map[curr_pos[0] - 1][curr_pos[1]]) <=
            abs(elevation_map[curr_pos[0]][curr_pos[1]] -
                elevation_map[curr_pos[0]][curr_pos[1] - 1]) and not is_row):
            supplies_left -= abs(elevation_map[curr_pos[0]][curr_pos[1]] -
                elevation_map[curr_pos[0] - 1][curr_pos[1]]) 
            curr_pos[0] = curr_pos[0] - 1
            

        elif not is_column:
    
            supplies_left -= abs(elevation_map[curr_pos[0]][curr_pos[1]] -
                elevation_map[curr_pos[0]][curr_pos[1] - 1])
            curr_pos[1] = curr_pos[1] - 1

        if supplies_left < 0:
            return False

    return True

     

def get_lower_resolution(elevation_map: List[List[int]]) -> List[List[int]]:
    '''Return a new elevation map, which is constructed from the values
    of elevation_map by decreasing the number of points within it.

    Precondition: elevation_map is a valid elevation map.

    >>> get_lower_resolution(
    ...     [[1, 6, 5, 6],
    ...      [2, 5, 6, 8],
    ...      [7, 2, 8, 1],
    ...      [4, 4, 7, 3]])
    [[3, 6], [4, 4]]
    >>> get_lower_resolution(
    ...     [[7, 9, 1],
    ...      [4, 2, 1],
    ...      [3, 2, 3]])
    [[5, 1], [2, 3]]
    '''
    return elevation_map
