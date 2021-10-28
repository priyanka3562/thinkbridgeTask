# -*- coding: utf-8 -*-
__author__ = "priyanka"

# strings at index 0 is not used, it is to make array indexing simple
one = [ "", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
 
# strings at index 0 and 1 are not used, they is to make array indexing simple
ten = [ "", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
 
# n is 1- or 2- digit number
def numToWords(value, point):

    str = ""

    # if n is more than 19, divide it
    str += ten[value // 10] + one[value % 10] if (value > 19) else one[value]

    # if n is non-zero
    if (value):
        str += point

    return str

 
# Function to print a given number in words
def convertToWords(value):
    # stores word representation of given number n
    output = ""
 
    # handles digits at ten millions and hundred millions places (if any)
    output += numToWords((int(value) // 10000000), "crore ")
 
    # handles digits at hundred thousands and one millions places (if any)
    output += numToWords(((int(value) // 100000) % 100), "lakh ")
 
    # handles digits at thousands and tens thousands places (if any)
    output += numToWords(((int(value) // 1000) % 100), "thousand ")
 
    # handles digit at hundreds places (if any)
    output += numToWords(((int(value) // 100) % 10), "hundred ")
 
    if (int(value) > 100 and int(value) % 100):
        output += "and "
 
    # handles digits at ones and tens places (if any)
    output += numToWords((int(value) % 100), "")

    if '.' in str(value) and '0' in str(value):
        output += f"{output} ONLY"
    else:
        fractional_element = str(value).split('.')[-1]
        output += f"{fractional_element}/{(10**len(fractional_element))} ONLY"

    return output.title()


def main():
    try:
        value = float(input("Enter your value: "))

        # long handles upto 9 digit no change to unsigned long long int to handle more digit number
        if isinstance(value, float) or isinstance(value, int):
            # value = 99999999.99
            print(convertToWords(value = value))
        else:
            print('Please enter int value or float value')

    except Exception as e:
        print(str(e))
        print('Please enter int value or float value')


if __name__ == '__main__':
    main()