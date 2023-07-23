#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """

if __name__ == '__main__':

    import sys

    Codes = {"200": 0,
                   "301": 0,
                   "400": 0,
                   "401": 0,
                   "403": 0,
                   "404": 0,
                   "405": 0,
                   "500": 0
                   }
    fileSize = 0
    counter = 0


    def print_results(Codes, fileSize):
        """Print values"""
        print("File size: {:d}".format(fileSize))
        for Code, times in sorted (Codes.items()):
            if times:
                print("{:s}: {:d}".format(Code, times))
    try:
        """Read stdin per line"""
        for line in sys.stdin:
            if counter != 0 and counter == 10:
                """After every 10 lines, print from the beginning"""
                print_results(Codes, fileSize)
            counter += 1
            data = line.split()
            try:
                """Compute metrics"""
                Code = data[-2]
                if Code in Codes:
                    Codes[Code] += 1
                fileSize += int(data[-1])
            except:
                pass
        print_results(Codes, fileSize)
    except KeyboardInterrupt:
        """Keyboard interruption, print from the beginning"""
        print_results(  def print_results(Codes, fileSize):
        """ Print statistics """
        print("File size: {:d}".format(fileSize))
        for Code, times in sorted(Codes.items()):
            if times:
                print("{:s}: {:d}".format(Code, times))Codes, fileSize)
        raise

