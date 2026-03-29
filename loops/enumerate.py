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
# files = ["log1.txt", "log2.txt", "log3.txt"]
# for a,b in enumerate(files):
#     if a == 2:
#         print(b) 

# תרגיל 7: כולם מלבד הראשון
regions = ["us-east-1", "eu-west-1", "ap-south-1"]
for index, region in enumerate(regions):
    if index != 0:
        print(region)

# תרגיל 8: שירות ואינדקס מ-1
services = ["nginx", "redis", "postgres"]
for index, service in enumerate(services, start=1):
    print(index, service)

# תרגיל 9: אינדקס אי-זוגי
tasks = ["backup", "cleanup", "monitoring"]
for index, task in enumerate(tasks):
    if index % 2 != 0:
        print(task)

# תרגיל 10: עצירה באינדקס 2
containers = ["c1", "c2", "c3", "c4"]
for index, container in enumerate(containers):
    if index == 2:
        break
    print(container)
    
    
# תרגיל 11: Host ו-IP
hosts = ["host1", "host2", "host3"]
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
for host, ip in zip(hosts, ips):
    print(host, ip)

# תרגיל 12: User ו-ID
users = ["alice", "bob", "charlie"]
ids = [101, 102, 103]
for name, user_id in zip(users, ids):
    print(f"User {name} has ID {user_id}")

# תרגיל 13: Service ו-Port
services = ["nginx", "redis", "postgres"]
ports = [80, 6379, 5432]
for service, port in zip(services, ports):
    print(service, port)

# תרגיל 14: חיבור Region ו-Zone
regions = ["us-east-1", "eu-west-1"]
zones = ["a", "b"]
for r, z in zip(regions, zones):
    print(r + z)

# תרגיל 15: רק Containers במצב running
containers = ["c1", "c2", "c3"]
statuses = ["running", "stopped", "paused"]
for container, status in zip(containers, statuses):
    if status == "running":
        print(container)

# תרגיל 16: שלושה ערכים יחד
files = ["file1", "file2"]
sizes = [100, 200]
types = ["txt", "log"]
for f, s, t in zip(files, sizes, types):
    print(f, s, t)

# תרגיל 17: כמה יודפסו בפועל? (יודפסו 2 - לפי הרשימה הקצרה ביותר)
names = ["serviceA", "serviceB", "serviceC"]
versions = ["1.0", "2.0"]
for name, ver in zip(names, versions):
    print(name, ver)

# תרגיל 18: שלישיית DB
dbs = ["mysql", "postgres", "mongo"]
ports = [3306, 5432, 27017]
hosts = ["db1", "db2", "db3"]
for db, port, host in zip(dbs, ports, hosts):
    print(db, port, host)

# תרגיל 19: משימות שנכשלו
tasks = ["build", "test", "deploy"]
durations = [5, 10, 3]
statuses = ["ok", "ok", "failed"]
for task, time, status in zip(tasks, durations, statuses):
    if status == "failed":
        print(task)

# תרגיל 20: הכל בשורה אחת
users = ["admin", "dev"]
roles = ["full-access", "read-only"]
regions = ["us", "eu"]
for u, r, reg in zip(users, roles, regions):
    print(u, r, reg)