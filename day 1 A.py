lines=[]
for i in range(4):
    lines.append(input())

# Function to extract the first two integers from a string and return their sum
def extract_and_sum(line):
    digits = [char for char in line if char.isdigit()]
    if len(digits) >= 2:
        print(int(digits[0] + digits[-1]))
        return int(digits[0] + digits[-1])
        
    if len(digits)==1:
        print(int(digits[0] + digits[0]))
        return int(digits[0]+digits[0])
    

# Summing up the first two integers from each line
total_sum = sum(extract_and_sum(line) for line in lines)

print("Total Sum:", total_sum)
