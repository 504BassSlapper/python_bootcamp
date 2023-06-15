import random

position = str(random.randint(1,3))+str(random.randint(1,3))
horizental = int(position[0])
vertical = int(position[1])

raw1=["a", "b","c"]
raw2=["d", "e","f"]
raw3=["g", "h","i"]
map = [raw1, raw2, raw3]

selected_raw = map[horizental -1]
selected_item = selected_raw[vertical -1]

print(selected_item)
map[horizental -1][vertical-1] = "x"
for i,item in enumerate(map):
    print(f" {i+1} : {item} \n")
