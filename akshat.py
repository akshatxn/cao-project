# CAO PROJECT FINANCIAL STOCK PORTFOLIO MANAGEMENT
# BY, MAHESHWAR, AKSHAT AND ADITYA


stocka = 0
stockb = 0
stockc = 0


def addition1():
    global stocka

    def decimal_to_binary(decimal):
        if decimal == 0:
            return "0"
        binary = ""
        while decimal > 0:
            remainder = decimal % 2
            binary = str(remainder) + binary
            decimal = decimal // 2
        return binary

    def binary_to_decimal(binary_str):
        decimal_value = 0
        power = 0

        # Start from the rightmost (least significant) bit
        for bit in reversed(binary_str):
            if bit == '1':
                decimal_value += 2 ** power
            power += 1

        return decimal_value

    def binary_addition(bin1, bin2):
        max_len = max(len(bin1), len(bin2))
        bin1 = bin1.zfill(max_len)
        bin2 = bin2.zfill(max_len)

        carry = 0
        result = []

        for i in range(max_len - 1, -1, -1):
            bit1 = int(bin1[i])
            bit2 = int(bin2[i])

            # Calculate the sum and carry
            bit_sum = bit1 + bit2 + carry
            result.append(str(bit_sum % 2))
            carry = bit_sum // 2

        if carry:
            result.append('1')

        result.reverse()
        return ''.join(result)

    decimal_num1 = stocka
    decimal_num2 = int(input("Enter how many stocks you want to buy: "))

    binary_num1 = decimal_to_binary(decimal_num1)
    binary_num2 = decimal_to_binary(decimal_num2)

    result = binary_addition(binary_num1, binary_num2)
    decimal_value = binary_to_decimal(result)

    print(f"The sum of {decimal_num1} and {decimal_num2} in binary is: {result}")
    print(f"The sum in decimal is: {decimal_value}")
    max_len = max(len(binary_num1), len(binary_num2), len(result))
    binary_num1 = binary_num1.zfill(max_len)
    binary_num2 = binary_num2.zfill(max_len)
    result = result.zfill(max_len)

    print("\nBinary Addition Table:")
    print(f"{'A'.rjust(max_len + 2)}")
    print(f"{binary_num1.rjust(max_len + 2)}")
    print(f"+ {'B'.rjust(max_len + 1)}")
    print(f"{binary_num2.rjust(max_len + 2)}")
    print(f"{'-' * (max_len + 2)}")
    print(f"{result.rjust(max_len + 2)}")
    stocka = decimal_value


