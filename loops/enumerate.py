# enumerate
# zip

# servers = ["web-01", "web-02", "web-03"]
# [(0, "web-01"), (1, "web-02"),(2, "web-03")]
# for server in enumerate(servers):
#     print(type(server))
#     print(server)
#     print(f"this is tuple {server}")
    

# servers = ["web-01", "web-02", "web-03"]
# [(0, "web-01"), (1, "web-02"),(2, "web-03")]
# for index, server in enumerate(servers):
#     # print(type(server))
#     # print(server)
#     # print(server[0]) # index
#     # print(server[1]) # item
#     print(f"{index} Proccessing server {server}")

# ?  [Python Basics] Hands-On Lab 4.2 - Enumerate & Zip

# 1
# names = ["Alice", "Bob", "Charlie"]
# for name in enumerate(names):
#     print(name)

# 2
# servers = ["app-01", "app-02", "app-03"]
# for server in  enumerate(servers,start=1):
#     print(server)

# 3

# errors = ["disk full", "timeout", "connection lost"]
# for x,e in  enumerate(errors,start=1):
#     if x % 2 == 0:
#         print(e)

# 4
# ports = [22, 80, 443, 8080]
# for a,b in enumerate(ports):
#     if a >= 1:
#         print(b)

# 5
# users = ["admin", "dev", "ops"]
# for a,b, in enumerate(users,start=1):
#     print(f"user {a}:{b}")

# 6
files = ["log1.txt", "log2.txt", "log3.txt"]
for a,b in enumerate(files):
    if a == 2:
        print(b) 