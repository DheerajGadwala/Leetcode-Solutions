class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        s = sum(damage)
        mx = max(damage)
        return sum(damage) - min(armor, max(damage)) + 1