#
# Run script $ python3.4 pairSum.py --start=True
#

# ------------------------------------------------------------------------------------------------------------------------

from optparse import OptionParser
import random

class CheckPairSum():
    def __init__(self, x, array):
        self.x = x
        self.array = array

    def createHashMap(self):
        hashMap = {}
        for i in range(len(self.array)):
            hashMap[self.array[i]] = int(self.array[i])
        return hashMap

    def identifyPairs(self, hashMap):
        pairs = []
        for i in range(len(self.array)):
            num = int(self.array[i])
            if str(self.x-num) in hashMap and hashMap[str(self.x-num)] is not None and (num != self.x-num)  :
                pair = (self.x-num,num) if num > self.x-num else (num,self.x-num)
                if pair not in pairs:
                    pairs.append((pair))
        return pairs

    def start(self):
        hashMap = self.createHashMap()
        pairs = self.identifyPairs(hashMap)
        print("Pairs to be totalled to : {}".format(self.x))
        print("Pairs found:")
        for pair in pairs:
            print(pair)

if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option('-s', '--start', dest='start', help='Start the script',
                      default=False)

    (options, args) = parser.parse_args()

    n = int(input("Please enter a number that the pairs should total to: "))
    array = [i for i in input("Please enter as many numbers to run the program on: ").split(" ")]
    if (options.start):
        pairSum = CheckPairSum(n, array);
        pairSum.start()
