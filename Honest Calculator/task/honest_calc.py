# write your code here
msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msg_ = ["", "", "", "", "", "", "", "", "", "", msg_10, msg_11, msg_12]

def is_one_digit(v):
	return -10 < v < 10 and int(v) == float(v)
	
def chek(v1, v2, v3):
	msg = ""
	if is_one_digit(v1) and is_one_digit(v2):
		msg += msg_6
	if (v1 == 1 or v2 == 1) and v3 =="*":
		msg += msg_7
	if (v1 == 0 or v2 == 0) and (v3 == "+" or v3 == "-" or v3 == "*"):
		msg += msg_8
	if msg != "":
		msg = msg_9 + msg
		print(msg)
	else:
		return

def number(n):
    if '.' in str(n):
        if str(n).replace('.', '').isdigit():
            return float(n)
    elif str(n).isdigit():
        return int(n)
    else:
        return msg_1


def znak(z):
    if z in '+-*/':
        return z
    else:
        return msg_2


memory = 0
flag_main = 0
while flag_main == 0:
    print(msg_0)
    x, o, y = input().split()
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    x = number(x)
    y = number(y)
    o = znak(o)
    if isinstance(x, str):
        print(x)
        continue
    elif isinstance(y, str):
        print(y)
        continue
    elif len(o) != 1:
        print(o)
        continue
    chek(x, y, o)
    if o == '+':
        result = x + y
    elif o == '-':
        result = x - y
    elif o == '*':
        result = x * y
    elif o == '/' and y == 0:
        print(msg_3)
        continue
    elif o == '/' and y != 0:
        result = x / y
    print(float(result))
    flag = 0
    while flag == 0:
        print(msg_4)
        ansower = input()
        if ansower == 'y':
            if is_one_digit(result):
            	msg_index = 10
            	while msg_index <= 12:
            		print(msg_[msg_index])
            		ansower = input()
            		if ansower == "y":
            			msg_index += 1
            			if msg_index == 12:
            				memory = result
            		else:
            			break
            else:
            	memory = result
            flag1 = 0
            while flag1 == 0:
                print(msg_5)
                ansower1 = input()
                if ansower1 == 'y':
                    flag = 1
                    break
                elif ansower1 == 'n':
                    flag = 1
                    flag1 = 1
                    flag_main = 1

        elif ansower == 'n':
            flag1 = 0
            while flag1 == 0:
                print(msg_5)
                ansower1 = input()
                if ansower1 == 'y':
                    flag = 1
                    break
                elif ansower1 == 'n':
                    flag = 1
                    flag1 = 1
                    flag_main = 1
        else:
            break
