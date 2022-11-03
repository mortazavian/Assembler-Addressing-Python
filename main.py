def remove_empty_string(lst):
    for item in lst:
        if item == '':
            lst.remove(item)
    return lst


def valid_input(lst):
    instructions_list = ['add', 'ADD', 'sub', 'SUB', 'mpy', 'MPY', 'div', 'DIV', 'lda', 'LDA', 'sto', 'STO', 'hlt',
                         'HLT',
                         'bru', 'BRU', 'bmi', 'BMI', 'wwd', 'WWD' , '000' , 'rwd', 'RWD']
    global app_running
    global pc
    global instructions
    if lst[0] not in instructions_list:
        print("Invalid Instruction")
        print("The application terminated")
        print("The problem is on line: " + str(pc))
        app_running = False
    # elif lst[0] == '000':
    #     for i in range(len(instructions)):
    #         if instructions[i] == lst:
    #             index = i
    #     while instructions[index][0] == '000':
    #         memory.append(instructions[index][2])
    else:
        decide(lst)


def decide(lst):
    if lst[0] == 'add' or lst[0] == 'ADD':
        addition(lst[2])
    elif lst[0] == 'sub' or lst[0] == 'SUB':
        subtraction(lst[2])
    elif lst[0] == 'mpy' or lst[0] == 'MPY':
        mul(lst[2])
    elif lst[0] == 'div' or lst[0] == 'DIV':
        div(lst[2])
    elif lst[0] == 'lda' or lst[0] == 'LDA':
        load(lst[2])
    elif lst[0] == 'sto' or lst[0] == 'STO':
        store(lst[2])
    elif lst[0] == 'hlt' or lst[0] == 'HLT':
        halt(lst[2])
    elif lst[0] == 'bru' or lst[0] == 'BRU':
        branch_unconditional(lst[2])
    elif lst[0] == 'bmi' or lst[0] == 'BMI':
        branch_on_minus(lst[2])
    elif lst[0] == 'wwd' or lst[0] == 'WWD':
        write(lst[2])
    elif lst[0] == 'rwd' or lst[0] == 'RWD':
        read(lst[2])


### Instructions:
# 1.ADD
def addition(memory_address):
    global acc
    global pc
    acc += memory[int(memory_address)]
    # print(acc)
    pc += 1


# 2.SUB
def subtraction(memory_address):
    global acc
    global pc
    acc -= memory[int(memory_address)]
    # print(acc)
    pc += 1


# 3.MUL
def mul(memory_address):
    global acc
    global pc
    acc *= memory[int(memory_address)]
    # print(acc)
    pc += 1


# 4.DIV
def div(memory_address):
    global acc
    global pc
    acc /= memory[int(memory_address)]
    acc = int(acc)
    # print(acc)
    pc += 1


# 5.LOAD
def load(memory_address):
    global acc
    global pc
    acc = memory[int(memory_address)]
    # print(acc)
    pc += 1


# 6.STORE
def store(memory_address):
    global acc
    global pc
    memory[int(memory_address)] = acc
    # print(memory)
    pc += 1


# 7.HALT
def halt(memory_to_point):
    global pc
    # global pc
    global app_running
    app_running = False
    pc = int(memory_to_point)
    print("The pc is: " + str(pc))
    pc += 1
    print("The program stopped because of hlt instruction")


# 8.Branch Unconditional
def branch_unconditional(memory_to_point):
    global pc
    pc = int(memory_to_point)
    # print("The program counter is: " + str(pc))


# 9.Branch On Minus
def branch_on_minus(memory_to_point):
    global pc
    global acc
    if acc < 0:
        pc = int(memory_to_point)
    else:
        pc += 1


# 10.Write
def write(memory_address):
    global memory
    global pc
    print("The output of the program is: "+ str(memory[int(memory_address)]))
    pc = int(pc) + 1

# 11.Read
def read(memory_to_put_in):
    global memory
    global index_of_input
    global inputs
    global app_running
    # if index_of_input > len(inputs):
    #     pass
    # else:
    memory[int(memory_to_put_in)] = int(inputs[index_of_input][0])
    index_of_input += 1
    print(memory)
    global pc
    pc = int(pc) + 1

# Acc -> Register to store datas temporary
acc = 0

# PC -> Program Counter(is pointer which point to address of instruction to run)
pc = 0

# Input file
f_input = open("input4.txt", "r")

# Memory to store variables and works like real memory
# Memory is 2D array filled with '0'
memory = [0]
# Fill memory with '0'
# memory.append(3)
# memory.append(2)
# for i in range(10000):
#     memory.append(0)
    # memory.append(['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])

# Read inputs
instructions = []
for line in f_input:
    # Remove the first bit
    line = line[1:]
    # Split them by ' '
    line = line.split(" ")
    # Remove the empty string from list
    line = remove_empty_string(line)
    # append all the lines to instruction list
    instructions.append(line)

    # Check for valid inputs
    # if inputs are valid then decide what to do
    # valid_input(line)

    # print(acc)
f_input.close()

app_running = True

print(instructions)

# print(len(instructions))

index = 1
for i in range(len(instructions)):
    if len(instructions[i]) != 0:
        if instructions[i][0] == '000':
            print(i)
        # while instructions[i+1][0] == '000':
            memory.insert(index,int(instructions[i][2]))
            index += 1
        # memory.append(int(instructions[i][2]))

for i in range(10000):
    memory.append(0)


# print(memory)
index_of_input = 0
inputs = []

for i in range(len(instructions)):
    if len(instructions[i]) == 1:
        inputs.append(instructions[i])
    # elif int(instructions[i][0]) == 1:
    #     print("Read inputs finished")
    #     break

print("inputs are" + str(inputs))


while app_running:
    if int(pc) < len(instructions):
        valid_input(instructions[int(pc)])
        # print(pc)
    # elif int(pc) > len(instructions):
    #     app_running = False
    #
    # if index_of_input > len(inputs)-1:
    #     app_running = False

    else:
        app_running = False


print(instructions)

print(memory)
