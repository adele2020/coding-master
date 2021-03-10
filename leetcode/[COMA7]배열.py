from typing import *
#######################################################################
# 7. 두 수의 합 (리트코드1.) *
# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라
# input = [2,7,11,15], target=9
# output = [0,1]
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Input: nums = [3,3], target = 6
# Output: [0,1]
# Input: nums = [0,4,3,0], target = 0
# Output: [0,3]
#######################################################################
def twoSum(nums: List[int], target: int) -> List[int]:
    output = []
    for i, v in enumerate(nums):
        temp = target - v
        #목표값에서 해당값을 뺀 나머지(temp)를 리스트에서 찾는다.
        for j, z in enumerate(nums):
            #나머지(temp) 값이 같고, 자기자신은 아닌 값을 리스트에 담는다.
            if temp == z and i != j:
                output.append(j)
    return sorted(output)

twoSum([2,7,11,15],9)
twoSum([3,2,4],6)
twoSum([3,3],6)
twoSum([0,4,3,0],0)
#Runtime 632 ms
#Memory 14.5 MB

"""
반복문과 조회하는 in을 활용하면 되고,
아니면 딕션너리로 값과 인덱스로 구현한 다음 타겟값에서 뺀 값을 그대로 조회하여 return
"""
#######################################################################
# 8. 빗물 트래핑 (리트코드42.) ***
# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.
# input = [0,1,0,2,1,0,1,3,2,1,2,1]
# output = 6
# 설명 : 나눗셈을 하지 않고 O(n)에 풀이하라.
#######################################################################
def trap(height: List[int]) -> int:
    x = 0
    for i, v in enumerate(height):
        if i != (len(height)-1):
            h = height[i] - height[i+1]
            if (h) > 0:
                x += h
    return x



def trap_2(height: List[int]) -> int:
    x = 0
    for i, v in enumerate(height):
        if i != (len(height)-1):
            h = height[i] - height[i+1]
            if (h) > 0:
                x += h
    return x

def trap_2(height: List[int]) -> int:
    # height가 없으면 0
    if not height:
        return 0

    volume = 0
    #left index와 right index 설정 - 초기값
    left, right = 0, len(height)-1
    #left 값 과 right 값 설정 - 초기값
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume


trap_2([0,1,0,2,1,0,1,3,2,1,2,1])
trap_2([1,0,2,0,2,0,1])    #틀렸다. ㅠ

#######################################################################
# 9. 세 수의 합 (리트코드15.) **
# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.
# input = [-1,0,1,2,-1,-4]
# output = [ [-1,0,1], [-1,-1,2] ]
#######################################################################
def threeSum(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()
    kList = []
    for i in range(len(nums)-2):

        # 중복된 값 건너띄기
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)-1):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k-1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append((nums[i], nums[j], nums[k]))
                kList.append((nums[i], nums[j], nums[k]))
    print("kList: {}".format(kList))
    return results

threeSum([-1,0,1,2,-1,-4])
"""
(-4, -1, -1),
(-4, -1, 0),
(-4, -1, 1),
(-4, -1, 2),
(-4, 0, 1),
(-4, 0, 2),
(-4, 1, 2),
(-1, -1, 0),
(-1, -1, 1),
(-1, -1, 2),
(-1, 0, 1),
(-1, 0, 2),
(-1, 1, 2),
(0, 1, 2)
"""

def threeSum_twopoint(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()
    for i in range(len(nums)-2):
        #중복된 값 건너띄기
        if i > 0 and nums[i] == nums[i-1]:
            continue
        #간격을 좁혀가면 합 sum
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # sum=0 인 경우이므로 정답 및 스킵 처리
                results.append((nums[i], nums[left], nums[right]))
                while left < right and nums[left] == nums[left+1]:
                    left +=1
                while left < right and nums[right] == nums[right-1]:
                    right -=1
                left += 1
                right -= 1
    return results

threeSum_twopoint([-1,0,1,2,-1,-4])
#######################################################################
# 10. 배열 파티션 I (리트코드561.) *
# n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
# input = [1,4,3,2]
# output = 4
# 설명 : n은 2가 되며, 최대 합은 4이다. min(1,2)+min(3,4)=4
# Input: nums = [6,2,6,5,1,2]
# Output: 9
#######################################################################
def arrayPairSum(nums: List[int]) -> int:
    slist = sorted(nums) # 정렬
    output = 0
    l = len(nums)//2 # 몇개의 페어로 나오나
    for i in range(l):
        output += min(slist[i*2:(i+1)*2]) # 각 페어의 index적용
    return output

arrayPairSum([1,4,3,2])
arrayPairSum([6,2,6,5,1,2])
#Runtime 288 ms
#Memory 16.9 MB

def arrayPairSum_2(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])

#######################################################################
# 11. 자신을 제외한 배열의 곱 (리트코드238.) **
# 배열을 입력받아 output[i]가 자신을 제외한 나머지 요소의 곱셈 결과가 되도록 출력하라.
# input = [1,2,3,4]
# output = [24,12,8,6]
# 설명 : 나눗셈을 하지 않고 O(n)에 풀이하라.
#######################################################################
def productExceptSelf(nums: List[int]) -> List[int]:
    output = []
    for i, v in enumerate(nums):
        copy_nums = nums.copy() #원본 리스트를 매번 복사해서 원본유지.
        del copy_nums[i] #index를 통한 원소 삭제
        x = 1
        for v in copy_nums: #삭제된 리스트내 원소들 곱하기
            x = x * v
        output.append(x)
    return output
# time limit 초과 ㅠ


from functools import reduce
def productExceptSelf_reduce(nums: List[int]) -> List[int]:
    output = []
    for i, v in enumerate(nums):
        copy_nums = nums.copy() #원본 리스트를 매번 복사해서 원본유지.
        del copy_nums[i] #index를 통한 원소 삭제
        output.append(reduce(lambda x, y: x * y, copy_nums))
    return output
# time limit 초과 ㅠ

productExceptSelf([1,2,3,4])
productExceptSelf_reduce([1,2,3,4])

#책은 위와 다른 풀이를 하고 있다 이해할 수 없다.

#reduce() : 리스트의 두 아이템(원소)에 함수를 왼쪽에서 오른쪽으로
#           누적적으로 적용해서 하나의 단일 값으로 줄인다

#######################################################################
# 12. 주식을 사고파기 가장 좋은 시점 (리트코드121.) *
# 한 번의 거래로 낼 수 있는 최대 이익을 산출하라.
# input = [7,1,5,3,6,4]
# output = 5
# 설명 : 1일 때 사서 6일 때 팔면 5의 이익을 얻는다.
########################################################################
def maxProfit(self, prices: List[int]) -> int:
