import re


class Solution:

    def myAtoi(self, s: str) -> int:
        white_space_ignored = s.replace(' ', '')
        composite_nums = ''

        if not white_space_ignored:
            return 0

        if white_space_ignored[0] == '-':
            if not white_space_ignored[1::]:
                return 0
            if not white_space_ignored[1].isdigit():
                return 0
            composite_nums = white_space_ignored[0::]
        elif white_space_ignored[0] == '+':
            if not white_space_ignored[1::]:
                return 0
            if not white_space_ignored[1].isdigit():
                return 0
            composite_nums = white_space_ignored[1::]
        elif not white_space_ignored[0].isdigit():
            return 0
        else:
            composite_nums = white_space_ignored

        only_nums = float(re.sub('[^\d -.]', '', composite_nums))

        if only_nums < -1 * 2 ** 31:
            return -1 * 2 ** 31
        elif (only_nums >= -1 * 2 ** 31) and (only_nums <= (2 ** 31 - 1)):
            return int(only_nums)
        else:
            return 2 ** 31 - 1

