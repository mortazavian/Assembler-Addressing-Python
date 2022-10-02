def remove_empty_string(lst):
    for item in lst:
        if item == '':
            lst.remove(item)
    return lst


def valid_input(lst):
    instructions_list = ['add', 'sub' , 'mul' , 'div']
    if lst[0] not in instructions_list:
        print("Invalid Instruction")
    else:
        decide(lst)


def decide(lst):
    if lst[0] == 'add':
        addition(lst[2])
    if lst[0] == 'sub':
        subtraction(lst[2])
    if lst[0] == 'mul':
        mul(lst[2])


### Instructions:
# 1.ADD
def addition(memory_address):
    global acc
    acc += memory[int(memory_address)]
    print(acc)


# 2.SUB
def subtraction(memory_address):
    global acc
    acc -= memory[int(memory_address)]
    print(acc)


# 3.MUL
def mul(memory_address):
    global acc
    acc *= memory[int(memory_address)]
    print(acc)

# Acc -> Register to store datas temporary
acc = 0

# Input file
f_input = open("input.txt", "r")

# Memory to store variables and works like real memory
# Memory is 2D array filled with '0'
memory = []
# Fill memory with '0'
memory.append(3)
memory.append(2)
for i in range(10000):
    memory.append(0)
    # memory.append(['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])

# Read inputs
for line in f_input:
    # Remove the first bit
    line = line[1:]

    # Split them by ' '
    line = line.split(" ")

    line = remove_empty_string(line)

    # Split inputs

    print(line)

    print(memory)

    # Check for valid inputs
    # if inputs are valid then decide what to do
    valid_input(line)

    print(acc)

f_input.close()
