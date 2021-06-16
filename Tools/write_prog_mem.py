

mem = ["00"] * (2**15)

mem[0x0000] = "00"
mem[0x0001] = "01"
mem[0x7ffc] = "00"
mem[0x7ffd] = "80"

filePath = "../RTL/program_ROM.hex"

f = open("program_ROM.hex", "w")

for i in range(len(mem)):
    # for j in range(8):
    f.write(mem[i] + " ")
    if((i+1)%8==0):
        f.write("\n")

f.close()