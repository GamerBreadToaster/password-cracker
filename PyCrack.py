import time, string, random, os, winsound

# default variables
letters = list(string.ascii_letters + string.digits)
psswrd_lengt = 0
filepath = "options.txt"
crack = False
times = 0

# defines

# reading options.txt
if os.path.isfile(filepath):
    with open(filepath, "r") as file:
        line = file.readlines()
else:
    with open(filepath, "w") as file:
        file.write("||random options||\n")
        file.write("password random:\n")
        file.write("False\n")
        file.write("random amount of letters:\n")
        file.write("False\n")
        file.write("amount of letters:\n")
        file.write("4\n")
        file.write("\n")
        file.write("||more options||\n")
        file.write("the program knows how many letters there are:\n")
        file.write("False\n")
    with open(filepath, 'r') as file:
        line = file.readlines()

# assigning variables
psswrd_random = False if line[2].strip() == 'False' else True
psswrd_random_amount = False if line[4].strip() == 'False' else True
if psswrd_random == True and psswrd_random_amount == True:
    psswrd_lengt = random.randrange(1,8)
elif psswrd_random == True and psswrd_random_amount == False:
    psswrd_lengt = int(line[6])
if psswrd_random == True:
    password = ""
    for i in range(psswrd_lengt):
        password += random.choice(letters) # password randomiser
letters_known = False if line[10].strip() == 'False' else True
if letters_known == False:
    psswrd_lengt = 1

    

# input of password
while (letters_known == False or psswrd_lengt < 1 or psswrd_lengt > 8) and psswrd_random == False:
    password = input("put password here: ")
    if letters_known == True:
        psswrd_lengt = len(password) # lengt of password
        print("Password lengt =",psswrd_lengt)
    else:
        break
print("password =",password)
os.system('pause')
os.system('cls')
print("i am busy")
print("password =",password)

# beginning of cracking the password:
time_begin = time.time()
if psswrd_lengt == 1:
    for a in letters:
        times +=1
        if a == password:
            crack = True
            break
    if crack == False:
        psswrd_lengt += 1

if psswrd_lengt == 2:
    for a in letters:
        if crack == True:
            break
        for b in letters:
            times +=1
            if (a+b) == password:
                crack = True
                break
    if crack == False:
        psswrd_lengt += 1
        
if psswrd_lengt == 3:
    for a in letters:
        if crack == True:
            break
        for b in letters:
            if crack == True:
                break
            for c in letters:
                times +=1
                if (a+b+c) == password:
                    crack = True
                    break
    if crack == False:
        psswrd_lengt += 1

if psswrd_lengt == 4:
    for a in letters:
        if crack == True:
            break
        for b in letters:
            if crack == True:
                break
            for c in letters:
                if crack == True:
                    break
                for d in letters:
                    times +=1
                    if (a+b+c+d) == password:
                        crack = True
                        break
    if crack == False:
        psswrd_lengt += 1

if psswrd_lengt == 5:
    for a in letters:
        if crack == True:
            break
        for b in letters:
            if crack == True:
                break
            for c in letters:
                if crack == True:
                    break
                for d in letters:
                    if crack == True:
                        break
                    for e in letters:
                        times +=1
                        if (a+b+c+d+e) == password:
                            crack = True
                            break
    if crack == False:
        psswrd_lengt += 1

if psswrd_lengt == 6:
    for a in letters:
        if crack == True:
            break
        for b in letters:
            if crack == True:
                break
            for c in letters:
                if crack == True:
                    break
                for d in letters:
                    if crack == True:
                        break
                    for e in letters:
                        if crack == True:
                            break
                        for f in letters:
                            times +=1
                            if (a+b+c+d+e+f) == password:
                                crack = True
                                break
    if crack == False:
        psswrd_lengt += 1

if psswrd_lengt == 7:
    for a in letters:
        if crack == True:
            break
        for b in letters:
            if crack == True:
                break
            for c in letters:
                if crack == True:
                    break
                for d in letters:
                    if crack == True:
                        break
                    for e in letters:
                        if crack == True:
                            break
                        for f in letters:
                            if crack == True:
                                break
                            for g in letters:
                                times +=1
                                if (a+b+c+d+e+f+g) == password:
                                    crack = True
                                    break
    if crack == False:
        psswrd_lengt += 1
        
if psswrd_lengt == 8:
    for a in letters:
        if crack == True:
            break
        for b in letters:
            if crack == True:
                break
            for c in letters:
                if crack == True:
                    break
                for d in letters:
                    if crack == True:
                        break
                    for e in letters:
                        if crack == True:
                            break
                        for f in letters:
                            if crack == True:
                                break
                            for g in letters:
                                if crack == True:
                                    break
                                for h in letters:
                                    times +=1
                                    if (a+b+c+d+e+f+g+h) == password:
                                        crack = True
                                        break
    if crack == False:
        psswrd_lengt += 1

if psswrd_lengt == 9:
    for a in letters:
        if crack == True:
            break
        for b in letters:
            if crack == True:
                break
            for c in letters:
                if crack == True:
                    break
                for d in letters:
                    if crack == True:
                        break
                    for e in letters:
                        if crack == True:
                            break
                        for f in letters:
                            if crack == True:
                                break
                            for g in letters:
                                if crack == True:
                                    break
                                for h in letters:
                                    if crack == True:
                                        break
                                    for i in letters:
                                        times +=1
                                        if (a+b+c+d+e+f+g+h+i) == password:
                                            crack = True
                                            break
    if crack == False:
        psswrd_lengt += 1

if psswrd_lengt == 10:
    for a in letters:
        if crack == True:
            break
        for b in letters:
            if crack == True:
                break
            for c in letters:
                if crack == True:
                    break
                for d in letters:
                    if crack == True:
                        break
                    for e in letters:
                        if crack == True:
                            break
                        for f in letters:
                            if crack == True:
                                break
                            for g in letters:
                                if crack == True:
                                    break
                                for h in letters:
                                    if crack == True:
                                        break
                                    for i in letters:
                                        if crack == True:
                                            break
                                        for j in letters:
                                            times +=1
                                            if (a+b+c+d+e+f+g+h+i+j) == password:
                                                crack = True
                                                break 
# end

winsound.MessageBeep()
time_end = time.time()
time_crack = time_end - time_begin
minutes, seconds = divmod(time_crack, 60)
print("see 'password_cracks.txt' for the crack information")
with open("password_cracks.txt", "a") as file:
    file.write("\n")
    file.write(f"password: {password}\n")
    file.write(f"time taken: {minutes:.0f} minutes and {seconds:.2f} seconds.\n")
    file.write(f"times i tried: {times}\n")
os.system('pause') # to see the end result