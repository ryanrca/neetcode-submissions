class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort positions from first to last descending
        # calculate time to reach destination
        # push first on stack
        # if next car reaches destination  BEFORE previous car, they become a fleet
        # else, a new fleet is created
        # at bottom of list of cars, unwind stack
        # return length of stack

        # space: sorted array of tuples, stack = O(3n) = O(n)

        tup_arry = []

        for i in range(len(position)):
            # (position, speed, time to reach dest)
            ta = (position[i], speed[i], (target - position[i]) / speed[i])
            tup_arry.append(ta)
            
        # sort by position: 
        tup_arry.sort(reverse=True)

        # push onto fleet_stack
        fleet_stack = []
        if not tup_arry: 
            return 0
        fleet_stack.append(tup_arry[0])
        for i in range(1, len(tup_arry)):

            p, s, t = tup_arry[i]
            cur_pos, cur_speed, cur_time = fleet_stack[len(fleet_stack) - 1]

            if t > cur_time:
                fleet_stack.append(tup_arry[i])
        
        return len(fleet_stack)
        