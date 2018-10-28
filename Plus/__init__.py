import os

print("----go------")

all=[]
path="Plus/"
for each in os.listdir(path):
    if each.endswith(".py") and not each.startswith("__"):
        all.append(each[:each.find('.')])