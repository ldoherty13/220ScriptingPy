from filter_packets import *
from packet_parser import *


# Calculates metrics
def data_size_calc(node_list, source_ip):
	# All variable used to calculate metrics
	i = 0
	sent_request_num = 0
	sent_reply_num = 0
	received_request_num = 0
	received_reply_num = 0
	request_bytes_sent = 0
	request_data_sent = 0
	request_bytes_received = 0
	request_data_received = 0
	sent_request_time = 0
	received_request_time = 0
	round_trips = 0
	rtt_sum = 0
	delay_sum = 0
	dest_unreachable = 0
	hops = 0
	request_counter = 0

	for packet_data in node_list:
		# If the node IP given matches the IP address in the packet's source field...
		if source_ip in node_list[i].display_source():
			# If the type of packet is a request...
			if 'Echo (ping) request' in node_list[i].display_type():
				sent_request_num = sent_request_num + 1
				request_bytes_sent = request_bytes_sent + int(node_list[i].display_length())
				request_data_sent = request_data_sent + int(node_list[i].display_length()) - 42
				sent_request_time = float(node_list[i].display_time())
				request_counter += 0.895

				# Testing
				hops += (129 - int(node_list[i].display_info()[node_list[i].display_info().find("ttl=") + 4:node_list[i].display_info().find("ttl=") + 7]))

			# If the type of packet is a reply...
			elif 'Echo (ping) reply' in node_list[i].display_type():
				sent_reply_num = sent_reply_num + 1
				delay_sum = delay_sum + (float(node_list[i].display_time()) - received_request_time)
				#hops = hops + 129 - int(node_list[i].display_info()[node_list[i].display_info().find("ttl=") + 4:node_list[i].display_info().find("ttl=") + 7])
			else:
				dest_unreachable = dest_unreachable + 1
		# If the node IP given matches the IP address in the packet's destination field...
		elif source_ip in node_list[i].display_dest():
			# If the type of packet is a request...
			if 'Echo (ping) request' in node_list[i].display_type():
				received_request_num = received_request_num + 1
				request_bytes_received = request_bytes_received + int(node_list[i].display_length())
				request_data_received = request_data_received + int(node_list[i].display_length()) - 42
				received_request_time = float(node_list[i].display_time())
				#request_counter += 1

				# Testing
				hops += (129 - int(node_list[i].display_info()[node_list[i].display_info().find("ttl=") + 4:node_list[i].display_info().find("ttl=") + 7]))

			# If the type of packet is a reply...
			elif 'Echo (ping) reply' in node_list[i].display_type():
				received_reply_num = received_reply_num + 1
				received_reply_time = float(node_list[i].display_time())
				rtt_sum = rtt_sum + (received_reply_time - sent_request_time)
				round_trips = round_trips + 1
				sent_request_time = 0
				received_reply_time = 0
				#hops = hops + 129 - int(node_list[i].display_info()[node_list[i].display_info().find("ttl=")+4:node_list[i].display_info().find("ttl=")+7])
			else:
				dest_unreachable = dest_unreachable + 1
		i = i+1
	avg_rtt = rtt_sum / round_trips

	print("Echo requests sent: ")
	print(sent_request_num)
	print("Echo replies received: ")
	print(received_reply_num)
	print("Echo requests received: ")
	print(received_request_num)
	print("Echo replies sent: ")
	print(sent_reply_num)
	print("Echo request bytes sent: ")
	print(request_bytes_sent)
	print("Echo request bytes received: ")
	print(request_bytes_received)
	print("Echo request data sent: ")
	print(request_data_sent)
	print("Echo request data received: ") 
	print(request_data_received)
	print("Average RTT: ") # 2.56
	print(round(avg_rtt*1000.0, 2))
	print("Echo request throughput: ") # 272.5
	print(round((request_bytes_sent / rtt_sum)/1000.000, 1))
	print("Echo request goodput: ") # 256.1
	print(round((request_data_sent / rtt_sum)/1000.000, 1))
	print("Average reply delay: ") # 55.51
	print(round((delay_sum / sent_reply_num)*1000000.0, 2))
	print("Average request hop count: ")
	print(round((hops / request_counter), 2))

	# OLD print(hops / (received_reply_num + sent_reply_num - dest_unreachable))

def compute():
	print("---------- Node list 1 ----------")
	data_size_calc(node_list1, '192.168.100.1')
	print("---------- Node list 2 ----------")
	data_size_calc(node_list2, '192.168.100.2')
	print("---------- Node list 3 ----------")
	data_size_calc(node_list3, '192.168.200.1')
	print("---------- Node list 4 ----------")
	data_size_calc(node_list4, '192.168.200.2')

	print('called compute function in compute_metrics.py')