def boothmulti2():
    global stockb

    def conversion(a):  # returns a binary string of a number which has bits equal to count
        q = ""
        current_n = len(a)
        temp = count - current_n
        if (current_n != count):
            q = "0" * temp + a
        return q

    def add(x, y):  # fun to add two binary number strings
        max_len = max(len(x), len(y))
        result = ''
        carry = 0
        for i in range(max_len - 1, -1, -1):
            r = carry
            if x[i] == '1':
                r += 1
            if y[i] == '1':
                r += 1
            if r % 2 == 1:
                result = "1" + result
            else:
                result = "0" + result
            if r < 2:
                carry = 0
            else:
                carry = 1
        return result

    def twoc(a):
        l = list(a)
        for i in range(len(l)):
            if l[i] == "1":
                l[i] = "0"
            else:
                l[i] = "1"
        b = "0" * (len(l) - 1) + "1"
        return add("".join(l), b)

    def right_shift(ac, q, q1):
        a = ac[0]
        for i in range(1, len(ac)):
            a += ac[i - 1]
        b = ac[-1]
        for j in range(1, len(q)):
            b += q[j - 1]
        c = q[-1]
        return a, b, c

    # Taking input and assigning values
    x = stockb
    y = int(input("Enter the current per stock pricing: "))  # taking x and y decimal numbers as input for x * y
    a = bin(x).replace("0b", "")
    b = bin(y).replace("0b", "")
    negative_a = 0
    negative_b = 0
    if (a[0] == "-"):
        a = a.replace("-", "")
        negative_a = 1
    if (b[0] == "-"):
        b = b.replace("-", "")
        negative_b = 1

    if (len(a) > len(b)):
        count = len(a) + 1
    else:
        count = len(b) + 1
    count1 = count
    firstP = conversion(a)  # contains the positive representation of the multiplicand
    secondP = conversion(b)  # contains the positive representation of the multiplier
    firstN = twoc(firstP)  # contains 2's complement of the multiplicand
    secondN = twoc(secondP)  # contains 2's complement of the multiplier

    # BOOTH ALGO IMPLEMENTATION
    if negative_a == 0:
        M = firstP  # M is the multiplicand and M2 contains its 2's complement
        M2 = firstN
    else:
        M = firstN
        M2 = firstP
    if negative_b == 0:
        Q = secondP  # Q is the multiplier
    else:
        Q = secondN
    AC = conversion("0")
    Q1 = "0"  # one bit for comparision
    print("The table for the booth's algorithm is as follow:")
    print("Count" + " " * count1 + "AC" + " " * count1 + "Q" + " " * count1 + "Q1" + " " * count1 + "Operation")
    print(str(count) + " " * count1 + AC + " " * count1 + Q + " " * count1 + Q1 + " " * count1 + "initial")
    print("\n")

    while (count > 0):
        compare = Q[-1] + Q1
        if compare[0] == compare[-1]:
            AC, Q, Q1 = right_shift(AC, Q, Q1)
            Op = "right shift"
        elif compare == "10":
            AC = add(AC, M2)
            AC, Q, Q1 = right_shift(AC, Q, Q1)
            Op = "AC=AC-M and right shift"
        elif compare == "01":
            AC = add(AC, M)
            AC, Q, Q1 = right_shift(AC, Q, Q1)
            Op = "AC=AC+M and right shift"

        print(str(count) + " " * count1 + AC + " " * count1 + Q + " " * count1 + Q1 + " " * count1 + Op)
        print("\n")
        count = count - 1
    answer = AC + Q
    if negative_a == negative_b:
        ans_d = str(int(answer, 2))
    else:
        ans_d = "-" + str(int(twoc(answer), 2))

    print("The product in binary is:" + answer)
    print("Decimal conversion:" + ans_d)


