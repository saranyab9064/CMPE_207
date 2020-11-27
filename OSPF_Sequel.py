import matplotlib
import networkx
from easysnmp import Session
from pprint import pprint

#Asking the user for input
ip = input("\nEnter the 'root' device IP address: ")

#List of OSPF devices
ospf = []

#Discovering OSPF neighbors for the root device
def ospf_func(ip):
    #Creating empty containers for adding discovered devices
    nbridlist = []
    nbriplist = []
    ospf_device = {}

    #Opening the SNMPv3 session to the device
    session = Session(hostname = ip, version = 3, security_level = "auth_with_privacy", security_username = "mihai", auth_protocol = "SHA", auth_password = "shapass1234", privacy_protocol = "AES", privacy_password = "aespass1234")

    #Getting device OSPF ID
    snmp_walk = session.walk('.1.3.6.1.2.1.14.1.1')
    #pprint(snmp_walk)
    ospf_host_id = snmp_walk[0].value

    #Performing SNMP WALK to get OSPF neighbor IDs
    snmp_walk = session.walk('.1.3.6.1.2.1.14.10.1.3')
    #pprint(snmp_walk)

    for neighbor_id in snmp_walk:
        nbridlist.append(neighbor_id.value)

    #Performing SNMP WALK to get OSPF neighbor IPs
    snmp_walk = session.walk('.1.3.6.1.2.1.14.10.1.1')
    #pprint(snmp_walk)

    for neighbor_ip in snmp_walk:
        nbriplist.append(neighbor_ip.value)

    #Building the dictionary with the device's OSPF info
    ospf_device["HostID"] = ospf_host_id
    ospf_device["NbrRtrID"] = nbridlist
    ospf_device["NbrRtrIP"] = nbriplist
    #pprint(ospf_device)

    #List of OSPF devices
    if ospf_device not in ospf:
        ospf.append(ospf_device)

    return ospf

#Calling the function above
ospf = ospf_func(ip)
#pprint(ospf)

#Querying neighbors to find other OSPF routers (if any)
def neighbor_query():
    #All queried OSPF routers (by ID)
    all_rtr_ids = []

    for router in range(len(ospf)):
        rtr_id = ospf[router]["HostID"]
        all_rtr_ids.append(rtr_id)

    #pprint(all_rtr_ids)

    #All discovered neighbor OSPF router IDs
    all_nbr_ids = []

    for router in range(len(ospf)):
        for nbr_id in ospf[router]["NbrRtrID"]:
            all_nbr_ids.append(nbr_id)

    #pprint(all_nbr_ids)

    #All unqueried OSPF routers (by ID)
    all_unqueried = []
    for nbr_id in all_nbr_ids:
        if nbr_id not in all_rtr_ids:
            all_unqueried.append(nbr_id)

    #pprint(all_unqueried)
    #print("\n\n")

    #Running the ospf_func() function for each unqueried neighbor (by IP)
    for q in all_unqueried:
        for r in range(len(ospf)):
            for index, s in enumerate(ospf[r]["NbrRtrID"]):
                if q == s:
                    new_ip_to_query = ospf[r]["NbrRtrIP"][index]
                    ospf_func(new_ip_to_query)
                else:
                    pass
    #pprint(ospf)

    all_devices = []

    for device in ospf:
        if device not in all_devices:
            all_devices.append(device)

    return all_rtr_ids, all_nbr_ids, all_devices

#Calling the neighbor_query() function
while True:
    neighbor_query()
    if len(list(set(neighbor_query()[0]))) == len(list(set(neighbor_query()[1]))):
        break

final_devices_list = neighbor_query()[2]
#pprint(final_devices_list)

#Creating a dictionary of neighborships
neighborship_dict = {}

for each_dictionary in final_devices_list:
    for index, each_neighbor in enumerate(each_dictionary["NbrRtrID"]):
        each_tuple = (each_dictionary["HostID"], each_neighbor)
        neighborship_dict[each_tuple] = each_dictionary["NbrRtrIP"][index]

#pprint(neighborship_dict)

#Generating the OSPF graph
print("\nGenerating OSPF network topology...\n")

#Drawing the topology using the dictionary of neighborships
G = networkx.Graph()

G.add_edges_from(neighborship_dict.keys())

pos = networkx.spring_layout(G, k = 0.1, iterations = 70)

networkx.draw_networkx_labels(G, pos, font_size = 9, font_family = "sans-serif", font_weight = "bold")

networkx.draw_networkx_edges(G, pos, width = 4, alpha = 0.4, edge_color = 'black')

networkx.draw_networkx_edge_labels(G, pos, neighborship_dict, label_pos = 0.3, font_size = 6)

networkx.draw(G, pos, node_size = 700, with_labels = False)

matplotlib.pyplot.show()

#End of program
