class VanderCorputSeq:
    """
    Van der Corput Sequence is 'dense' on [0, 1] so it can be used to
    generate ideal samples for sample-based motion planning algorithms
    """
    def __init__(self, dimension = 1):
        self._dimension = 1
        self._seq = []
        self._num = 0

    def get_sample(self, index):
        """
        get the element at the place of [index] in van der Corput Sequence, 0-indexing;
        if the element was not calculated, calculate all elements before.
        :param index: the index where the element is inquired
        :return: the element inquired
        TODO: add support for dimension = 2
        """
        if self._dimension == 1:
            if index < self._num:
                return self._seq[index]
            else:
                for i in range(self._num, index+1):
                    i_bin = bin(i)[2:][::-1]
                    the_num = 0
                    for j in range(len(i_bin)):
                        the_num += (i_bin[j] == '1') * 2**(-j-1)
                    self._seq.append(the_num)
                return self._seq[index]