def boothmulti1():
    global stocka

    def conversion(a):  # returns a binary string of a number which has bits equal to count
        q = ""
        current_n = len(a)
        temp = count - current_n
        if (current_n != count):
            q = "0" * temp + a
        return q

    def add(x, y):  # fun to add two binary number strings
        max_len = max(len(x), len(y))
        result = ''
        carry = 0
        for i in range(max_len - 1, -1, -1):
            r = carry
            if x[i] == '1':
                r += 1
            if y[i] == '1':
                r += 1
            if r % 2 == 1:
                result = "1" + result
            else:
                result = "0" + result
            if r < 2:
                carry = 0
            else:
                carry = 1
        return result

    def twoc(a):
        l = list(a)
        for i in range(len(l)):
            if l[i] == "1":
                l[i] = "0"
            else:
                l[i] = "1"
        b = "0" * (len(l) - 1) + "1"
        return add("".join(l), b)

    def right_shift(ac, q, q1):
        a = ac[0]
        for i in range(1, len(ac)):
            a += ac[i - 1]
        b = ac[-1]
        for j in range(1, len(q)):
            b += q[j - 1]
        c = q[-1]
        return a, b, c

    # Taking input and assigning values
    x = stocka
    y = int(input("Enter the current per stock pricing: "))  # taking x and y decimal numbers as input for x * y
    a = bin(x).replace("0b", "")
    b = bin(y).replace("0b", "")
    negative_a = 0
    negative_b = 0
    if (a[0] == "-"):
        a = a.replace("-", "")
        negative_a = 1
    if (b[0] == "-"):
        b = b.replace("-", "")
        negative_b = 1

    if (len(a) > len(b)):
        count = len(a) + 1
    else:
        count = len(b) + 1
    count1 = count
    firstP = conversion(a)  # contains the positive representation of the multiplicand
    secondP = conversion(b)  # contains the positive representation of the multiplier
    firstN = twoc(firstP)  # contains 2's complement of the multiplicand
    secondN = twoc(secondP)  # contains 2's complement of the multiplier

    # BOOTH ALGO IMPLEMENTATION
    if negative_a == 0:
        M = firstP  # M is the multiplicand and M2 contains its 2's complement
        M2 = firstN
    else:
        M = firstN
        M2 = firstP
    if negative_b == 0:
        Q = secondP  # Q is the multiplier
    else:
        Q = secondN
    AC = conversion("0")
    Q1 = "0"  # one bit for comparision
    print("The table for the booth's algorithm is as follow:")
    print("Count" + " " * count1 + "AC" + " " * count1 + "Q" + " " * count1 + "Q1" + " " * count1 + "Operation")
    print(str(count) + " " * count1 + AC + " " * count1 + Q + " " * count1 + Q1 + " " * count1 + "initial")
    print("\n")

    while (count > 0):
        compare = Q[-1] + Q1
        if compare[0] == compare[-1]:
            AC, Q, Q1 = right_shift(AC, Q, Q1)
            Op = "right shift"
        elif compare == "10":
            AC = add(AC, M2)
            AC, Q, Q1 = right_shift(AC, Q, Q1)
            Op = "AC=AC-M and right shift"
        elif compare == "01":
            AC = add(AC, M)
            AC, Q, Q1 = right_shift(AC, Q, Q1)
            Op = "AC=AC+M and right shift"

        print(str(count) + " " * count1 + AC + " " * count1 + Q + " " * count1 + Q1 + " " * count1 + Op)
        print("\n")
        count = count - 1
    answer = AC + Q
    if negative_a == negative_b:
        ans_d = str(int(answer, 2))
    else:
        ans_d = "-" + str(int(twoc(answer), 2))

    print("The product in binary is:" + answer)
    print("Decimal conversion:" + ans_d)


