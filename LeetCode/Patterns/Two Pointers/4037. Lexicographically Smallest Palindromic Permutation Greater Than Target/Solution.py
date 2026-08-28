from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)

        odd_placeholder = [c for c, count in counts.items() if count % 2 != 0]
        if len(odd_placeholder) > 1:
            return ""

        mid = odd_placeholder[0] if odd_placeholder else ""

        half_counts = {c: count // 2 for c, count in counts.items() if count // 2 > 0}

        m = n // 2
        left = []

        def dfs(idx, is_greater):
            if is_greater:
                temp_left = list(left)
                current_counts = half_counts.copy()
                for _ in range(idx, m):
                    for i in range(ord('a'), ord('z') + 1):
                        c = chr(i)
                        if current_counts.get(c, 0) > 0:
                            current_counts[c] -= 1
                            temp_left.append(c)
                            break
                left_str = "".join(temp_left)
                return left_str + mid + left_str[::-1]

            if idx == m:
                left_str = "".join(left)
                full_str = left_str + mid + left_str[::-1]
                return full_str if full_str > target else ""

            start_char = target[idx]
            for i in range(ord(start_char), ord('z') + 1):
                c = chr(i)
                if half_counts.get(c, 0) > 0:
                    half_counts[c] -= 1
                    left.append(c)

                    next_greater = is_greater or (c > target[idx])
                    ans = dfs(idx + 1, next_greater)
                    if ans:
                        return ans

                    left.pop()
                    half_counts[c] += 1
            return ""

        return dfs(0, False)
        