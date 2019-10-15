def longestPalindrome(self, s: str) -> str:
    def is_palindrome(string):
        n = len(string)
        if n % 2 == 0:
            mid = (n // 2) - 1
            for j in range(mid + 1):
                if string[j] == string[2 * mid - j + 1]:
                    continue
                else:
                    return False
            return True
        else:
            mid = n // 2
            for i in range(mid):
                if string[i] == string[2 * mid - i]:
                    continue
                else:
                    return False
            return True

    count = 0
    max_len = 0
    for j in range(len(s)):
        left = 0
        right = 1 + count
        while right <= len(s):
            if is_palindrome(s[left:right]):
                cur_len = right - left
                if cur_len > max_len:
                    max_len = cur_len
                    cur_s = s[left:right]
                    left += 1
                    right += 1
                    break
            else:
                left += 1
                right += 1
                continue
        count += 1

    return cur_s

if __name__ == '__main__':
    s = longestPalindrome('ccabcdcbacc','testset')
    print(s)