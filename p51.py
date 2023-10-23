from funcs import in_primes
primes = in_primes()
def main():
    done = False
    for num_digits in range(2, 10):
        #print("starting", num_digits)
        if done:
            return ""
        for number in range(10 ** (num_digits - 1), 10 ** num_digits):
            for replace_count in range(1, num_digits):
                if replace_count == 1:
                    for a in range(num_digits):
                        if not((number%2 == 0  or number % 5==0) and a != num_digits):
                            total = 0
                            my_lis = []
                            for letter in str(number):
                                my_lis.append(letter)
                            for digit in range(10):
                                my_lis.pop(a)
                                my_lis.insert(a, digit)
                                full = ""
                                for dig in my_lis:
                                    full = "".join([full, str(dig)])
                                if int(full) in primes and int(my_lis[0]) != 0:
                                    total += 1
                                    if total == 8:
                                        for digit in range(10):
                                            my_lis.pop(a)
                                            my_lis.insert(a, digit)
                                            full = ""
                                            for dig in my_lis:
                                                full = "".join([full, str(dig)])
                                            if int(full) in primes and int(my_lis[0]) != 0:
                                                print(full)
                                                #print(a)
                                                done = True
                                                return ""
                                if int(digit) - total > 1:
                                    break

                if replace_count == 2:
                    for a in range(num_digits):
                        for b in range(num_digits):
                            if b > a and not((number%2 == 0 or number % 5==0) and b != num_digits):
                                total = 0
                                my_lis = []
                                for letter in str(number):
                                    my_lis.append(letter)
                                for digit in range(10):
                                    my_lis.pop(a)
                                    my_lis.insert(a, digit)
                                    my_lis.pop(b)
                                    my_lis.insert(b, digit)
                                    full = ""
                                    for dig in my_lis:
                                        full = "".join([full, str(dig)])
                                    if int(full) in primes and int(my_lis[0]) != 0:
                                        total += 1
                                        if total == 8:
                                            for digit in range(10):
                                                my_lis.pop(a)
                                                my_lis.insert(a, digit)
                                                my_lis.pop(b)
                                                my_lis.insert(b, digit)
                                                full = ""
                                                for dig in my_lis:
                                                    full = "".join([full, str(dig)])
                                                if int(full) in primes and int(my_lis[0]) != 0:
                                                    print(full)
                                                    #print(a,b)
                                                    done = True
                                                    return ""
                                    if int(digit) - total > 1:
                                        break

                if replace_count == 3:
                    for a in range(num_digits):
                        for b in range(num_digits):
                            for c in range(num_digits):
                                if b > a and c > b and not((number%2 == 0 or number % 5 == 0) and c != num_digits):
                                    total = 0
                                    my_lis = []
                                    for letter in str(number):
                                        my_lis.append(letter)
                                    for digit in range(10):
                                        my_lis.pop(a)
                                        my_lis.insert(a, digit)
                                        my_lis.pop(b)
                                        my_lis.insert(b, digit)
                                        my_lis.pop(c)
                                        my_lis.insert(c, digit)
                                        full = ""
                                        for dig in my_lis:
                                            full = "".join([full, str(dig)])
                                        if int(full) in primes and int(my_lis[0]) != 0:
                                            total += 1
                                            if total == 8:
                                                for digit in range(10):
                                                    my_lis.pop(a)
                                                    my_lis.insert(a, digit)
                                                    my_lis.pop(b)
                                                    my_lis.insert(b, digit)
                                                    my_lis.pop(c)
                                                    my_lis.insert(c, digit)
                                                    full = ""
                                                    for dig in my_lis:
                                                        full = "".join([full, str(dig)])
                                                    if int(full) in primes and int(my_lis[0]) != 0:
                                                        print(full)
                                                        #print(a,b,c)
                                                        done = True
                                                        return ""
                                        if int(digit) - total > 1:
                                            break

                if replace_count == 4:
                    for a in range(num_digits):
                        for b in range(num_digits):
                            for c in range(num_digits):
                                for d in range(num_digits):
                                    if b > a and c > b and d > c and not((number % 2 == 0 or number % 5 == 0) and d != num_digits):
                                        total = 0
                                        my_lis = []
                                        for letter in str(number):
                                            my_lis.append(letter)
                                        for digit in range(10):
                                            my_lis.pop(a)
                                            my_lis.insert(a, digit)
                                            my_lis.pop(b)
                                            my_lis.insert(b, digit)
                                            my_lis.pop(c)
                                            my_lis.insert(c, digit)
                                            my_lis.pop(d)
                                            my_lis.insert(d, digit)
                                            full = ""
                                            for dig in my_lis:
                                                full = "".join([full, str(dig)])
                                            if int(full) in primes and int(my_lis[0]) != 0:
                                                total += 1
                                                if total == 8:
                                                    for digit in range(10):
                                                        my_lis.pop(a)
                                                        my_lis.insert(a, digit)
                                                        my_lis.pop(b)
                                                        my_lis.insert(b, digit)
                                                        my_lis.pop(c)
                                                        my_lis.insert(c, digit)
                                                        my_lis.pop(d)
                                                        my_lis.insert(d, digit)
                                                        full = ""
                                                        for dig in my_lis:
                                                            full = "".join([full, str(dig)])
                                                        if int(full) in primes and int(my_lis[0]) != 0:
                                                            print(full)
                                                            #print(a,b,c,d)
                                                            done = True
                                                            return ""
                                            if int(digit) - total > 1:
                                                break

                if replace_count == 5:
                    for a in range(num_digits):
                        for b in range(num_digits):
                            for c in range(num_digits):
                                for d in range(num_digits):
                                    for e in range(num_digits):
                                        if b > a and c > b and d > c and e > d  and not((number%2 == 0 or number % 5 == 0) and e!= num_digits):
                                            total = 0
                                            my_lis = []
                                            for letter in str(number):
                                                my_lis.append(letter)
                                            for digit in range(10):
                                                my_lis.pop(a)
                                                my_lis.insert(a, digit)
                                                my_lis.pop(b)
                                                my_lis.insert(b, digit)
                                                my_lis.pop(c)
                                                my_lis.insert(c, digit)
                                                my_lis.pop(d)
                                                my_lis.insert(d, digit)
                                                my_lis.pop(e)
                                                my_lis.insert(e, digit)
                                                full = ""
                                                for dig in my_lis:
                                                    full = "".join([full, str(dig)])
                                                if int(full) in primes and int(my_lis[0]) != 0:
                                                    total += 1
                                                    if total == 8:
                                                        for dig in range(10):
                                                            my_lis.pop(a)
                                                            my_lis.insert(a, digit)
                                                            my_lis.pop(b)
                                                            my_lis.insert(b, digit)
                                                            my_lis.pop(c)
                                                            my_lis.insert(c, digit)
                                                            my_lis.pop(d)
                                                            my_lis.insert(d, digit)
                                                            my_lis.pop(e)
                                                            my_lis.insert(e, digit)
                                                            full = ""
                                                            for dig in my_lis:
                                                                full = "".join([full, str(dig)])
                                                            if int(full) in primes and int(my_lis[0]) != 0:
                                                                print(full)
                                                                #print(a,b,c,d,e)
                                                                done = True
                                                                return ""
                                                if int(digit) - total > 1:
                                                    break


main()