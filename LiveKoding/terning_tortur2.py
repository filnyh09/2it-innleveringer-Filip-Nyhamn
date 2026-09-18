t1 = 1
t2 = 1
t3 = 6
t4 = 6
t5 = 6

def terning():
    return (t1 - t2) * t3 * t4 * t5

print(terning())

t1 = 1
t2 = 2
t3 = 2
t4 = 5
t5 = 6

def terning2():
    print((t2 / t3) / ((t1 + t4) / t5))

terning2()

t1 = 1
t2 = 5
t3 = 5
t4 = 5
t5 = 5

def terning3():
    print(t1 + ((t2 / t3) / (t4 / t5)))

terning3()

t1 = 2
t2 = 3
t3 = 4
t4 = 5
t5 = 6

def terning4():
    return ((t3 + t4) - (t1 + t5)) * t2

print(terning3())