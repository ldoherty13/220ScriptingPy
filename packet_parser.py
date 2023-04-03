import re

node_list1 = []
node_list2 = []
node_list3 = []
node_list4 = []


# Takes txt file with filtered ICMP packets, splits the packets, and puts them into a list
def read_data(filename):
	with open(filename, 'r') as packet_list:
		packets = packet_list.read()
	l = packets.split('No.     Time           Source                Destination           Protocol Length Info')
	del l[0]
	return l


# Packet class. Instance of class stores info about individual packets. Also includes methods to return those attributes.
class packet:
	def __init__(self, time, source, destination, length, type, info):
		self.packet_time = time
		self.packet_source = source
		self.packet_dest = destination
		self.packet_length = length
		self.packet_type = type
		self.packet_info = info

	def display_time(self):
		return self.packet_time

	def display_source(self):
		return self.packet_source

	def display_dest(self):
		return self.packet_dest

	def display_length(self):
		return self.packet_length

	def display_type(self):
		return self.packet_type

	def display_info(self):
		return self.packet_info


# Splits each packet into its fields and adds important info to a packet class object
def parse_list(l, nodelist):
	i = 0
	for packet_data in l:
		fields = re.split(r'\s{2,}', l[i])
		time = fields[1].split(' ')
		nodelist.append(packet(time[1], fields[2], fields[3],fields[5], fields[6], fields[7]))
		i = i+1


def parse():
	print('called parse function in packet_parser.py')

	parse_list(read_data('Node1_filtered.txt'), node_list1)
	parse_list(read_data('Node2_filtered.txt'), node_list2)
	parse_list(read_data('Node3_filtered.txt'), node_list3)
	parse_list(read_data('Node4_filtered.txt'), node_list4)
