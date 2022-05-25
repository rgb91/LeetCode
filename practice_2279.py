class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        gaps = sorted([c-r for c, r in zip(capacity, rocks)])
        # print(gaps)
        full = 0
        for gap in gaps:
            if gap == 0:
                full += 1
            elif gap <= additionalRocks:
                full += 1
                additionalRocks -= gap
            else:
                break
            # print(gaps, additionalRocks, full)
        return full