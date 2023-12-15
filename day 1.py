new=[]
lines=[]
for i in range(1000):
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

print("part 1:", total_sum)

for line in lines:
    line=line.replace("one","o1ne")
    line=line.replace("two","t2wo")
    line=line.replace("three",'t3hree')
    line=line.replace("four","f4or")
    line=line.replace("five","f5ive")
    line=line.replace("six","s6ix")
    line=line.replace("seven","s7even")
    line=line.replace("eight","e8ight")
    line=line.replace("nine","n9ine")
    item=[]

    for char in line:
        if char>="0" and char <="9":
            item.append(int(char))
    new.append(item)
total=0
for item in new:
    total+=(10*item[0])
    total+=item[-1] 

print("part 2 ",total)