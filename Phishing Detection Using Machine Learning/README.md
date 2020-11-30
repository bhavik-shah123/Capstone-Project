## PROPOSED APPROACH TO DETECT PHISHING USING NEURAL NETWORKS
1. Preprocess the information to evacuate any kind of unnecessary data like null
values
2. Use the feature extraction based on the research on phishing URLs and convert
English content to numerical data which is understandable by the computer
3. Find out the general information about the dataset such as the summary and the
number of safe and unsafe rows
4. Partition the newly formed numerical dataset into two distinct sets into training
and testing set
5. Define callback function to monitor loss and adjust learning rates accordingly and
to stop the model once it reaches a certain average accuracy rate
6. Train and test numerous models for various optimizers namely, Adam, RMSProp,
and SGD with 3 hidden layers, two with 512 nodes, and the last one with 256
nodes and Sigmoid activation function
7. Evaluate model to gauge loss and accuracy of the prepared model for all the
optimizers and compare them
8. Train and test again with the same optimizers but now with the first two hidden
layers with 512 nodes only but the last hidden node having 1024 nodes, and
Sigmoid activation function. Loss function in both the cases is “binary
cross-entropy” as it is perfect for binary classification
9. Evaluate and compare the result generated from both the models for the specific
optimizers
10. Finally, enhance the result using Swarm Intelligence/TDLHBA technique
