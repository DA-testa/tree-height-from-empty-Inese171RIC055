# python3

import sys
import threading
import numpy

from os.path import exists


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    return max_height

def compute_tree_height(nodes, parents, nodeCount):
    maxDepth = 0
    depthHolder = numpy.empty([nodeCount, 1], dtype=numpy.int32)

    for mainCheckingItem in nodes:
        notChecked = True
        currentDepth = 1
        checkItem = mainCheckingItem
        while notChecked :
            if checkItem in depthHolder:
                currentDepth = currentDepth + (depthHolder[checkItem] - 1)
                notChecked = False
            else:
                currentParent = parents[checkItem]
                if currentParent > -1:
                    currentDepth = currentDepth + 1
                    checkItem = currentParent
                else:
                    notChecked = False
        depthHolder[mainCheckingItem] = currentDepth
        if currentDepth > maxDepth and currentDepth < nodeCount:
            maxDepth = currentDepth
    return maxDepth

def main():
    # implement input form keyboard and from files
    fistInput = input("")
    try:
        if firstInput == "I":
            nodeCount = int(fistInput)
            parrentListString = input("")
        elif firstInput == "F":
            fistInput = input("")
            if fistInput.find('s'):
                exit()
            if exists(fistInput):
                fileItem = open(fistInput, "r")
                lines = fileItem.readlines()
                count = 0
                for line in lines:
                    if count == 0:
                        nodeCount = int(line.strip())
                    if count == 1:
                        parrentListString = line.strip()
                    if count > 1:
                        break
                    count = count + 1
    except:
        if fistInput.find('s'):
            exit()
        if exists(fistInput):
            fileItem = open(fistInput, "r")
            lines = fileItem.readlines()
            count = 0
            for line in lines:
                if count == 0:
                    nodeCount = int(line.strip())
                if count == 1:
                    parrentListString = line.strip()
                if count > 1:
                    break
                count = count + 1
        else:
            exit("Nepareiza atbilde")

    # list_of_strings = parrentListString.split(' ')# 👉️ 
    # list_of_integers = [int(x) for x in list_of_strings]
    
    nodes = numpy.arange(0, nodeCount)
    # nodesParrents = numpy.array(list_of_integers)
    nodesParrents = numpy.fromstring(parrentListString, dtype=int, sep=' ')
    height = compute_tree_height(nodes, nodesParrents, nodeCount)
    print(numpy.sum(height)) # output: 3

    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main() -- why is it called second time ?
# print(numpy.array([1,2,3]))