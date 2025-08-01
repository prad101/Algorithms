"""
                ----- PSEUDOCODE FOR SKYLINE ALGORITHM -----
FUNCTION SKYLINE_DIVIDE(buildings):

To convert (h, lxi, rxi) values to (h, lxi), (0, rxi) and divide the list based on midpoint value recursively

    IF buildings.size is empty:
        RETURN empty list
    
    # to set values as (h, lxi), (0, rxi) whenever a single building encounter (used recu)
    IF buildings.size == 1:
        GET h, lxi ,rxi from buildings
        RETURN [(h, lxi), (0, rxi)]
    
    midpoint = buildings.size / 2

    # recursively divide values to left and right
    left = SKYLINE_DIVIDE(buildings[0 to midpoint])
    right = SKYLINE_DIVIDE(buildings[midpoint to end])

    # process the logic and merge results accordingly
    outlines = CALL SKYLINE_MERGE(left, right)

    RETURN outlines

FUNCTION SKYLINE_MERGE(left, right):

Gets left(h, x), right(h,x) values from SKYLINE_DIVIDE and the final (h,x) values are considered based on conditions, 
1. Selecting x (start/end horizontal point) and y (height) values based on lowest x value upon comparing from both left and right sets
2. Adding final values based on, a. if result set is empty or b. if current y value differs from y_max. 
3. The final part involves adding remaining values of left and right to the final result based on condition (2)


    INITIALIZE result to have (h, x) values.
    INITIALIZE i to 0.
    INITIALIZE j to 0.
    INITIALIZE left_yh to 0
    INITIALIZE right_yh to 0
    

    To start the loop over the elements of left and right lists
    WHILE i < left.size AND j < right.size:

        IF x from left < x from right THEN 
            Consider values from left,
            SET x = x
            SET left_yh = y
            INCREMENT i

        ELSE IF x from right < x from left THEN 
            Consider values from right,
            SET x = x
            SET right_yh = y
            INCREMENT j
        
        ELSE 
            To handle overlapping x-coordinates
            SET x = x from left
            SET left_yh = y from left
            SET right_yh = y from right
            INCREMENT i
            INCREMENT j
        
        GET MAX(left_yh, right_yh), SET as ymax

        IF result not empty OR y value has changed:
            ADD (ymax, x) to result

    To check and add remaining values from left set        
    WHILE i < left.size
        IF result not empty OR y value has changed:
            ADD (y, x) to result
        INCREMENT i

    To check and add remaining values from right set        
    WHILE i < right.size
        IF result not empty OR y value has changed:
            ADD (y, x) to result
        INCREMENT j

    RETURN result

                --------------------------------------------------------
"""

from pathlib import Path

ROOT = Path.cwd()

class Skyline:
    def __init__(self):
        pass

    
    def process_input_from_file(self, file_path):

        buildings = []
        clear_list = False

        #to read .csv or .txt file and build each row value as a tuple
        try:
            with open(file_path, mode='r') as file:
                for row in file:           
                    h, left, right = map(int, row.strip().split(','))
                    if right > left >= 0:
                        buildings.append((h, left, right))
                    else:
                        clear_list = True
                        print("Input error: Please enter coordinates as per inequality of, (0 <= Lxi < Rxi)")

            if clear_list:
                buildings.clear()
            
        except ValueError:
            print("Value error: Please enter coordinates as per order, (h, Lxi, Rxi) for every new line")

        return buildings
    
    def skyline_merge(self, left, right):

        result = []
        i = 0
        j = 0 
        left_yh = 0
        right_yh = 0

        n_left = len(left)
        n_right = len(right)

        # iterating over left and right set in parallel
        while i < n_left and j < n_right:

            x1 = left[i][1]
            x2 = right[j][1]

            # to consider values from left
            if x1 < x2:
                x = x1
                left_yh = left[i][0]
                i+= 1
            
            # to consider values from right
            elif x2 < x1:
                x = x2
                right_yh = right[j][0]
                j+=1

            # to handle the overlapping x-coordinates
            else:
                x = x1
                left_yh = left[i][0]
                right_yh = right[j][0]
                i+=1
                j+=1
            
            ymax = max(left_yh, right_yh)

            # add coordinates if result set is empty or if y value changes
            if not result or result[-1][0] != ymax:
                result.append((ymax, x))

        # check and add remaining values from left set
        while i < n_left:
            
            if not result or result[-1][0] != left[i][0]:
                result.append(left[i])

            i+=1

        # check and add remaining values from right set
        while j < n_right:

            if not result or result[-1][0] != right[j][0]:
                result.append(right[j])
            
            j+=1     


        return result
    

    def skyline_divide(self, buildings):

        # return empty list if no buildings
        if len(buildings) == 0:
            print("No buildings found")
            return []

        building_len = len(buildings)
        # build tuple as (height, left), (0, right) when there's only 1 building in the set
        if building_len == 1:
            height, left, right = buildings[0]
            return [(height, left), (0, right)]

        # calculate mid value
        mid = building_len // 2
        left_skyline = self.skyline_divide(buildings[:mid])
        right_skyline = self.skyline_divide(buildings[mid:])
        
        # merge the left and right results based on the skyline_merge logic
        merged_result = self.skyline_merge(left_skyline, right_skyline)
        return merged_result


if __name__ == "__main__":

    result_list = []
    # change number below accordingly to run over predefined samples
    file_num_suffix = '_e1'

    # change file path below for custom file
    input_path = f"InputsOutputs/Input{file_num_suffix}.txt"
    output_path = f"InputsOutputs/Output{file_num_suffix}.txt"

    skyline_obj = Skyline()

    # buildings = [(3, 1, 5), (5, 1, 5), (4, 1, 5)]
    buildings = skyline_obj.process_input_from_file(input_path)
    outline_list = skyline_obj.skyline_divide(buildings)
    print(f"""Input: {buildings}\nOutput: {outline_list}""")

    #save the results as .txt
    if outline_list:
        with open(output_path, "w") as op:
            for tuple in outline_list:
                op.write(f"{tuple[0]}, {tuple[1]}\n")
    
        op.close()