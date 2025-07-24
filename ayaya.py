def Fib(n):
    k = 1
    l = 1
    for i in range(n-2):
        p = l
        l = l + k
        k = p
    return l
asd = 'sug'
n   = 20000
print('jo')
print("Calculating something...\n")
print(f"Fib. number {n}:\n{Fib(20000)}")
print('re')
def rand_generator(seed, N=10**6, a=0, b=10, integer = True):
    '''For a given seed, this function returns N pseudo-random between a and b'''
    rands =[]
    if integer:
        for i in range(N):
            num = int(a+(b-a)*(abs(hash(str(hash(str(seed)+str(i+1)))))%10**13)/10**13)
            rands.append(num)
        return rands
    else:
        for i in range(N):
            num = a+(b-a)*(abs(hash(str(hash(str(seed)+str(i+1)))))%10**13)/10**13
            rands.append(num)
        return rands

print("According to all known laws of aviation, there is no way a bee should be able to fly.")
print("Its wings are too small to get its fat little body off the ground.")
print("The bee, of course, flies anyway because bees don't care what humans think is impossible.")
print("Yellow, black. Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Let's shake it up a little.")
print("Barry! Breakfast is ready!")
print("Coming!")
print("Hang on a second... Hello?")
print("- Barry?")
print("- Adam?")
print("- Can you believe this is happening?")
print("- I can't. I'll pick you up.")
print("Looking sharp.")
print("Use the stairs. Your father paid good money for those.")
print("Sorry, I'm excited.")
print("Here's the graduate. We're very proud of you, son.")
print("A perfect report card, all B's!")
print("Very proud.")
print("Ma! I got a think going here.")
print("- You got lint on your fuzz.")
print("- Ow! That's me!")
print("- Wave to us! We'll be in row 118,000!")
print("- Bye!")
print("Barry, I told you,")
print("stop flying in the house!")
print("- Hey, Adam.")
print("- Hey, Barry.")
print("- Is that fuzz gel?")
print("- A little. Special day, graduation.") 
print("Never thought I'd make it.")
print("Three days grade school,")
print("three days high school.")
print("Those were awkward.")
print("Three days college. I'm glad I took")
print("a day and hitchhiked around the hive.")
print("You did come back different.")
print("- Hi, Barry.")
print("- Artie, growing a mustache? Looks good.")
print("- Hear about Frankie?")
print("- Yeah.")
print("- You going to the funeral?")
print("- No, I'm not going.")
print("Everybody knows,")
print("sting someone, you die.")
print("Don't waste it on a squirrel.")
print("Such a hothead.")
print("I guess he could have")
print("just gotten out of the way.")
print("I love this incorporating")
print("an amusement park into our day.")
print("That's why we don't need vacations.")
print("Boy, quite a bit of pomp...")
print("under the circumstances.")
print("- Well, Adam, today we are men.")
print("- We are!")
print("- Bee-men.")
print("- Amen!")
print("Hallelujah!")
print("Students, faculty, distinguished bees,")
print("please welcome Dean Buzzwell.")
print("Welcome, New Hive Oity")
print("graduating class of...")
print("...9:15.")
print("That concludes our ceremonies.")
print("And begins your career")
print("at Honex Industries!")
print("Will we pick ourjob today?")
print("I heard it's just orientation.")
print("Heads up! Here we go.")
print("Keep your hands and antennas")
print("inside the tram at all times.")
print("- Wonder what it'll be like?")
print("- A little scary.")
print("Welcome to Honex,")
print("a division of Honesco")
print("and a part of the Hexagon Group.")
print("This is it!")
print("Wow.")
print("Wow.")
print("We know that you, as a bee,")
print("have worked your whole life")
print("to get to the point where you")
print("can work for your whole life.")
print("Honey begins when our valiant Pollen..........................................")

print('nce')

print(f"{Fib(69)} pseudo-random integer numbers between 0 and 1000:")
print(rand_generator(Fib(69), 1000, 0, 1000, True))
print('fe')
def itob(N):
    s = ''
    while N > 1:
        s = str(N%2) + s
        N = N//2
    s = str(N) + s
    return s

def bingap(N):
    gap = 0
    tmp = -1
    while N > 1:
        r = N%2        
        if r == 1:
            if tmp > gap:
                gap = tmp
            tmp = 0  
        elif tmp > -1:
            tmp += 1
        N //= 2
    if N == 1:
        if tmp > gap:
            gap = tmp
    return gap

def reverse(A, i, j):
    while i < j:
        tmp = A[j]
        A[j] = A[i]
        A[i] = tmp
        i+=1
        j-=1
    
def rotate(A, K):
    if A:
        K = K % len(A)
        if K > 0:
            reverse(A, 0, len(A)-1)
            reverse(A, 0, K-1)
            reverse(A, K, len(A)-1)
    return A

def tape_diff_slow(A):
    md = None
    for p in range(1, len(A)):
        d = abs(sum(A[:p])-sum(A[p:]))
        # print(d)
        md = d if md is None or d < md else md
    print('min diff: ' + str(md))


def tape_diff(A, n, s1, s2):
    if n < 0:
        return abs(s1-s2)
    else:
        inc = tape_diff(A, n-1, s1+A[n], s2)
        exc = tape_diff(A, n-1, s1, s2+A[n])
        return min(inc, exc)

def tape_diff_fast(A):
    return tape_diff(A, len(A)-1, 0, 0)

A = [3,1,2,4,3]
A = rand_generator(6969, 1000, -1000, 1000, True)

print(A)

print('jo')

def CRAZY(N):
    for i in range(N):
        if i == 69:
            print('re')
        print('Crazy? I was crazy once. They locked me in a room. A rubber room! A rubber room with rats,and rats make me crazy...')
CRAZY(105)