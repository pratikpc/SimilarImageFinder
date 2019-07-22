from HashCalculate import DHashFromPath
from typing import Iterable

MINIMUM_HAMMING_DISTANCE=6

class ImageType:
    def __init__(self, path: str, Hash: str = None, Searched: bool = False, Unique: bool = True):
        self.Path: str = path
        # Calculate DHash From Path
        # Only if Required
        if Hash is None:
            self.Hash: str = DHashFromPath(path)
        else:
            self.Hash = Hash
        # print(self.Path, self.Hash)
        # By Default, All Elements are Unique
        self.Unique: bool = bool(Unique)

    # Calculate the Hamming distance between two bit strings
    def __HammingDistance(self, sleft, sright):
        if len(sleft) == len(sright):
            # Find Number of Dissimilar Bits
            return sum(int(cleft != cright)*1 for cleft, cright in zip(sleft, sright))
        else:
            # If Length is not same, assume all different
            return max(len(sleft), len(sright))


    def __iter__(self):
        return iter([self.Path, self.Hash])

    def __hash__(self) -> int:
        # Convert Given String to hash
        return int(self.Hash)

    def __eq__(self, other) ->  bool:
        hamming = self.__HammingDistance(self.Hash, other.Hash)
        return hamming <= MINIMUM_HAMMING_DISTANCE

ImageIterable = Iterable[ImageType]
