import io

total = 0
money_member_map = {}

f = open("result.txt", "r")
lines = f.readlines()
for l in lines:
    if len(l.strip()) == 0:
        continue
    
    if l[0] == '#':
        continue

    strArr = [str.strip() for str in l.rstrip('\n').split(',')]
    (exercise_date, amount, members) = (strArr[0], float(strArr[1]), strArr[2:])

    total = total + amount
    
    for name in members:
        if name not in money_member_map:
            money_member_map[name] = 0
        money_member_map[name] = round(money_member_map[name] + amount / len(members), 2)

# Print out results
print('Expected total: EUR ' + str(total))
print('Calculated total: EUR ' + str(round(sum(money_member_map.values()), 2)))
print(money_member_map)
