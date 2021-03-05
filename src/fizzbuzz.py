class FizzBuzz():
    def __init__(self):
        pass

    def convert(self, num: int) -> str:
        """Return int to str but print 'Fizz' if an integer is divisible by 3, 
           'Buzz' if an integer is divisible by 5, 
           and 'FizzBuzz' if an integer is divisible by both 3 and 5

        Args:
            num (int): input num

        Returns:
            str: output str
        """
        if num % 3 == 0 and num % 5 == 0:
            return 'FizzBuzz'
        elif num % 3 == 0:
            return 'Fizz'
        elif num % 5 == 0:
            return 'Buzz'
        return str(num)


if __name__ == '__main__':
    pass
