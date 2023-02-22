class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ans, sum_ = 0, 0
        ptr1, ptr2 = 0, len(skill) - 1
        for i in range(len(skill) // 2):
            if i == 0:
                sum_ = skill[ptr1] + skill[ptr2]
                ans += (skill[ptr1] * skill[ptr2])
            else:
                if (skill[ptr1] + skill[ptr2]) != sum_: return -1
                ans += (skill[ptr1] * skill[ptr2])
            ptr1 += 1
            ptr2 -= 1
        return ans
        