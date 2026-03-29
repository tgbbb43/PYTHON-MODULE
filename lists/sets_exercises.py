ports_list = [8080, 8443, 22, 8080, 443]
unique_ports = set(ports_list)
# print(unique_ports)
server_names = {"web01", "web02", "web03"}
is_22 = 22 in ports_list
is_22 = 22  in server_names
# print(is_22)
unique_ports.add(3000)
# unique_ports.remove(22)
unique_ports.discard(22)
# print(unique_ports)

o = [1, 2, 2, 3, 3, 4]
u = set(o)
f = 4 in o
print(o)
print(u)
print(f)