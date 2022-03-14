class Bitset:

    def __init__(self, size: int):
        self.bitset = 0
        self.size = size
        self.mask = 2**self.size-1

    def fix(self, idx: int) -> None:
        self.bitset |= (1 << ((self.size-1)-idx))

    def unfix(self, idx: int) -> None:
        temp_mask = self.mask - (2**((self.size-1)-idx))
        self.bitset &= temp_mask

    def flip(self) -> None:
        self.bitset ^= self.mask

    def all(self) -> bool:
        return True if self.bitset == self.mask else False

    def one(self) -> bool:
        return True if self.bitset != 0 else False

    def count(self) -> int:
        return self.bitset.bit_count()

    def toString(self) -> str:
        return "{0:0{length}b}".format(self.bitset, length = self.size)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()