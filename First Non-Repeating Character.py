class Solution:
    
    # Function to check whether two strings are anagram of each other
    def isAnagram(self, s1, s2):
        # Step 1: Length check karlo
        if len(s1) != len(s2):
            return False
        
        # Step 2: Character frequency count karlo
        freq = {}
        
        for ch in s1:
            freq[ch] = freq.get(ch, 0) + 1  # s1 ke characters ka count
        
        # Step 3: s2 ke characters ke count ko decrease karte jao
        for ch in s2:
            if ch not in freq:
                return False  # Character missing hai
            freq[ch] -= 1
            if freq[ch] < 0:
                return False  # Count negative hua toh not anagram
        
        # Step 4: Sab balance hai toh anagram hai
        return True



# Example Driver Code (for testing)
if __name__ == "__main__":
    s1 = input("Enter first string: ").strip()
    s2 = input("Enter second string: ").strip()

    ob = Solution()
    if ob.isAnagram(s1, s2):
        print("YES, they are anagrams.")
    else:
        print("NO, they are not anagrams.")
