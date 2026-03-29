required_packages = {"python3", "pip", "requests", "boto3", "pip"}
i = "requests" in required_packages
x = "ansible" in required_packages
# print(f"Is 'requests' required? {i}")
# print(f"Is 'ansible' required? {x}")
required_packages.add( "paramiko")
required_packages.discard("pip")
# print(required_packages)

installed_packages = {"docker", "python3", "pip"}
missing_packages = required_packages - installed_packages
extra_packages = installed_packages - required_packages
common_packages = required_packages & installed_packages
print(f"Missing packages: {missing_packages}")
print(f"Extra packages: {extra_packages}")
print(f"Common packages: {common_packages}")