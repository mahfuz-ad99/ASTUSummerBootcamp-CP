class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words by spaces
        words = s.split(" ")
        
        # Reverse each word individually
        reversed_words = [word[::-1] for word in words]
        
        # Join the words back together with a space
        return " ".join(reversed_words)
