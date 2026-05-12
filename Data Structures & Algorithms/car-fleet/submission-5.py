class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        for i in range(len(position)):
            pos_speed.append([position[i], speed[i]])
        
        pos_speed.sort(reverse = True)
        print(pos_speed)
        stack = []
        for i in range(len(pos_speed)):
            pos, speed = pos_speed[i]
            t = (target - pos)/speed
            if not stack:
                stack.append(t)
            else:
                print(stack[-1],t)
                if stack[-1] >= t:
                    continue
                else:
                    stack.append(t)
        print(stack)
        return len(stack)