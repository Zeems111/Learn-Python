import math

def tj(L, W):
    def p(i, j):
    #Penalty for a line consisting of words[i:j]
        length = sum(len(W[k]) for k in range(i, j))
        length += j - i - 1
        if length > L:
            return math.inf
        return (L - length) ** 3

    def tjp(n):
        #target penalty for line split of words [0:i]
        tbl = [math.inf] * (n+1)
        split = [0] * (n+1)
        tbl[0] = 0
        for i in range(1, n+1):
            length = -1
            for j in range(i-1, -1, -1):

                length += 1 + len(W[j])
                P = math.inf if length > L else (L-length)**3
                P = 0 if i == n and P < math.inf else P
                #print(i, j, W[j:i], P)
                if P + tbl[j] <= tbl[i]:
                    tbl[i] = P + tbl[j]
                    split[i] = j
        #print(tbl, sep='\n')
        #print(split)
        #print(tbl[n])
        #return tbl[n]

        result = []
        last = n
        while last > 0:
            result.append(W[split[last] : last])
            last = split[last]
        return result[::-1]

    text = tjp(len(W))
    result = []
    for line in text:
        tmp = line[0]
        for i in range(1, len(line)):
            tmp += ' ' + line[i]
        result.append(tmp)

    tmp = result[0]
    for i in range(1, len(result)):
        tmp += "\n" + result[i]
    result = tmp

    return result


if __name__ == '__main__':
    L = 15
    W = "jars jaws joke jury juxtaposition".split()
    print(tj(L, W))
    print()
    L = 10
    W = ["jars", "jaws", "joke", "jury", "кoke"]
    print(tj(L, W))
