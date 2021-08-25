import copy


# https://www.masswerk.at/6502/6502_instruction_set.html 
# https://www.pagetable.com/c64ref/6502/
#

mc_mem_len = 0xFF
max_instruction_len = 8

microcode_template = [0b0000000000000000] * max_instruction_len
# microcode_template = [1, 2, 3, 4, 5, 6, 7, 8]

instruction_template = {"name": "UKN", "len": 0, "microcode": [0] * max_instruction_len}





mc_END = 0b1 << 0
mc_INC_DEC_OP = 0b1 << 1
mc_INC_DEC = 0b1 << 2 #INC_DEC SRW ACCESS
mc_PC_SRW = 0b1 << 3 #PC GETS registered by SRW bus
mc_PC_AD = 0b1 << 4 #fetches instruction indexed by PC from data bus to IR
mc_SP_AD = 0b1 << 5 #connects stack pointer to abus
mc_SP_SRW = 0b1 << 6 #SP GETS registered by SRW bus

# opcodes = [instruction_template] * mc_mem_len
opcodes = []
for i in range(mc_mem_len):
    opcodes.append(copy.deepcopy(instruction_template))
    # opcodes[i]['microcode'][max_instruction_len-1] = mc_END

opcodes[0x00]['name'] = 'BRK' 
opcodes[0x00]['len'] = 7
opcodes[0x00]['microcode'][0] = mc_INC_DEC_OP | mc_INC_DEC | mc_PC_SRW | mc_PC_AD #PC+1
opcodes[0x00]['microcode'][1] = mc_SP_AD #ABUS=STACKPTR DBUS=PCH
# opcodes[0x00]['microcode'][2] = 0b111111111111#mc_INC_DEC | mc_SP_SRW | mc_SP_AD #SP-1
opcodes[0x00]['microcode'][3] = mc_END


opcodes[0x01]['name'] = 'ORA' 
opcodes[0x01]['len'] = 6
opcodes[0x01]['microcode'][2] = mc_END

opcodes[0x02]['name'] = 'DUMMY' 
opcodes[0x02]['len'] = 7
opcodes[0x02]['microcode'][0] = mc_INC_DEC_OP | mc_INC_DEC | mc_PC_SRW | mc_PC_AD
opcodes[0x02]['microcode'][2] = mc_END

opcodes[0x05]['name'] = 'ORA' 
opcodes[0x05]['len'] = 3

opcodes[0x06]['name'] = 'ASL' 
opcodes[0x06]['len'] = 5

opcodes[0x08]['name'] = 'PHP' 
opcodes[0x08]['len'] = 3

opcodes[0x09]['name'] = 'ORA' 
opcodes[0x09]['len'] = 2

opcodes[0x0A]['name'] = 'ASL' 
opcodes[0x0A]['len'] = 2

opcodes[0x0D]['name'] = 'ORA' 
opcodes[0x0D]['len'] = 3

opcodes[0x0E]['name'] = 'ORA' 
opcodes[0x0E]['len'] = 3

opcodes[0x10]['name'] = 'ORA' 
opcodes[0x10]['len'] = 3

opcodes[0x11]['name'] = 'ORA' 
opcodes[0x11]['len'] = 3

opcodes[0x15]['name'] = 'ORA' 
opcodes[0x15]['len'] = 3

opcodes[0x16]['name'] = 'ORA' 
opcodes[0x16]['len'] = 3

opcodes[0x18]['name'] = 'ORA' 
opcodes[0x18]['len'] = 3

opcodes[0x19]['name'] = 'ORA' 
opcodes[0x19]['len'] = 3

opcodes[0x1D]['name'] = 'ORA' 
opcodes[0x1D]['len'] = 3

opcodes[0x1E]['name'] = 'ORA' 
opcodes[0x1E]['len'] = 3

opcodes[0x20]['name'] = 'ORA' 
opcodes[0x20]['len'] = 3

opcodes[0x21]['name'] = 'ORA' 
opcodes[0x21]['len'] = 3

opcodes[0x24]['name'] = 'ORA' 
opcodes[0x24]['len'] = 3

opcodes[0x25]['name'] = 'ORA' 
opcodes[0x25]['len'] = 3

opcodes[0x26]['name'] = 'ORA' 
opcodes[0x26]['len'] = 3

opcodes[0x28]['name'] = 'ORA' 
opcodes[0x28]['len'] = 3

opcodes[0x29]['name'] = 'ORA' 
opcodes[0x29]['len'] = 3

