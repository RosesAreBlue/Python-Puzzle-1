level = int(input("What level of triangle do you want? "))
char1 = input("Pick a char: ")
char2 = input("Pick another char: ")
innermost_Width = int(input("What is the innermost width? "))

def triangle(lvl, width, c1, c2): #for loop solution
    t = []
    
    #initial level (level 1)
    for i in range(int((width+1)/2)):
        t.append(c1*(width - 2*i))

    #levels beyond level 1    
    for i in range(lvl-1): #0
        if i%2 == 0:
            for i, line in enumerate(t):
                t[i] = c2*(2*i+1) + line + c2*(2*i+1)

            len_num = len(t[0])
            
            for i in range(len(t)):
                t = [c2*(len_num - 2*(i+1))] + t
        else:
            n = len(t[-1])
            for i, line in enumerate(t):
                t[i] = c1*(n-2*i) + line + c1*(n-2*i)

            len_num = len(t[-1])
            for i in range(len(t)):
                t = t + [c1*(len_num - 2*(i+1))]          

    #print lines
    pattern = list(range(len(t)))
    
    if lvl%2 == 0:
        pattern = list(reversed(pattern))
    
    for i, line in enumerate(t):
        spaces = " "*pattern[i]
        print(spaces + line + spaces)

triangle(level, innermost_Width, char1, char2)
