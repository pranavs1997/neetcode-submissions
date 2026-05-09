class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dict1 = {}
        # for i in range(len(nums)):
        #     if nums[i] in dict1:
        #         dict1[nums[i]] += 1
        #     else:
        #         dict1[nums[i]] = 1
        # sorted_dict_desc = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
        # list_1 = []
        # for small_k in range(k):
        #     list_1.append(list(sorted_dict_desc.keys())[small_k])
        # return list_1
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        # my_dict = {n: [] for n in range(1, len(nums) + 1)}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        # for key, val in dict1.items():
        #     my_dict[val] = [key]
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res