import io

main_line = list(range(1, 51))
bonus_line = list(range(1, 11))
main_line_freq = [0] * len(main_line)
bonus_line_freq = [0] * len(bonus_line)

f = open("result.txt", "r")
lines = f.readlines()
for l in lines:
  if l[0] == '#':
    continue
  
  main_l = [int(n) for n in l.rstrip('\n').split('|')[0].strip().split(' ')]
  bonus_l = [int(n) for n in l.rstrip('\n').split('|')[1].strip().split(' ')]
  for m in main_l:
    main_line_freq[m-1] = main_line_freq[m-1] + 1
  for b in bonus_l:
    bonus_line_freq[b-1] = bonus_line_freq[b-1] + 1
	
# print(main_line_freq)
# print(bonus_line_freq)

from heapq import nlargest

print([i+1 for i,j in enumerate(main_line_freq) if j in nlargest(5, main_line_freq)])
print([i+1 for i,j in enumerate(bonus_line_freq) if j in nlargest(2, bonus_line_freq)])
