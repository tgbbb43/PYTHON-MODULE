host_port = ("127.0.0.1",3000)
# print(type(host_port))

# red_rgb = (255, 0, 0)
# print(red_rgb[0])

# single_value = ("eli",)
# print(type(single_value))

# host_port[1] = "eli"
# print(host_port)

service_endpoint =("auth.server.dev.local",80)
print(f"host {service_endpoint[0]} \nport {service_endpoint[1]}")

version = (1, 2, 0)
print("Major version:", version[0])
print("First two parts:", version[:2])