def boothmulti3():
    global stockc

    def conversion(a):  # returns a binary string of a number which has bits equal to count
        q = ""
        current_n = len(a)
        temp = count - current_n
        if (current_n != count):
            q = "0" * temp + a
        return q

    def add(x, y):  # fun to add two binary number strings
        max_len = max(len(x), len(y))
        result = ''
        carry = 0
        for i in range(max_len - 1, -1, -1):
            r = carry
            if x[i] == '1':
                r += 1
            if y[i] == '1':
                r += 1
            if r % 2 == 1:
                result = "1" + result
            else:
                result = "0" + result
            if r < 2:
                carry = 0
            else:
                carry = 1
        return result

    def twoc(a):
        l = list(a)
        for i in range(len(l)):
            if l[i] == "1":
                l[i] = "0"
            else:
                l[i] = "1"
        b = "0" * (len(l) - 1) + "1"
        return add("".join(l), b)

    def right_shift(ac, q, q1):
        a = ac[0]
        for i in range(1, len(ac)):
            a += ac[i - 1]
        b = ac[-1]
        for j in range(1, len(q)):
            b += q[j - 1]
        c = q[-1]
        return a, b, c

    # Taking input and assigning values
    x = stockc
    y = int(input("Enter the current per stock pricing: "))  # taking x and y decimal numbers as input for x * y
    a = bin(x).replace("0b", "")
    b = bin(y).replace("0b", "")
    negative_a = 0
    negative_b = 0
    if (a[0] == "-"):
        a = a.replace("-", "")
        negative_a = 1
    if (b[0] == "-"):
        b = b.replace("-", "")
        negative_b = 1

    if (len(a) > len(b)):
        count = len(a) + 1
    else:
        count = len(b) + 1
    count1 = count
    firstP = conversion(a)  # contains the positive representation of the multiplicand
    secondP = conversion(b)  # contains the positive representation of the multiplier
    firstN = twoc(firstP)  # contains 2's complement of the multiplicand
    secondN = twoc(secondP)  # contains 2's complement of the multiplier

    # BOOTH ALGO IMPLEMENTATION
    if negative_a == 0:
        M = firstP  # M is the multiplicand and M2 contains its 2's complement
        M2 = firstN
    else:
        M = firstN
        M2 = firstP
    if negative_b == 0:
        Q = secondP  # Q is the multiplier
    else:
        Q = secondN
    AC = conversion("0")
    Q1 = "0"  # one bit for comparision
    print("The table for the booth's algorithm is as follow:")
    print("Count" + " " * count1 + "AC" + " " * count1 + "Q" + " " * count1 + "Q1" + " " * count1 + "Operation")
    print(str(count) + " " * count1 + AC + " " * count1 + Q + " " * count1 + Q1 + " " * count1 + "initial")
    print("\n")

    while (count > 0):
        compare = Q[-1] + Q1
        if compare[0] == compare[-1]:
            AC, Q, Q1 = right_shift(AC, Q, Q1)
            Op = "right shift"
        elif compare == "10":
            AC = add(AC, M2)
            AC, Q, Q1 = right_shift(AC, Q, Q1)
            Op = "AC=AC-M and right shift"
        elif compare == "01":
            AC = add(AC, M)
            AC, Q, Q1 = right_shift(AC, Q, Q1)
            Op = "AC=AC+M and right shift"

        print(str(count) + " " * count1 + AC + " " * count1 + Q + " " * count1 + Q1 + " " * count1 + Op)
        print("\n")
        count = count - 1
    answer = AC + Q
    if negative_a == negative_b:
        ans_d = str(int(answer, 2))
    else:
        ans_d = "-" + str(int(twoc(answer), 2))

    print("The product in binary is:" + answer)
    print("Decimal conversion:" + ans_d)


