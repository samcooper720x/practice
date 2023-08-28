class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        for (i in nums.indices) {
            for (j in nums.indices) {
                if (i == j) {
                    continue
                }

                val sum = nums[i] + nums[j]

                if (sum == target) {
                    return intArrayOf(i, j)
                }
            }
        }
        throw Exception("No two sum solution found")  
    }
}
