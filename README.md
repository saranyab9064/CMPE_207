# Load Balancer using Ryu Controller

**Course:** CMPE 210 SDN & NFV
Routing algorithm is used to find all possible paths from source to destination in a network topology. By finding the two shortest path routes to a destination, it is possible to distribute the traffic fairly through that shortest paths. In this way we can achieve the efficiency of network utility.


## Install Requirements
```
sudo apt-get install mininet
sudo pip install ryu
Download miniedit (https://raw.githubusercontent.com/mininet/mininet/master/examples/miniedit.py)
```
## Run Application
In your terminal, run the following:
```
# open controller terminal
ryu-manager --observe-links ryu_bfs.py

# open mininet console
sudo python final_topo.py
```


## Bugs
```
1. ryu_bfs module not found error - Try to compile the python file and then run ryu-manager
2. If you get links are already exists error  try to use "sudo mn -c " and then create a topology on mininet console
3. If the tcpdump is not capturing ICMP packet, try to kill all the tasks and restart again by rerunning the ping request
4. If you get any error on the ryu-controller try to reinstall ryu on VM
```


## Error Handling
```
Try to give maximum path value > or = 1
```
Make sure to give the commands correctly 

