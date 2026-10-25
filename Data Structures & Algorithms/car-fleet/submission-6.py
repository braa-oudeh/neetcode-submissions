##### MAIN NOTE: MY BIGGEST PROBLEM HERE WAS THE COUNTER INCREMENTATION, I WAS ALWAYS OFF AND DIDN'T KNOW HOW TO DO THE COUNTER CORRECTLY
##### HOW IS IT RELEVANT FOR OTHER PROBLEMS? 

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we sort off the position first, if they are the same we sort off based of the speed
        # because even if the previous position needs less time to get to the target, we can't overtake or collide with cars after us
            positions = [(p, s) for p, s in zip(position, speed)]
            positions_sorted_desc = sorted(positions)[::-1]  # Sort by position, then reverse

            stack = []  # Store (position, time_to_target)

            for pos, spd in positions_sorted_desc:
                time_to_target = (target - pos) / spd
                stack.append(time_to_target)
                if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                    stack.pop()
            return len(stack)

        