opcodes[0x2A]['name'] = 'ORA' 
opcodes[0x2A]['len'] = 3

opcodes[0x2C]['name'] = 'ORA' 
opcodes[0x2C]['len'] = 3

opcodes[0x2D]['name'] = 'ORA' 
opcodes[0x2D]['len'] = 3

opcodes[0x2E]['name'] = 'ORA' 
opcodes[0x2E]['len'] = 3

opcodes[0x30]['name'] = 'ORA' 
opcodes[0x30]['len'] = 3

opcodes[0x31]['name'] = 'ORA' 
opcodes[0x31]['len'] = 3

opcodes[0x35]['name'] = 'ORA' 
opcodes[0x35]['len'] = 3

opcodes[0x36]['name'] = 'ORA' 
opcodes[0x36]['len'] = 3

opcodes[0x38]['name'] = 'ORA' 
opcodes[0x38]['len'] = 3

opcodes[0x39]['name'] = 'ORA' 
opcodes[0x39]['len'] = 3

opcodes[0x3D]['name'] = 'ORA' 
opcodes[0x3D]['len'] = 3

opcodes[0x3E]['name'] = 'ORA' 
opcodes[0x3E]['len'] = 3

opcodes[0x40]['name'] = 'ORA' 
opcodes[0x40]['len'] = 3

opcodes[0x41]['name'] = 'ORA' 
opcodes[0x41]['len'] = 3

opcodes[0x45]['name'] = 'ORA' 
opcodes[0x45]['len'] = 3

opcodes[0x46]['name'] = 'ORA' 
opcodes[0x46]['len'] = 3

opcodes[0x48]['name'] = 'ORA' 
opcodes[0x48]['len'] = 3

opcodes[0x49]['name'] = 'ORA' 
opcodes[0x49]['len'] = 3

opcodes[0x4A]['name'] = 'ORA' 
opcodes[0x4A]['len'] = 3

opcodes[0x4C]['name'] = 'ORA' 
opcodes[0x4C]['len'] = 3

opcodes[0x4D]['name'] = 'ORA' 
opcodes[0x4D]['len'] = 3

opcodes[0x4E]['name'] = 'ORA' 
opcodes[0x4E]['len'] = 3

opcodes[0x50]['name'] = 'ORA' 
opcodes[0x50]['len'] = 3

opcodes[0x51]['name'] = 'ORA' 
opcodes[0x51]['len'] = 3

opcodes[0x55]['name'] = 'ORA' 
opcodes[0x55]['len'] = 3

opcodes[0x56]['name'] = 'ORA' 
opcodes[0x56]['len'] = 3

opcodes[0x58]['name'] = 'ORA' 
opcodes[0x58]['len'] = 3

opcodes[0x59]['name'] = 'ORA' 
opcodes[0x59]['len'] = 3

opcodes[0x5D]['name'] = 'ORA' 
opcodes[0x5D]['len'] = 3

opcodes[0x5E]['name'] = 'ORA' 
opcodes[0x5E]['len'] = 3

opcodes[0x60]['name'] = 'ORA' 
opcodes[0x60]['len'] = 3

opcodes[0x61]['name'] = 'ORA' 
opcodes[0x61]['len'] = 3

opcodes[0x65]['name'] = 'ORA' 
opcodes[0x65]['len'] = 3

opcodes[0x66]['name'] = 'ORA' 
opcodes[0x66]['len'] = 3

opcodes[0x68]['name'] = 'ORA' 
opcodes[0x68]['len'] = 3

opcodes[0x69]['name'] = 'ORA' 
opcodes[0x69]['len'] = 3

opcodes[0x6A]['name'] = 'ORA' 
opcodes[0x6A]['len'] = 3

opcodes[0x6C]['name'] = 'ORA' 
opcodes[0x6C]['len'] = 3

opcodes[0x6D]['name'] = 'ORA' 
opcodes[0x6D]['len'] = 3

opcodes[0x6E]['name'] = 'ORA' 
opcodes[0x6E]['len'] = 3

opcodes[0x70]['name'] = 'ORA' 
opcodes[0x70]['len'] = 3

opcodes[0x71]['name'] = 'ORA' 
opcodes[0x71]['len'] = 3

opcodes[0x75]['name'] = 'ORA' 
opcodes[0x75]['len'] = 3

opcodes[0x76]['name'] = 'ORA' 
opcodes[0x76]['len'] = 3

opcodes[0x78]['name'] = 'ORA' 
opcodes[0x78]['len'] = 3

