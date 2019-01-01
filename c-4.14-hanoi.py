#!/usr/local/bin/python3

# IntheTowersofHanoipuzzle,wearegivenaplatformwiththreepegs,a, b, and c,
# sticking out of it. On peg a is a stack of n disks, each larger than
# the next, so that the smallest is on the top and the largest is on
# the bottom. The puzzle is to move all the disks from peg a to peg c,
# moving one disk at a time, so that we never place a larger disk on
# top of a smaller one. See Figure 4.15 for an example of the case n = 4
# Describe a recursive algorithm for solving the Towers of Hanoi puzzle
# for arbitrary n. (Hint: Consider first the subproblem of moving all
# but the nth disk from peg a to another peg using the third as
# “temporary storage.”)

def hanoi(height, source, target):
#    print("   DEBUG:  hanoi(",height,",",source,",",target,")")
    if source + target == 3:
        aux = 3
    if source + target == 4:
        aux = 2
    if source + target == 5:
        aux = 1

#    print("[",source,",",target,",",aux,"]")
    
    if height == 1:
        print("Move", source, "--->", target)
    else:
        hanoi(height-1, source, aux)
        hanoi(1,source,target)
        hanoi(height-1, aux, target)
    


hanoi(10,1,3)

