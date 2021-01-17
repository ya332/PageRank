from mrjob.job import MRJob
from mrjob.job import MRStep
from mrjob.protocol import JSONProtocol
import time,re, os, ntpath, math

 #PageRank Algorithm

class PageRank(MRJob):
    # def configure_args(self):
    #     super(PageRank,self).configure_args()

    #     self.add_passthru_arg('--graph_size',dest='graph_size',type=int, help='')
    
    INPUT_PROTOCOL = JSONProtocol
    def mapper(self, nid, node):
        # Unpack the values of the node
        adjacency_list, pagerank = node
        p = pagerank / len(adjacency_list)

        # Yield the node, labelled for the reducer
        yield nid, ('node', node)

        # Iterate through the adjacency list,
        for adj in adjacency_list:
            yield adj, ('pagerank', p)

    def reducer(self, nid, values):
        # Initialize sum and node
        cur_sum = 0
        node = ('node', [], cur_sum)

        for val in values:
            # Unpack the content of a value
            label, content = val

            # If it's a node, save the node
            if label == 'node':
                node = content
                previous_pagerank = content[1]

            # If it's a pagerank, store the pagerank
            # We will sum the pagerank values
            elif label == 'pagerank':
                cur_sum += content
                previous_pagerank = content

        # Bundle the adjacency list and the pagerank value
        node = (node[0], cur_sum)

        # Increment the unconverged node count (which is the number of updated nodes)
        if abs(cur_sum - previous_pagerank) > 1e-9:
            self.increment_counter('nodes', 'unconverged_node_count', 1)

        # Return just the node
        yield nid, node
               
if __name__ == '__main__':
    start = time.time()
    PageRank.run()
    end = time.time()
    print(round(end-start,5),"seconds completed")


"""
class Mapper
2: method Map(nid n, node N)
3:    p ← N.PageRank/|N.AdjacencyList|
4:    Emit(nid n, N) . Pass along graph structure
5:  for all nodeid m ∈ N.AdjacencyList do
6:    Emit(nid m, p) . Pass PageRank mass to neighbors
1: class Reducer
2: method Reduce(nid m, [p1, p2, . . .])
3:      M ← ∅
4: for all p ∈ counts [p1, p2, . . .] do
5: if IsNode(p) then
6: M ← p . Recover graph structure
7: else
8: s ← s + p . Sum incoming PageRank contributions
9: M.PageRank ← s
10: Emit(nid m, node M)
"""