# DIVISION RESTORING ALGORITHM
def restoringdivi():
    # CONVERTS DECIMAL TO BINARY
    def binary(a):  # converts decimal to binary
        bits_list = []

        while (a > 0):
            num = a
            b = int(num % 2)
            bits_list.append(b)
            num = num // 2
            a = int(a / 2)
        # print(bits_list)
        bits_list.reverse()
        return bits_list;

    # LEFT SHIFT OPERATION
    def Shift(shiftA, shiftQ):

        val = shiftA + shiftQ
        l = len(val)
        i = 0

        '''while(i<l-1):
            val[i]=val[i+1]
            i=i+1
        val[i]=0
        return val
    '''
        for i in range(0, l - 1):
            val[i] = 0
            val[i] = val[i + 1]
        del val[i]
        return val

    # TAKES 2's COMPLIMENT (REQD FOR "-M")
    def compliment(value):
        onecomp = []
        twocomp = []
        for i in range(0, len(value)):
            if value[i] == 0:
                onecomp.append(1)
            elif value[i] == 1:
                onecomp.append(0)

        carry = 1
        for j in range(len(value) - 1, -1, -1):

            if (onecomp[j] == 0 and carry == 1):
                twocomp.append(1)
                carry = 0
            elif (onecomp[j] == 1 and carry == 1):
                twocomp.append(0)
                carry = 1
            elif (onecomp[j] == 0 and carry == 0):
                twocomp.append(0)
                carry = 0
            elif (onecomp[j] == 1 and carry == 0):
                twocomp.append(1)
                carry = 0
        twocomp.reverse()
        return twocomp

    # ADDING TWO BINARY NOS.
    def Add(valA, valM):
        add = []
        ad = valA
        carry = 0
        for i in range(len(ad) - 1, -1, -1):
            if (valA[i] == 0 and valM[i] == 0 and carry == 0):
                add.append(0)
                carry = 0
            elif (valA[i] == 0 and valM[i] == 0 and carry == 1):
                add.append(1)
                carry = 0
            elif (valA[i] == 0 and valM[i] == 1 and carry == 0):
                add.append(1)
                carry = 0
            elif (valA[i] == 0 and valM[i] == 1 and carry == 1):
                add.append(0)
                carry = 1
            elif (valA[i] == 1 and valM[i] == 0 and carry == 0):
                add.append(1)
                carry = 0
            elif (valA[i] == 1 and valM[i] == 0 and carry == 1):
                add.append(0)
                carry = 1
            elif (valA[i] == 1 and valM[i] == 1 and carry == 0):
                add.append(0)
                carry = 1
            elif (valA[i] == 1 and valM[i] == 1 and carry == 1):
                add.append(1)
                carry = 1
        add.reverse()
        return add

    # CONVERTS BINARY TO DECIMAL
    def decimal(bin):
        bin.reverse()
        dec = 0
        for i in range(0, len(bin)):
            if (bin[i] == 1):
                dec = dec + (bin[i] * (2 ** i))
            elif (bin[i] == 0):
                pass
        bin.reverse()
        return dec

    print("      DIVISION RESTORING ALGORITHM     ")
    print("")
    dividend = int(input("Enter the money you want to invest -> Q : "))
    divisor = int(input("Enter the value of the stocks -> M : "))
    print("")
    print("")

    q = binary(dividend)
    m = binary(divisor)

    print("Q : ", *q)

    # SETTING THE M VALUE : i.e. len(M) should be 1 more than len(Q)
    if len(m) < len(q):
        diff = len(q) - len(m)
        for i in range(0, diff + 1):
            m.insert(0, 0)
    print("M : ", *m)

    # ASSIGNING VALUE OF A to 0
    ACC = []
    for i in range(0, len(m)):
        ACC.append(0)
    print("A : ", *ACC)

    # VALUE OF -M
    negM = compliment(m)
    print("-M : ", *negM)
    print("")

    """
    #LEFT SHIFT A, Q
    a = Shift(ACC,q)
    print(*a)

    #TAKING THE "A" part from the AQ 
    newA=a[0:len(ACC)]
    print(*newA)
    """  # Ignore this comment

    print("          ", "    |   ", "   A    ", "    |    ", "   Q  ", "    |    ")
    print("--------------------------------------------------------")
    n = 1
    # No of iterations
    counter = len(q)
    while counter > 0:

        # LEFT SHIFT A, Q
        a = Shift(ACC, q)
        # print(*a)

        # TAKING THE "A" AND "Q" PART FROM THE "a"
        newA = a[0:len(ACC)]
        newQ = a[len(ACC):]
        # print(*newA)
        # print(*newQ)

        # A<-A-M
        sumAM = Add(newA, negM)
        # print(*sumAM)

        b = len(newQ) + 1
        if (sumAM[0] == 1):  # MSB(A)=1
            newQ.insert(b, 0)
            sumAM = Add(sumAM, m)
        elif (sumAM[0] == 0):  # MSB(A)=0
            newQ.insert(b, 1)

        ACC = sumAM
        q = newQ

        print("Step : ", n, "    |    ", *ACC, "    |    ", *q, "  |  ")

        print("--------------------------------------------------")
        n = n + 1
        counter = counter - 1

    print("Quotient: ", *q, "  ->  ", decimal(q))
    print("Remainder: ", *ACC, "  ->  ", decimal(ACC))
    print("You can buy these many Stocks for A,B and C each: ", *q, "  ->  ", decimal(q) / 3)


