def common(NodeA,NodeB,sizeA,sizeB):
    check =[]
    chA =[]
    chB =[]
    if sizeA == sizeB:
        for i in range(sizeA):
            if ord(NodeA[i]) == ord(NodeB[i]):
                check.append(NodeA[i])
            elif ord(NodeA[i]) < ord(NodeB[i]):
                chA.append(NodeA[i])
                check.append(NodeA[i])
                break
            elif ord(NodeA[i]) > ord(NodeB[i]):
                chB.append(NodeB[i])
                check.append(NodeB[i])
                break
    elif sizeA < sizeB:
        if sizeA ==1:
            for i in range(sizeA):
                for j in range(sizeA+1):
                    if ord(NodeA[i]) == ord(NodeB[j]):
                        check.append(NodeA[i])
                    elif ord(NodeA[i]) < ord(NodeB[j]):
                        chA.append(NodeA[i])
                        check.append(NodeA[i])
                        break
                    elif ord(NodeA[i]) > ord(NodeB[j]):
                        chB.append(NodeB[j])
                        check.append(NodeB[j])
                        break
        elif sizeA > 1:
            for i in range(sizeA):
                if ord(NodeA[i]) == ord(NodeB[i]):
                    check.append(NodeA[i])
                elif ord(NodeA[i]) < ord(NodeB[i]):
                    chA.append(NodeA[i])
                    check.append(NodeA[i])
                    break
                elif ord(NodeA[i]) > ord(NodeB[i]):
                    chB.append(NodeB[i])
                    check.append(NodeB[i])
                    break
    elif sizeA > sizeB:
        if sizeB == 1:
            for i in range(sizeB):
                for j in range(sizeB + 1):
                    if ord(NodeA[j]) == ord(NodeB[i]):
                        check.append(NodeA[j])
                    elif ord(NodeA[j]) < ord(NodeB[i]):
                        chA.append(NodeA[j])
                        check.append(NodeA[j])
                        break
                    elif ord(NodeA[j]) > ord(NodeB[i]):
                        chB.append(NodeB[i])
                        check.append(NodeB[i])
                        break
        elif sizeB > 1:
            for i in range(sizeB):
                if ord(NodeA[i]) == ord(NodeB[i]):
                    check.append(NodeA[i])
                elif ord(NodeA[i]) < ord(NodeB[i]):
                    chA.append(NodeA[i])
                    check.append(NodeA[i])
                    break
                elif ord(NodeA[i]) > ord(NodeB[i]):
                    chB.append(NodeB[i])
                    check.append(NodeB[i])
                    break
    if len(chA) ==0 and len(chB) ==0 and len(check) !=0:
        return check[0],'A'
    elif len(chA) !=0 and len(chB) ==0 and len(check) !=0:
        return check[0],'A'
    elif len(chA) ==0 and len(chB) !=0 and len(check) !=0:
        return check[0],'B'

def morganAndString(a, b):
    NodeA = a
    NodeB = b
    sizeA = len(NodeA)
    sizeB = len(NodeB)
    result = []
    index = 0
    while index < sizeA or index < sizeB:
        if sizeA != 0 and sizeB != 0:
            if ord(NodeA[index]) > ord(NodeB[index]):
                result.append(NodeB[index])
                NodeB = NodeB[index + 1:]
                sizeB -= 1
            elif ord(NodeA[index]) < ord(NodeB[index]):
                result.append(NodeA[index])
                NodeA = NodeA[index + 1:]
                sizeA -= 1
            elif ord(NodeA[index]) == ord(NodeB[index]):
                ans,cls=common(NodeA,NodeB,sizeA,sizeB)
                if cls =='A':
                    if ans == NodeA[index]:
                        result.append(NodeA[index])
                        NodeA = NodeA[index + 1:]
                        sizeA -= 1
                elif cls =='B':
                    if ans == NodeB[index]:
                        result.append(NodeB[index])
                        NodeB = NodeB[index + 1:]
                        sizeB-=1

        elif sizeA != 0 and sizeB == 0:
            result.append(NodeA)
            sizeA = sizeA - len(NodeA)
        elif sizeA == 0 and sizeB != 0:
            result.append(NodeB)
            sizeB = sizeB - len(NodeB)
    if index == sizeA and index == sizeB:
        if len(result) == 0:
            return 0
        else:
            return ''.join([i for i in result if i != ' ' ])

t = int(input())
for t_itr in range(t):
    a = input()
    b = input()
    result = morganAndString(a, b)
    ch= input()
    if result==ch:
        print("yes")
        print(result)
    else:
        print("FALSE")
        print(result)







