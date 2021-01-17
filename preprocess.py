from mrjob.protocol import JSONProtocol
import math
import re,os
if __name__ == '__main__':

    NUMBER_RE = re.compile(r"[-?\d']+")
    input_file = 'sample_input.txt'
    with open(input_file, 'r') as out_file:
        data = [x.split() for x in out_file.read().splitlines()]

    # print(data)
    nodes = {}
    for line in data:
        nodes[int(line[0])] = [] #Will be written as null

        
    for line in data:
        #Check for dangling nodes
        if line[1:] == []:
            nodes[int(line[0])] = [] #Will be written as null
        else:
            nodes[int(line[0])].append(int(line[1:][0]))
    # print('nodes',nodes)
    # unique_nodes = sorted(set(nodes), key = lambda ele: nodes.count(ele)) 
    # print(nodes)    
    # print(unique_nodes)
    unique_node_count = len(nodes.keys()) 
    initial_pagerank = 1 / unique_node_count
    

    j = JSONProtocol()

    with open("preprocessed_" + input_file,"wb+") as out_file:
        j = JSONProtocol()
        for _id, adj in nodes.items():
            out_file.write(j.write(_id, (adj, initial_pagerank)))
            out_file.write('\n'.encode('utf-8'))    

    