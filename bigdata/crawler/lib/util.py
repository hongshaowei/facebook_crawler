'''

@author: casper
'''

import random
import string


class Util:
    @staticmethod
    def add_unique_postfix(suffix, length):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length)) + '.' + suffix
