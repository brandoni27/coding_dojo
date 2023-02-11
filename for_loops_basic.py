# Brandon Washington
# Assignment: For Loops: Basic I

# Basic
for i in range(151):
    print(i);

# Multiples of Five
for x in range(1,201):
    print(x*5)

# Counting the Dojo way
for c in range(1,101):
    if(c%5==0):
        print("coding")
    else:
        print(c)

# Whoa. That Sucker's Huge
sum=0
for o in range(1,500001):
    if(o%2==1):
        sum+=o
    elif(o==500000):
        print(sum)

# Countdown by Fours
for r in range(2018, 0, -4):
    print(r)

# Flexible Counter
lowNum = 5
highNum = 60
multi = 8

for m in range(lowNum, highNum):
    if(m%multi==0):
        print(m)