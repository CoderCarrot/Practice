# 100 --> 'one hundred'
# 345223 --> 'three hundred forty five thousand two hundred twenty three'
# 140000 -> 'one hundred forty thousand'

# assumptions: maximum number is 999,999
# assumptions: no commas 
# assumptions: no strings, only int 

WORDS =  {
  0: 'zero',
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety',
}

def num_to_string(num):

    new_num = str(num)

    if len(new_num) > 6:
        return "That is not a number we care about"
    elif len(new_num) == 1:
        return is_what_it_is(new_num)
    elif len(new_num) == 2:
        return double_digit(new_num)
    elif len(new_num) == 3:
        return hundreds(new_num)
    elif len(new_num) == 4:
        thousands = is_what_it_is(new_num[0])
        hundred_spot = hundreds(new_num)
        return (thousands + " thousand " + hundred_spot)
    elif len(new_num) == 5:
        ten_thou = double_digit(new_num[:2])
        hundred_spot = hundreds(new_num[2:])
        return (ten_thou + " thousand " + hundred_spot)
    elif len(new_num) == 6:
        hundred_thou = hundreds(new_num[:3])
        hundred_spot = hundreds(new_num[3:])
        return (hundred_thou + " thousand " + hundred_spot)
    else:
        return "Are you sure you entered a number?"


def is_what_it_is(new_num):
    num_int = int(new_num)
    return WORDS[num_int]


def double_digit(num):
    if int(num) < 21:
        return is_what_it_is(num)
    else:
        ten_spot = is_what_it_is(num[0] + '0')
        one_spot = is_what_it_is(num[1])
        return (ten_spot + " " + one_spot)


def hundreds(num):
        hundreds = is_what_it_is(num[0])
        doubles = double_digit(num[1:])
        return (hundreds + " hundred " + doubles)
# single digit 

# if single digit -- is what it is 
# else:
#     call itself, but to do what?


# while i < len(num - 1)

# <20 process o directly
# 21-99 pull off front, add zero, process tenth and oneth places directly
# 100-999, pull off front, process as oneth and hundred, process the rest as before
# 10k-99k, process k as 21-99 and add thousand, process the rest as before

print(num_to_string(34567))
print(num_to_string(100))
print(num_to_string(121))
print(num_to_string(121611364))