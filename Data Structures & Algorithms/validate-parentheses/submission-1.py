class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for c in s:
            # opening parens get pushed:
            if c in ['(', '{', '[']:
                stack.append(c)

            # closing get poped and checked
            if c in [')', '}', ']']:

                # stack not symetrical
                if len(stack) < 1:
                    return False

                open = stack.pop()
                if open == '(' and c == ')':
                    continue
            
                if open == '{' and c == '}':
                    continue
        
                if open == '[' and c == ']':
                    continue

                # No match, we have a mis-matched pair
                return False
        if len(stack) > 0:
            return False
        return True
