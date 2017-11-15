# M02
#
print("\n--------------------------------------------------------------")
print("\n------------------------     M03     -------------------------\n")
CorruptedLine = "In a hole inXXXXXXXXXXX the ground there lived a hobbit.XXXX Not a nasty,XXXXXXXXXX dirty, wet hole, filled with theXXX ends of worms andXXXXX an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was aXXXXXXXXXXXX hobbit-hole, and that means comfort."
CleanedLine = CorruptedLine.replace("X","")
print("{}\n{}".format(CorruptedLine,CleanedLine))

