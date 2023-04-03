# Reads txt files and splits the packets and puts them into a list
def read_data(filename):
	with open(filename, 'r') as packet_list:
		packets = packet_list.read()
	l = packets.split('No.     Time           Source                Destination           Protocol Length Info')
	return l


# Takes packet list and filters out all non ICMP packets
def filter_packets(node):
	filtered = []
	for packet in node:
		if 'ICMP' in packet:
			packet = 'No.     Time           Source                Destination           Protocol Length Info' + packet
			filtered.append(packet)
	return filtered


# Takes filtered list and writes all ICMP packets to a new file
def write_filtered(filteredlist, filteredfilename):
	filtered_string = ''.join(filteredlist)
	with open(filteredfilename, 'w') as filterfile:
		filterfile.writelines(filtered_string)


def filter():
	write_filtered(filter_packets(read_data('Node1.txt')), 'Node1_filtered.txt')
	write_filtered(filter_packets(read_data('Node2.txt')), 'Node2_filtered.txt')
	write_filtered(filter_packets(read_data('Node3.txt')), 'Node3_filtered.txt')
	write_filtered(filter_packets(read_data('Node4.txt')), 'Node4_filtered.txt')

	print('called filter function in filter_packets.py')
