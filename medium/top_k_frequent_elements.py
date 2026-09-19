class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hist = defaultdict(int)
        for num in nums:
            hist[num] += 1
        
        num_freq = defaultdict(list)
        for num, freq in hist.items():
            num_freq[freq].append(num)

        returnList = []
        for freq in sorted(num_freq, reverse=True):
            returnList = returnList + num_freq[freq]

        return returnList[0:k]
        
