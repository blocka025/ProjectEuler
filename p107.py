import numpy as np
import copy

f = open("C:/Users/blake/Documents/VSCode/Python/ProjectEuler/p107_network.txt", "r")
networks = []
for line in f:
    networks.append(line.strip().split(","))
f.close()


full_nodes =[]
total = 0
# tot = 0
for i,node in enumerate(networks):
    full_nodes.append({})
    for j, val in enumerate(node):
        if val != '-':
            full_nodes[i][j] = int(val)
            total += int(val)
            
ms = []
for node in full_nodes:
    ms.append(len(node))
my = np.argmin(ms)

def has_loops(pos, used, maxim=(0,0,0)):
    og_node_count = len(used)
    for node in (nodes := curr_nodes[pos]):
        if node == used[0] and len(used)>2 and len(nodes)!=1: #this means a loop has been found
            if (m :=nodes[node])>maxim[0]:
                return (False,(m,used[-1],used[0]))
            else:
                return (False,maxim)
        elif not(node in used):
            if len(used)>10+used[0]%my:
                break
            used.append(node)
            if (m :=nodes[node])>maxim[0]:
                a = has_loops(node,copy.deepcopy(used),(m,used[-1],used[-2]))
                if not(a is None):
                    done, max_loop = a
                    if not(done):
                        return (done, max_loop)

            else:
                a = has_loops(node,copy.deepcopy(used),maxim)
                if not(a is None):
                    done, max_loop = a
                    if not(done):
                        return (done, max_loop)
    
        while len(used) != og_node_count:
            used.pop()
    if maxim == (0,0,0):
        return (True,0)
    

curr_nodes = copy.deepcopy(full_nodes)
removed = 0
start = my
inds = list(range(start,len(curr_nodes)))+list(range(0,start))

for pos in inds:
    while len(curr_nodes[pos])>1:
        done, max_loop = has_loops(pos,[pos])
        if done:
            break
        else:
            if len(curr_nodes[max_loop[1]]) >1 and len(curr_nodes[max_loop[2]])>1:
                del curr_nodes[max_loop[1]][max_loop[2]]
                del curr_nodes[max_loop[2]][max_loop[1]]
                removed += 1

new_total = 0
for node in curr_nodes:
    for keys in (nodes := node):
        new_total += nodes[keys]

print(total//2-new_total//2)