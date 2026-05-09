class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] in dict1:
                dict1[nums[i]] += 1
            else:
                dict1[nums[i]] = 1
        sorted_dict_desc = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
        list_1 = []
        for small_k in range(k):
            list_1.append(list(sorted_dict_desc.keys())[small_k])
        return list_1
        