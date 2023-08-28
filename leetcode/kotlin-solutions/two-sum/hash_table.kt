class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val numsMap = mutableMapOf<Int, Int>()

        for ((i, num) in nums.withIndex()) {
            numsMap.put(num, i)
        }

        for ((i, num) in nums.withIndex()) {
            val complement = target - num
            
            if (numsMap.containsKey(complement) && numsMap.get(complement) != i) {
                val operandA = minOf(i?, numsMap.get(complement))
                val operandB = maxOf(i?, numsMap.get(complement))
                return intArrayOf(operandA, operandB)
            }
        }
        throw Exception("Unable to find two sum solution")
    }
}
