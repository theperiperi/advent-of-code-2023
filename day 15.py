def hash(s):
    v = 0
    
    for ch in s:
        v += ord(ch)
        v *= 17
        v %= 256

    return v

# Open the file in read mode
with open("C:\\Users\\pri\\Desktop\\sample.txt", 'r') as file:
    # Read the content of the file and split it by ","
    input_data = file.read().strip().split(",")

# Calculate the sum of hashes and print the result
print(sum(map(hash, input_data)))

boxes = [[] for _ in range(256)]
focal_lengths = {}

for instruction in input_data:
    if "-" in instruction:
        label = instruction[:-1]
        index = hash(label)
        if label in boxes[index]:
            boxes[index].remove(label)
    else:
        label, length = instruction.split("=")
        length = int(length)
        
        index = hash(label)
        if label not in boxes[index]:
            boxes[index].append(label)
            
        focal_lengths[label] = length

total = 0

for box_number, box in enumerate(boxes, 1):
    for lens_slot, label in enumerate(box, 1):
        total += box_number * lens_slot * focal_lengths[label]

print(total)
