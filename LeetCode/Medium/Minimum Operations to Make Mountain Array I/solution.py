class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        maxi = max(nums)
        maxi = maxi + 100

        if n <= 2:
            return -1

        dpl = [[10**8] * (maxi + 200 + 1) for _ in range(n + 1)]
        prefix = [[10**8] * (maxi + 200 + 1) for _ in range(n + 1)]

        for j in range(1, maxi + 200 + 1):
            dpl[0][j] = abs(nums[0] - j)
            prefix[0][j] = min(prefix[0][j-1], dpl[0][j])

        dpl[0][0] = 10**8

        for i in range(1, n):
            for j in range(1, maxi + 200 + 1):
                dpl[i][j] = min(dpl[i][j], abs(nums[i] - j) + prefix[i-1][j-1])
                prefix[i][j] = min(prefix[i][j-1], dpl[i][j])

        dpr = [[10**8] * (maxi + 200 + 1) for _ in range(n + 1)]
        suffix = [[10**8] * (maxi + 200 + 1) for _ in range(n + 1)]

        for j in range(1, maxi + 200 + 1):
            dpr[n-1][j] = abs(nums[n-1] - j)
            suffix[n-1][j] = min(suffix[n-1][j-1], dpr[n-1][j])

        dpr[n-1][0] = 10**8

        for i in range(n - 1, -1, -1):
            for j in range(1, maxi + 200 + 1):
                dpr[i][j] = min(dpr[i][j], abs(nums[i] - j) + suffix[i+1][j-1])
                suffix[i][j] = min(suffix[i][j-1], dpr[i][j])

        answer = 10**8

        for i in range(1, n - 1):
            for j in range(1, maxi + 200 + 1):
                first = abs(nums[i] - j)
                second = prefix[i-1][j-1]
                third = suffix[i+1][j-1]

                answer = min(answer, first + second + third)

        if answer >= 10**8:
            return -1

        return answer