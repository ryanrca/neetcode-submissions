import re
class Solution:
    def __init__(self):
        # self.delimiter = "\x1f"
        self.delimiter = "|"
        self.escaped_del = re.escape(self.delimiter)

    def encode(self, strs: List[str]) -> str:

        if strs == [""]: 
            return "" 
        if len(strs) == 0:
            return "empty"

        ret = ""

        # pattern: <number of chars><delimiter><chars>...
        # ex: 5|xxxxx3|ooo7|qqqqqqq
        for i in strs:
            ret += f"{len(i)}{self.delimiter}{i}"

        return ret


    def decode(self, s: str) -> List[str]:

        if s == "":
            return [""] 
        if s == "empty":
            return []

        ret = []

        pattern = re.compile(rf"^(\d+?){self.escaped_del}(.*)$", re.DOTALL)

        while s:
            match = pattern.match(s)

            if not match:
                break

            else:
                length = int(match.group(1))
                the_rest = match.group(2)

                word = the_rest[0:length]
                ret.append(word)

                s = the_rest[length:]

        return ret
