#open all fragments
fragment_1 = open('/Users/18dbrennan-rasmussen/PycharmProjects/Summer-holiday-homework/Part 2/fragment1.txt')
fragment_2 = open('/Users/18dbrennan-rasmussen/PycharmProjects/Summer-holiday-homework/Part 2/fragment2.txt')
fragment_3 = open('/Users/18dbrennan-rasmussen/PycharmProjects/Summer-holiday-homework/Part 2/fragment3.txt')
fragment_4 = open('/Users/18dbrennan-rasmussen/PycharmProjects/Summer-holiday-homework/Part 2/fragment4.txt')
fragment_5 = open('/Users/18dbrennan-rasmussen/PycharmProjects/Summer-holiday-homework/Part 2/fragment5.txt')
fragment_6 = open('/Users/18dbrennan-rasmussen/PycharmProjects/Summer-holiday-homework/Part 2/fragment6.txt')

#read all fragments
frag1 = fragment_1.read()
frag2 = fragment_2.read()
frag3 = fragment_3.read()
frag4 = fragment_4.read()
frag5 = fragment_5.read()
frag6 = fragment_6.read()

#open all suspects
suspect_1 = open('/Users/18dbrennan-rasmussen/PycharmProjects/Summer-holiday-homework/Part 2/suspect1.txt')
suspect_2 = open('/Users/18dbrennan-rasmussen/PycharmProjects/Summer-holiday-homework/Part 2/suspect2.txt')
suspect_3 = open('/Users/18dbrennan-rasmussen/PycharmProjects/Summer-holiday-homework/Part 2/suspect3.txt')
suspect_4 = open('/Users/18dbrennan-rasmussen/PycharmProjects/Summer-holiday-homework/Part 2/suspect4.txt')
suspect_5 = open('/Users/18dbrennan-rasmussen/PycharmProjects/Summer-holiday-homework/Part 2/suspect5.txt')

#read all suspects
sus1 = suspect_1.read()
sus2 = suspect_2.read()
sus3 = suspect_3.read()
sus4 = suspect_4.read()
sus5 = suspect_5.read()

#suspect 1
#extraction
frag1 = sus1[0:]
frag2 = sus1[0:]
frag3 = sus1[0:]
frag4 = sus1[0:]
frag5 = sus1[0:]
frag6 = sus1[0:]

#find fragment and print
part11 = sus1.find(frag1)
print(part11)

part12 = sus1.find(frag2)
print(part12)

part13 = sus1.find(frag3)
print(part13)

part14 = sus1.find(frag4)
print(part14)

part15 = sus1.find(frag5)
print(part15)

part16 = sus1.find(frag6)
print(part16)

print('------------------------')

#suspect 2
# extraction
frag1 = sus2[0:]
frag2 = sus2[0:]
frag3 = sus2[0:]
frag4 = sus2[0:]
frag5 = sus2[0:]
frag6 = sus2[0:]

#find fragment and print
part21 = sus2.find(frag1)
print(part21)

part22 = sus2.find(frag2)
print(part22)

part23 = sus2.find(frag3)
print(part23)

part24 = sus2.find(frag4)
print(part24)

part25 = sus2.find(frag5)
print(part25)

part26 = sus2.find(frag6)
print(part26)

print('------------------------')

#suspect 3
# extraction
frag1 = sus3[0:]
frag2 = sus3[0:]
frag3 = sus3[0:]
frag4 = sus3[0:]
frag5 = sus3[0:]
frag6 = sus3[0:]

#find fragment and print
part31 = sus3.find(frag1)
print(part31)

part32 = sus3.find(frag2)
print(part32)

part33 = sus3.find(frag3)
print(part33)

part34 = sus3.find(frag4)
print(part34)

part35 = sus3.find(frag5)
print(part35)

part36 = sus3.find(frag6)
print(part36)

print('------------------------')

#suspect 4 extraction
frag1 = sus4[0:]
frag2 = sus4[0:]
frag3 = sus4[0:]
frag4 = sus4[0:]
frag5 = sus4[0:]
frag6 = sus4[0:]

#suspect 5 extraction
frag1 = sus5[0:]
frag2 = sus5[0:]
frag3 = sus5[0:]
frag4 = sus5[0:]
frag5 = sus5[0:]
frag6 = sus5[0:]