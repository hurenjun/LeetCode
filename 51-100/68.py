class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        answer, tmp, length = [], [], 0
        for word in words:
            if length + len(tmp) + len(word) <= maxWidth:
                tmp.append(word)
                length += len(word)
            else:
                # print the current line
                if len(tmp) == 1:
                    space = [maxWidth - length]
                else:
                    base = (maxWidth - length) // (len(tmp) - 1)
                    space = [base] * (len(tmp) - 1) + [0]
                    for i in range(maxWidth - length - base * (len(tmp) - 1)):
                        space[i] += 1
                line = ''
                for i in range(len(tmp)):
                    line = line + tmp[i] + ' ' * space[i]
                answer.append(line)
                tmp, length = [word], len(word)
        line = ''
        for i in range(len(tmp)):
            line = line + tmp[i]
            if i < len(tmp) - 1:
                line += ' '
        line += ' ' * (maxWidth - len(line))
        answer.append(line)
        return answer
        
    
s = Solution()
answer = s.fullJustify(["Science"], 20)  
for line in answer:
    print(line)