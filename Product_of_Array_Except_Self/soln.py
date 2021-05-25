class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        l_arr=[]
        r_arr=[]
        prev_r=prev_l=1
        for i in range(len(nums)):
            tl=nums[i]*prev_l
            l_arr.append(tl)
            prev_l=tl
            
            tr=nums[len(nums)-i-1]*prev_r
            r_arr.append(tr)
            prev_r=tr
            
        r_arr=r_arr[::-1]
        
        res.append(r_arr[1])
        for i in range(1,len(nums)-1):
            res.append(l_arr[i-1]*r_arr[i+1])
        res.append(l_arr[-2])
        
        return res