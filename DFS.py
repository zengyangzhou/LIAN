graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]]
from collections import defaultdict
dic = defaultdict(list)
for g in graph:
    dic[g[0]].append(g[1])
#print(math.sqrt(25)==int(math.sqrt(25)))
graph = dic
#print(graph)
def DFS(graph,s):#图  s指的是开始结点
    '''
    从s点开始走，把能达到的点，去重复的记录下来，然后又依次看这些点又能到哪些点，以此类推，得到他会经过的所有点的stack，但是只保存不重复
    的点，实现方法为看这个点是否在seen中，不在就记录，在就跳过

    '''
    #需要一个队列
    stack=[]
    stack.append(s)
    seen=set()#看是否访问过
    seen.add(s)
    res = []
    while (len(stack)>0):
        #拿出邻接点
        vertex=stack.pop(0)#这里pop参数没有0了，pop最后一个元素
        print('vertex:', vertex)
        #print('stack:',stack)
        nodes=graph[vertex]
        for w in nodes:
            if w not in seen:#如何判断是否访问过，使用一个数组
                stack.append(w)
                print('stack:', stack)
                seen.add(w)
                #print('stack:',stack)
                print('seen:',seen)
                print('-----')
        res.append(vertex)
    print('can reach:',seen)
