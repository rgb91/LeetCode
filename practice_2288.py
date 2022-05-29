class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        res = []
        for word in words:
            res_word = ''
            if word[0]=='$' and len(word)>1 and word[1:].isnumeric():
                amt = round(int(word[1:])*(100-discount)/100, 2)
                res.append(f'${amt:.2f}')
            else:
                res.append(word)
        return ' '.join(res)