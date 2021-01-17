# from mr_pagerank_dangling_nodes import PageRankReDistribute
from mr_pagerank import PageRank

if __name__ == '__main__':
    input_file = 'preprocessed_web-Google.txt'
    output_dir = 'output_graph_{}/'

    iteration = 0
    running = True

    with open(input_file,'r') as f:
        graph_size = len(f.read().split('\n')) - 1
        print(graph_size)
    
  
    # lost_pagerank = 0
    while running:
        print('Running iteration {}'.format(iteration + 1))
        # A switch to determine whether to read the initial input graph
        # or one of our iteration folders
        if iteration == 0:
            job = PageRank([input_file,
                         '--output-dir=' + output_dir.format(iteration)])
            # job_redistribute = PageRankReDistribute([output_dir.format(iteration - 1) + '*',
            #                              '--output-dir=' + output_dir.format(iteration),'--graph-size', str(graph_size)])
        else:
            job = PageRank([output_dir.format(iteration - 1) + '*', '--output-dir=' + output_dir.format(iteration)])    
            # job_redistribute = PageRankReDistribute([output_dir.format(iteration - 1) + '*',
            #              '--output-dir=' + output_dir.format(iteration),'--graph-size', str(graph_size)])
        #lost_pagerank = 0
        # With block to construct a job
        with job.make_runner() as runner:
            # Run the job
            runner.run()

            # Collect the unconverged_node_count that we issue in an iteration
            unconverged_node_count = 0
            
            for val in runner.counters():
                try:
                    unconverged_node_count += val['nodes']['unconverged_node_count']
                    
                except KeyError:
                    pass

                # try: 
                #     lost_pagerank += val['nodes']['lost_pagerank']
                # except KeyError:
                #     pass

            print(unconverged_node_count,"unconverged_node_count")
            #print(lost_pagerank,"lost_pagerank")

            # Keep running there are unconverged nodes
            running = unconverged_node_count > 0

        iteration += 1