def subtract1():
    global stocka

    def decimal_to_binary(decimal):
        if decimal == 0:
            return "0"
        binary = ""
        while decimal > 0:
            remainder = decimal % 2
            binary = str(remainder) + binary
            decimal = decimal // 2
        return binary

    def binary_to_decimal(binary_str):
        decimal_value = 0
        power = 0

        # Start from the rightmost (least significant) bit
        for bit in reversed(binary_str):
            if bit == '1':
                decimal_value += 2 ** power
            power += 1

        return decimal_value

    def binary_addition(bin1, bin2):
        max_len = max(len(bin1), len(bin2))
        bin1 = bin1.zfill(max_len)
        bin2 = bin2.zfill(max_len)

        carry = 0
        result = []

        for i in range(max_len - 1, -1, -1):
            bit1 = int(bin1[i])
            bit2 = int(bin2[i])

            # Calculate the sum and carry
            bit_sum = bit1 + bit2 + carry
            result.append(str(bit_sum % 2))
            carry = bit_sum // 2

        if carry:
            result.append('1')

        result.reverse()
        return ''.join(result)

    def binary_subtraction(bin1, bin2):
        max_len = max(len(bin1), len(bin2))
        bin1 = bin1.zfill(max_len)
        bin2 = bin2.zfill(max_len)

        borrow = 0
        result = []

        for i in range(max_len - 1, -1, -1):
            bit1 = int(bin1[i])
            bit2 = int(bin2[i])

            # Calculate the difference and borrow
            bit_diff = bit1 - bit2 - borrow

            if bit_diff < 0:
                bit_diff += 2
                borrow = 1
            else:
                borrow = 0

            result.append(str(bit_diff))

        result.reverse()
        return ''.join(result)

    decimal_num1 = stocka
    decimal_num2 = int(input("Enter the second decimal number: "))

    binary_num1 = decimal_to_binary(decimal_num1)
    binary_num2 = decimal_to_binary(decimal_num2)

    # Perform binary subtraction
    result = binary_subtraction(binary_num1, binary_num2)

    # Call binary_to_decimal to convert the binary subtraction result back to decimal
    decimal_value = binary_to_decimal(result)

    print(f"The subtraction of {decimal_num1} and {decimal_num2} in binary is: {result}")
    print(f"The difference in decimal is: {decimal_value}")
    stocka = decimal_value


def subtract2():
    global stocka

    def decimal_to_binary(decimal):
        if decimal == 0:
            return "0"
        binary = ""
        while decimal > 0:
            remainder = decimal % 2
            binary = str(remainder) + binary
            decimal = decimal // 2
        return binary

    def binary_to_decimal(binary_str):
        decimal_value = 0
        power = 0

        # Start from the rightmost (least significant) bit
        for bit in reversed(binary_str):
            if bit == '1':
                decimal_value += 2 ** power
            power += 1

        return decimal_value

    def binary_addition(bin1, bin2):
        max_len = max(len(bin1), len(bin2))
        bin1 = bin1.zfill(max_len)
        bin2 = bin2.zfill(max_len)

        carry = 0
        result = []

        for i in range(max_len - 1, -1, -1):
            bit1 = int(bin1[i])
            bit2 = int(bin2[i])

            # Calculate the sum and carry
            bit_sum = bit1 + bit2 + carry
            result.append(str(bit_sum % 2))
            carry = bit_sum // 2

        if carry:
            result.append('1')

        result.reverse()
        return ''.join(result)

    def binary_subtraction(bin1, bin2):
        max_len = max(len(bin1), len(bin2))
        bin1 = bin1.zfill(max_len)
        bin2 = bin2.zfill(max_len)

        borrow = 0
        result = []

        for i in range(max_len - 1, -1, -1):
            bit1 = int(bin1[i])
            bit2 = int(bin2[i])

            # Calculate the difference and borrow
            bit_diff = bit1 - bit2 - borrow

            if bit_diff < 0:
                bit_diff += 2
                borrow = 1
            else:
                borrow = 0

            result.append(str(bit_diff))

        result.reverse()
        return ''.join(result)

    decimal_num1 = stockb
    decimal_num2 = int(input("Enter the second decimal number: "))

    binary_num1 = decimal_to_binary(decimal_num1)
    binary_num2 = decimal_to_binary(decimal_num2)

    # Perform binary subtraction
    result = binary_subtraction(binary_num1, binary_num2)

    # Call binary_to_decimal to convert the binary subtraction result back to decimal
    decimal_value = binary_to_decimal(result)

    print(f"The subtraction of {decimal_num1} and {decimal_num2} in binary is: {result}")
    print(f"The difference in decimal is: {decimal_value}")
    stockb = decimal_value


