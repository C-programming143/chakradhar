nums = [int(x) for x in raw_input().split()]

n, q = nums[0], nums[1]

nums = [int(x) for x in raw_input().split()]

for i in range(q):
     qq = [int(x) for x in raw_input().split()]

     if qq[0] == 1:
          nums[qq[1]-1] = 0 if nums[qq[1]-1] else 1
     else:
          m = nums[qq[2]-1]
if m:
     print ("ODD")
else:
     print ("EVEN")
