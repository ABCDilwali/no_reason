from itertools import permutations
from truths import truths
import random

def main():
    success=0
    while success==0:
        n=int(float(input('How many truths do you seek?  ')))
        try:
            if n<=0:
                print('You need to know the truth. Enter a value above 0.')
            elif n>len(truths):
                print(f'Only {len(truths)} truths available.')
            else:
                perm = permutations(truths,n)
                x=list(random.sample(list(perm),1))
                for y in x:
                    for truth in y:
                        print(truth)
                success=1
        except ValueError: print('Provide a different number')


if __name__=='__main__':
    main()