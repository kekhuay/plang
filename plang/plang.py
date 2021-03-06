import math


def to_thai(number):
    __SMALL = [
        'ศูนย์', 'หนึ่ง', 'สอง', 'สาม', 'สี่',
        'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า'
    ]
    __DENOM = {2: 'สิบ', 3: 'ร้อย', 4: 'พัน', 5: 'หมื่น', 6: 'แสน', 7: 'ล้าน'}
    n = number
    if __number_size(n) > 7:
        left = (n // 1000000)
        n = n - (left * 1000000)
        if n == 0:
            return to_thai(left) + 'ล้าน'
        return to_thai(left) + 'ล้าน' + to_thai(n)
    else:
        thai_word = ''
        if __is_negative(n):
            thai_word += 'ลบ'
            n = abs(n)
        if n < 10:
            return thai_word + __SMALL[n]
        else:
            while __number_size(n) > 0:
                left_most_digit = __left_most_digit(n)
                number_size = __number_size(n)
                if number_size == 2:
                    if left_most_digit != 1:
                        if left_most_digit == 2:
                            thai_word += 'ยี่'
                        else:
                            thai_word += __SMALL[left_most_digit]
                    thai_word += __DENOM[number_size]
                elif number_size == 1:
                    thai_word += 'เอ็ด' if n == 1 else __SMALL[n]
                else:
                    thai_word += __SMALL[__left_most_digit(n)]\
                        + __DENOM[__number_size(n)]
                n = __remove_left_most_digit(n)
            return thai_word


def __left_most_digit(n):
    if n < 10:
        return n
    else:
        return __left_most_digit(n // 10)


def __number_size(n):
    n = abs(n)
    if n == 0:
        return 0
    return math.floor(math.log10(n)) + 1


def __is_negative(n):
    return n < 0


def __remove_left_most_digit(n):
    return n - (__left_most_digit(n) * (10 ** (__number_size(n) - 1)))
