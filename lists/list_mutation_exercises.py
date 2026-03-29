deployment_targets = ["us-east-1","eu-west-1","ap-southeast-1"]
# print(deployment_targets)
# print(deployment_targets[1])

deployment_targets. append("us-west-2")
# print(deployment_targets)
deployment_targets[1] = "eu-central-1"
deployment_targets[0] = "eli"
print(len(deployment_targets))
print(deployment_targets)