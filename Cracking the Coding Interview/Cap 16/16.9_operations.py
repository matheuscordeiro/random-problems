class Operation:

    def sub(self, x, y):
        return x + self._negative(y)

    def mult(self, x, y):
        if y > x:
            return self.mult(y, x)

        total = 0
        for _ in range(self._abs(y)):
            total += x

        if y < 0:
            total = self._negative(total)

        return total

    def div(self, x, y):
        if y > x:
            return 0
        
        result = count = 0
        abs_x = self._abs(x)
        abs_y = self._abs(y)
        while result != abs_x:
            count += 1
            result = self.mult(abs_y, count)

        if (x < 0 and y > 0) or (y < 0 and x > 0):
            count = self._negative(count)
        
        return count

    def _abs(self, x):
        if x >= 0:
            return x
        else:
            return self._negative(x)

    def _negative(self, x):
        signal = 1 if x < 0 else -1
        y = 0
        while x != 0:
            y += signal
            x += signal

        return y

if __name__ == "__main__":
    o = Operation()
    print(o.sub(5,-3))
    print(o.mult(-3,4))
    print(o.div(10, 20))