opcodes[0x79]['name'] = 'ORA' 
opcodes[0x79]['len'] = 3

opcodes[0x7D]['name'] = 'ORA' 
opcodes[0x7D]['len'] = 3

opcodes[0x7E]['name'] = 'ORA' 
opcodes[0x7E]['len'] = 3

opcodes[0x81]['name'] = 'ORA' 
opcodes[0x81]['len'] = 3

opcodes[0x84]['name'] = 'ORA' 
opcodes[0x84]['len'] = 3

opcodes[0x85]['name'] = 'ORA' 
opcodes[0x85]['len'] = 3

opcodes[0x86]['name'] = 'ORA' 
opcodes[0x86]['len'] = 3

opcodes[0x88]['name'] = 'ORA' 
opcodes[0x88]['len'] = 3

opcodes[0x8A]['name'] = 'ORA' 
opcodes[0x8A]['len'] = 3

opcodes[0x8C]['name'] = 'ORA' 
opcodes[0x8C]['len'] = 3

opcodes[0x8D]['name'] = 'ORA' 
opcodes[0x8D]['len'] = 3

opcodes[0x8E]['name'] = 'ORA' 
opcodes[0x8E]['len'] = 3

opcodes[0x90]['name'] = 'ORA' 
opcodes[0x90]['len'] = 3

opcodes[0x91]['name'] = 'ORA' 
opcodes[0x91]['len'] = 3

opcodes[0x94]['name'] = 'ORA' 
opcodes[0x94]['len'] = 3

opcodes[0x95]['name'] = 'ORA' 
opcodes[0x95]['len'] = 3

opcodes[0x96]['name'] = 'ORA' 
opcodes[0x96]['len'] = 3

opcodes[0x98]['name'] = 'ORA' 
opcodes[0x98]['len'] = 3

opcodes[0x99]['name'] = 'ORA' 
opcodes[0x99]['len'] = 3

opcodes[0x9A]['name'] = 'ORA' 
opcodes[0x9A]['len'] = 3

opcodes[0x9D]['name'] = 'ORA' 
opcodes[0x9D]['len'] = 3

opcodes[0xA0]['name'] = 'ORA' 
opcodes[0xA0]['len'] = 3

opcodes[0xA1]['name'] = 'ORA' 
opcodes[0xA1]['len'] = 3

opcodes[0xA4]['name'] = 'ORA' 
opcodes[0xA4]['len'] = 3

opcodes[0xA5]['name'] = 'ORA' 
opcodes[0xA5]['len'] = 3

opcodes[0xA6]['name'] = 'ORA' 
opcodes[0xA6]['len'] = 3

opcodes[0xA8]['name'] = 'ORA' 
opcodes[0xA8]['len'] = 3

opcodes[0xA9]['name'] = 'ORA' 
opcodes[0xA9]['len'] = 3

opcodes[0xAA]['name'] = 'ORA' 
opcodes[0xAA]['len'] = 3

opcodes[0xAC]['name'] = 'ORA' 
opcodes[0xAC]['len'] = 3

opcodes[0xAD]['name'] = 'ORA' 
opcodes[0xAD]['len'] = 3

opcodes[0xAE]['name'] = 'ORA' 
opcodes[0xAE]['len'] = 3

opcodes[0xB0]['name'] = 'ORA' 
opcodes[0xB0]['len'] = 3

opcodes[0xB1]['name'] = 'ORA' 
opcodes[0xB1]['len'] = 3

opcodes[0xB4]['name'] = 'ORA' 
opcodes[0xB4]['len'] = 3

opcodes[0xB5]['name'] = 'ORA' 
opcodes[0xB5]['len'] = 3

opcodes[0xB6]['name'] = 'ORA' 
opcodes[0xB6]['len'] = 3

opcodes[0xB8]['name'] = 'ORA' 
opcodes[0xB8]['len'] = 3

opcodes[0xB9]['name'] = 'ORA' 
opcodes[0xB9]['len'] = 3

opcodes[0xBA]['name'] = 'ORA' 
opcodes[0xBA]['len'] = 3

opcodes[0xBC]['name'] = 'ORA' 
opcodes[0xBC]['len'] = 3

opcodes[0xBD]['name'] = 'ORA' 
opcodes[0xBD]['len'] = 3

opcodes[0xBE]['name'] = 'ORA' 
opcodes[0xBE]['len'] = 3

opcodes[0xC0]['name'] = 'ORA' 
opcodes[0xC0]['len'] = 3

