#Write a Python class to convert an integer to a roman numeral and roman numeral to an integer.

class Convert:
    def int_to_roman(self,num):
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        syb = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        roman_num=''
        i=0
        while num > 0:
            for _ in range(num//val[i]):
                roman_num+=syb[i]
                num-=val[i]
            i+=1
        return roman_num
    def roman_to_int(self,str1):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}    
        int_val=0
        for i in range(len(str1)):
            if i > 0 and rom_val[str1[i]] > rom_val[str1[i-1]]:
                int_val+=rom_val[str1[i]] - 2*rom_val[str1[i-1]]
            else:
                int_val+=rom_val[str1[i]]
        return int_val            
print(Convert().int_to_roman(1))
print(Convert().int_to_roman(4000))
print(Convert().roman_to_int('MMMCMLXXXVI'))
print(Convert().roman_to_int('MMMM'))
print(Convert().roman_to_int('C'))  

