##include<stdio.h>
#int main(){
 #   printf("hello world");
  #  return 0;
#}

import collections

Card =collections.namedtuple("card,['rank','suit']")

class frenchdeck:
    ranks=[str(n)for n in range(2,11)]+list('jqka')
    suits='spades diamond clubs hearts'.split()
    def __init__(self):
        self._cards=[Card(rank,suit)for suit in self.suits for rank in self.ranks]
        