opcodes[0xC1]['name'] = 'ORA' 
opcodes[0xC1]['len'] = 3

opcodes[0xC4]['name'] = 'ORA' 
opcodes[0xC4]['len'] = 3

opcodes[0xC5]['name'] = 'ORA' 
opcodes[0xC5]['len'] = 3

opcodes[0xC6]['name'] = 'ORA' 
opcodes[0xC6]['len'] = 3

opcodes[0xC8]['name'] = 'ORA' 
opcodes[0xC8]['len'] = 3

opcodes[0xC9]['name'] = 'ORA' 
opcodes[0xC9]['len'] = 3

opcodes[0xCA]['name'] = 'ORA' 
opcodes[0xCA]['len'] = 3

opcodes[0xCC]['name'] = 'ORA' 
opcodes[0xCC]['len'] = 3

opcodes[0xCD]['name'] = 'ORA' 
opcodes[0xCD]['len'] = 3

opcodes[0xCE]['name'] = 'ORA' 
opcodes[0xCE]['len'] = 3

opcodes[0xD0]['name'] = 'ORA' 
opcodes[0xD0]['len'] = 3

opcodes[0xD1]['name'] = 'ORA' 
opcodes[0xD1]['len'] = 3

opcodes[0xD5]['name'] = 'ORA' 
opcodes[0xD5]['len'] = 3

opcodes[0xD6]['name'] = 'ORA' 
opcodes[0xD6]['len'] = 3

opcodes[0xD8]['name'] = 'ORA' 
opcodes[0xD8]['len'] = 3

opcodes[0xD9]['name'] = 'ORA' 
opcodes[0xD9]['len'] = 3

opcodes[0xDD]['name'] = 'ORA' 
opcodes[0xDD]['len'] = 3

opcodes[0xDE]['name'] = 'ORA' 
opcodes[0xDE]['len'] = 3

opcodes[0xE0]['name'] = 'ORA' 
opcodes[0xE0]['len'] = 3

opcodes[0xE1]['name'] = 'ORA' 
opcodes[0xE1]['len'] = 3

opcodes[0xE4]['name'] = 'ORA' 
opcodes[0xE4]['len'] = 3

opcodes[0xE5]['name'] = 'ORA' 
opcodes[0xE5]['len'] = 3

opcodes[0xE6]['name'] = 'ORA' 
opcodes[0xE6]['len'] = 3

opcodes[0xE8]['name'] = 'ORA' 
opcodes[0xE8]['len'] = 3

opcodes[0xE9]['name'] = 'ORA' 
opcodes[0xE9]['len'] = 3

opcodes[0xEA]['name'] = 'NOP' #nop opcode
opcodes[0xEA]['len'] = 2
opcodes[0x00]['microcode'][0] = mc_INC_DEC_OP | mc_INC_DEC | mc_PC_SRW | mc_PC_AD
opcodes[0x00]['microcode'][2] = mc_END

opcodes[0xEC]['name'] = 'ORA' 
opcodes[0xEC]['len'] = 3

opcodes[0xED]['name'] = 'ORA' 
opcodes[0xED]['len'] = 3

opcodes[0xEE]['name'] = 'ORA' 
opcodes[0xEE]['len'] = 3

opcodes[0xF0]['name'] = 'ORA' 
opcodes[0xF0]['len'] = 3

opcodes[0xF1]['name'] = 'ORA' 
opcodes[0xF1]['len'] = 3

opcodes[0xF5]['name'] = 'ORA' 
opcodes[0xF5]['len'] = 3

opcodes[0xF6]['name'] = 'ORA' 
opcodes[0xF6]['len'] = 3

opcodes[0xF8]['name'] = 'ORA' 
opcodes[0xF8]['len'] = 3

opcodes[0xF9]['name'] = 'ORA' 
opcodes[0xF9]['len'] = 3

opcodes[0xFD]['name'] = 'ORA' 
opcodes[0xFD]['len'] = 3

opcodes[0xFE]['name'] = 'ORA' 
opcodes[0xFE]['len'] = 3



filePath = "../RTL/microcode_gen.hex"

f = open(filePath, "w")

for i in range(mc_mem_len):
    # print("opcode " + str(i) + '\n')
    for j in range(max_instruction_len):
        # for k in range(16):
        f.write(format(opcodes[i]['microcode'][j], '016b') + "\n")
            # if((i+1)%16==0):
            #     f.write("\n")

f.close()