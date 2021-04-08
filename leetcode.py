def maxSubArray(nums):
    max_val=nums[0]
    cur_sum=0
    for idx  in range(0,len(nums)):
        cur_sum=cur_sum+nums[idx]
        if cur_sum>max_val:
            max_val=cur_sum

        if nums[idx]>max_val:
            max_val=nums[idx]
            cur_sum=nums[idx]
        elif nums[idx]>=0 and nums[idx]>cur_sum:
            cur_sum=nums[idx]



        idx=idx+1

    return max_val
        
        

nums=[-2,1,-3,4,-1,2,1,-5,4]
erg=maxSubArray(nums)
print(erg)