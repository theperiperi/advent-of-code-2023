new=[]
lines = []
for i in range(1000):
    ele = input()
    lines.append(ele)

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

print(total)