def subtract3():
    global stockc

    def decimal_to_binary(decimal):
        if decimal == 0:
            return "0"
        binary = ""
        while decimal > 0:
            remainder = decimal % 2
            binary = str(remainder) + binary
            decimal = decimal // 2
        return binary

    def binary_to_decimal(binary_str):
        decimal_value = 0
        power = 0

        # Start from the rightmost (least significant) bit
        for bit in reversed(binary_str):
            if bit == '1':
                decimal_value += 2 ** power
            power += 1

        return decimal_value

    def binary_addition(bin1, bin2):
        max_len = max(len(bin1), len(bin2))
        bin1 = bin1.zfill(max_len)
        bin2 = bin2.zfill(max_len)

        carry = 0
        result = []

        for i in range(max_len - 1, -1, -1):
            bit1 = int(bin1[i])
            bit2 = int(bin2[i])

            # Calculate the sum and carry
            bit_sum = bit1 + bit2 + carry
            result.append(str(bit_sum % 2))
            carry = bit_sum // 2

        if carry:
            result.append('1')

        result.reverse()
        return ''.join(result)

    def binary_subtraction(bin1, bin2):
        max_len = max(len(bin1), len(bin2))
        bin1 = bin1.zfill(max_len)
        bin2 = bin2.zfill(max_len)

        borrow = 0
        result = []

        for i in range(max_len - 1, -1, -1):
            bit1 = int(bin1[i])
            bit2 = int(bin2[i])

            # Calculate the difference and borrow
            bit_diff = bit1 - bit2 - borrow

            if bit_diff < 0:
                bit_diff += 2
                borrow = 1
            else:
                borrow = 0

            result.append(str(bit_diff))

        result.reverse()
        return ''.join(result)

    decimal_num1 = stockc
    decimal_num2 = int(input("Enter the second decimal number: "))

    binary_num1 = decimal_to_binary(decimal_num1)
    binary_num2 = decimal_to_binary(decimal_num2)

    # Perform binary subtraction
    result = binary_subtraction(binary_num1, binary_num2)

    # Call binary_to_decimal to convert the binary subtraction result back to decimal
    decimal_value = binary_to_decimal(result)

    print(f"The subtraction of {decimal_num1} and {decimal_num2} in binary is: {result}")
    print(f"The difference in decimal is: {decimal_value}")
    stockc = decimal_value


def addition2():
    global stockb

    def decimal_to_binary(decimal):
        if decimal == 0:
            return "0"
        binary = ""
        while decimal > 0:
            remainder = decimal % 2
            binary = str(remainder) + binary
            decimal = decimal // 2
        return binary

    def binary_to_decimal(binary_str):
        decimal_value = 0
        power = 0

        # Start from the rightmost (least significant) bit
        for bit in reversed(binary_str):
            if bit == '1':
                decimal_value += 2 ** power
            power += 1

        return decimal_value

    def binary_addition(bin1, bin2):
        max_len = max(len(bin1), len(bin2))
        bin1 = bin1.zfill(max_len)
        bin2 = bin2.zfill(max_len)

        carry = 0
        result = []

        for i in range(max_len - 1, -1, -1):
            bit1 = int(bin1[i])
            bit2 = int(bin2[i])

            # Calculate the sum and carry
            bit_sum = bit1 + bit2 + carry
            result.append(str(bit_sum % 2))
            carry = bit_sum // 2

        if carry:
            result.append('1')

        result.reverse()
        return ''.join(result)

    decimal_num1 = stockb
    decimal_num2 = int(input("Enter how many stocks you want to buy: "))

    binary_num1 = decimal_to_binary(decimal_num1)
    binary_num2 = decimal_to_binary(decimal_num2)

    result = binary_addition(binary_num1, binary_num2)
    decimal_value = binary_to_decimal(result)

    print(f"The sum of {decimal_num1} and {decimal_num2} in binary is: {result}")
    print(f"The sum in decimal is: {decimal_value}")
    stockb = decimal_value


