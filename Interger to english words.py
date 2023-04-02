class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        #dict for ones
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        #dict for tens
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        #dict for between 10 and 20
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        #dict for thousands
        thousands = ["", "Thousand", "Million", "Billion"]


        words = ""

        # helper function for recursive approach
        def helper(num):
            if num == 0:
                return ""
            elif num < 10:
                return ones[num] + " "
            elif num < 20:
                return teens[num - 10] + " "
            elif num < 100:
                return tens[num // 10] + " " + helper(num % 10)
            else:
                return ones[num // 100] + " Hundred " + helper(num % 100)

        i = 0
        
        while num > 0:
            if num % 1000 != 0:
                words = helper(num % 1000) + thousands[i] + " " + words
            num //= 1000
            i += 1

        return words.strip()