#open fragment5.txt file
fragment_5 = open('/Users/18dbrennan-rasmussen/PycharmProjects/Summer-holiday-homework/Part 1/fragment5.txt')
fragment = fragment_5.read()

#open suspect1.txt file
suspect_1 = open('/Users/18dbrennan-rasmussen/PycharmProjects/Summer-holiday-homework/Part 1/suspect1.txt')
suspect = suspect_1.read()

frag1 = suspect[0:]

#find fragment in suspect's dna
part1 = suspect.find(fragment)

#print
print(part1)
