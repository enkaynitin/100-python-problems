class num_div_seven(object):

    def __init__(self,number):
        self.n = number

    def generate(number):
        start = 0
        stop = stop
        while start < number:
            j = start
            start = start+1
            if j%7 == 0:
                yield j

a = num_div_seven(100)
a.generate()
