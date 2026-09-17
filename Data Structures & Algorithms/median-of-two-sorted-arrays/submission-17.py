class Solution:
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        total = n + m
        def index(val, array, l):
            lb = 0
            ub = l - 1
            idx = 0
            while lb <= ub:
                mid = (lb + ub) // 2
                if val > array[mid]:
                    idx = mid + 1
                    lb = mid + 1
                else:
                    ub = mid - 1

            return idx

        def binary_search(src, dst, k):
            lb = 0
            ub = len(src) - 1
            ans = 0
            while lb <= ub :
                mid = (lb + ub) // 2
                otherIdx = index(src[mid], dst, len(dst))
                idx = mid + otherIdx
                if idx > k:
                    ub = mid - 1
                else: 
                    print(f"index is {mid}")
                    print(f"other index is {otherIdx}")
                    print(f"elem is {src[mid]}")
                    ans = mid
                    lb = mid + 1
            return ans
        
        if total % 2 == 1:
            k = total // 2
            ans = binary_search(nums1, nums2, k)
            if not nums1 or ans + index(nums1[ans], nums2, m) != k:
                return nums2[binary_search(nums2, nums1, k)]
            else:
                return nums1[ans]
        else:
            k1 = total // 2
            k2 = total // 2  - 1
            ans1 = binary_search(nums1, nums2, k1)
            print(f"index is ${ans1}")
            if not nums1 or ans1 + index(nums1[ans1], nums2, m) != k1:
                #print(binary_search(nums2, nums1, k1))
                ans1 = nums2[binary_search(nums2, nums1, k1)]
            else:
                ans1 = nums1[ans1]
            
            ans2 = binary_search(nums1, nums2, k2)
            print(f"index is ${ans2}")
            if not nums1 or ans2 + index(nums1[ans2], nums2, m) != k2:
                ans2 = nums2[binary_search(nums2, nums1, k2)]
            else:
                ans2 = nums1[ans2]
            print("answers")
            print(ans1)
            print(ans2)
            print("end")
            return (ans1 + ans2) / 2



        