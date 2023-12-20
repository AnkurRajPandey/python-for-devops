import sys
type = sys.argv[1]

if type == "t2.micro":
    print("outout is", type)
elif type == "t2.medium":
    print("output is:", type)
elif type == "t2.large":
    print("output is:", type)
else:
    print("output is wrong")