def addition3():
    global stockc

    def decimal_to_binary(decimal):
        if decimal == 0:
            return "0"
        binary = ""
        while decimal > 0:
            remainder = decimal % 2
            binary = str(remainder) + binary
            decimal = decimal // 2
        return binary

    def binary_to_decimal(binary_str):
        decimal_value = 0
        power = 0

        # Start from the rightmost (least significant) bit
        for bit in reversed(binary_str):
            if bit == '1':
                decimal_value += 2 ** power
            power += 1

        return decimal_value

    def binary_addition(bin1, bin2):
        max_len = max(len(bin1), len(bin2))
        bin1 = bin1.zfill(max_len)
        bin2 = bin2.zfill(max_len)

        carry = 0
        result = []

        for i in range(max_len - 1, -1, -1):
            bit1 = int(bin1[i])
            bit2 = int(bin2[i])

            # Calculate the sum and carry
            bit_sum = bit1 + bit2 + carry
            result.append(str(bit_sum % 2))
            carry = bit_sum // 2

        if carry:
            result.append('1')

        result.reverse()
        return ''.join(result)

    decimal_num1 = stockc
    decimal_num2 = int(input("Enter how many stocks you want to buy: "))

    binary_num1 = decimal_to_binary(decimal_num1)
    binary_num2 = decimal_to_binary(decimal_num2)

    result = binary_addition(binary_num1, binary_num2)
    decimal_value = binary_to_decimal(result)

    print(f"The sum of {decimal_num1} and {decimal_num2} in binary is: {result}")
    print(f"The sum in decimal is: {decimal_value}")
    stockc = decimal_value


# MAIN
stocka = 0
stockb = 0
stockc = 0
print("Hey User! Welcome to the Real-Time Financial Portfolio Management System. ")
while (True):
    print('''1. Buy Stock
2. Sell Stock
3. Value of your Stocks
4. Diversification of Stocks
5. Display Stocks
6. Quit''')
    ch = int(input("Enter your choice: "))
    if ch == 1:
        print('''1. Stock A
2. Stock B
3. Stock C''')
        ch1 = int(input("Enter your choice: "))
        if ch1 == 1:
            addition1()
        elif ch1 == 2:
            addition2()
        elif ch1 == 3:
            addition3()
        else:
            print('Enter a valid stock!')
    elif ch == 2:
        print('''Which Stock you want to Sell?
1. Stock A
2. Stock B
3. Stock C''')
        ch1 = int(input("Enter your choice: "))
        if ch1 == 1:
            subtract1()
        elif ch1 == 2:
            subtract2()
        elif ch1 == 3:
            subtract3()
        else:
            print("Enter a valid stock!")
    elif ch == 3:
        print('''Which stock you want to see value of?
1. Stock A
2. Stock B
3. Stock C''')
        ch1 = int(input("Enter your choice: "))
        if ch1 == 1:
            boothmulti1()
        elif ch1 == 2:
            boothmulti2()
        elif ch1 == 3:
            boothmulti3()
        else:
            print("Enter a valid stock!")
    elif ch == 4:
        restoringdivi()
    elif ch == 5:
        print("Stock A: ", stocka)
        print("Stock B: ", stockb)
        print("Stock C: ", stockc)
    elif ch == 6:
        print("Thank you, Have a good day!")
        break
    else:
        print("Enter a valid choice")
