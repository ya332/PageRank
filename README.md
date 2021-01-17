### Requirements ###
Python 3.x
mrjob==0.6.9


### Included Files ###

* mr_pagerank.py (For the first implementation of the pagerank algorithm. We dont handle the random jump factor and the dangling node case)
* preprocess.py (Takes the input and makes it ready to be parsed by MapReduce framework)
* README.md
* sample_input.txt (small testing dataset)
* preprocessed_sample_input.txt(output of the preprocess.py when I ran it on the sample_input.txt)
* web-Google.txt(A very large dataset with 739454 unique nodes)


### Instructions ###

### To run the Python files:
`$ python driver.py`
By default I am running the small dataset, because the web-Google.txt takes at least a day to run on i-5, 1.9 GHz, 16 GB RAM. 

Any additional dataset should be in the format of the sample_input.txt. 
When this command runs,
`$ python preprocess.py <file_name goes here>`
preprocessed_input.txt will be generated.(It attaches the word preprocessed to the beginning of the input filename) We then read this file in the driver.py file, and calculate the pagerank values based on our implementation.


When preprocess.py is ran, the output format of the processed file should be like this:

\# node id | [Adjacency list, initial pagerank value]

For instance, this is a snippet of the preprocessed_web-Google.txt,which is the 

`$ 565424	[[2, 30957, 357310, 423174, 430119, 462435, 472889], 1.3523491657357996e-06]`\
`581609	[[2, 30957, 357310, 423174, 430119, 462435, 644135, 858904, 908276],1.3523491657357996e-06]`\
`597621	[[2937, 89958, 679, 727948, 729403, 769429, 783319, 857417, 888289, 8978], 1.3523491657357996e-06]`\
`644135	[[2, 10245, 30957, 136144, 357310, 396205, 423174, 430119, 462435],1.3523491657357996e-06]`
