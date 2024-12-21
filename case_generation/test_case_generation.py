import os
import copy

import test_case_template

PARENT_MAKEFILE = \
"""
SUBDIRS := $(wildcard */.)

all: $(SUBDIRS)
$(SUBDIRS):
\t$(MAKE) -C $@

.PHONY: all $(SUBDIRS)
"""

MAKEFILE_TEMPLATE = \
"""
CC = ~/chipyard/.conda-env/riscv-tools/bin/riscv64-unknown-elf-gcc
TARGET = FILE1 FILE2
LDFLAGS = -march=rv64g -mabi=lp64 -static -mcmodel=medany -fvisibility=hidden -nostdlib -nostartfiles -T ../../../link.ld

all: $(TARGET)
"""

ALU_R_INST = [
    "add",
    "sub",
    "xor",
    "and",
    "or",
    "mul",
    "mulh",
    "mulhsu",
    "mulhu",
    "div",
    "divu",
    "rem",
    "remu",
]

ALU_I_INST = [
    "addi",
    "xori",
    "ori",
    "andi"
]
SFT_R_INST = [
    "sll",
    "srl",
    "sra",
]
SFT_I_INST = [
    "slli",
    "srli",
    "srai",
]

LOAD_IMM_INST = [
    "lui",
    "auipc"
]

CMP_R_INST = [
    "slt",
    "sltu",
]

CMP_I_INST = [
    "slti",
    "sltiu",
]

BR_INST = [
    "beq",
    "bne",
    "blt",
    "bge",
    "bltu",
    "bgeu",
]

MEM_INST = [
    "lb",
    "lh",
    "lw",
    "lbu",
    "lhu",

    "sb",
    "sh",
    "sw",
]


parent_dir = "../"
directory = "isa/rv64ui/"
test_dir = parent_dir + directory

def write_to_file(file, content: str):
    with open(file, "w") as f:
        f.write(content)

def build_makefile(inst):
    makefile_content = copy.deepcopy(MAKEFILE_TEMPLATE)
    makefile_content = makefile_content.replace("FILE1", f"{inst}-1").replace("FILE2", f"{inst}-2")
    return makefile_content

def generate_alu_r():
    def build_alu_r_tests(opcode, value1, value2):
        template = copy.deepcopy(test_case_template.ALU_R_CASE)
        template = template.replace("OPCODE", opcode).replace("VALUE1", value1).replace("VALUE2", value2)
        return template
    for inst in ALU_R_INST:
        inst_dir = test_dir + inst
        os.makedirs(inst_dir, exist_ok=True)
        write_to_file(test_dir + inst + "/Makefile", build_makefile(inst=inst))
        write_to_file(f"{inst_dir}/{inst}-1.S", build_alu_r_tests(inst, "0xdad", "0x2"))
        write_to_file(f"{inst_dir}/{inst}-2.S", build_alu_r_tests(inst, "0xdad", "0x3"))


def generate_alu_i():
    def build_alu_i_tests(opcode, value1, imm):
        template = copy.deepcopy(test_case_template.ALU_I_CASE)
        template = template.replace("OPCODE", opcode).replace("VALUE1", value1).replace("IMM", imm)
        return template
    for inst in ALU_I_INST:
        inst_dir = test_dir + inst
        os.makedirs(inst_dir, exist_ok=True)
        write_to_file(test_dir + inst + "/Makefile", build_makefile(inst=inst))
        write_to_file(f"{inst_dir}/{inst}-1.S", build_alu_i_tests(inst, "0xdad", "0x212"))
        write_to_file(f"{inst_dir}/{inst}-2.S", build_alu_i_tests(inst, "0xdad", "0x212"))

def generate_sft_r():
    def build_sft_r_tests(opcode, value1, value2):
        template = copy.deepcopy(test_case_template.SFT_R_CASE)
        template = template.replace("OPCODE", opcode).replace("VALUE1", value1).replace("VALUE2", value2)
        return template
    for inst in SFT_R_INST:
        inst_dir = test_dir + inst
        os.makedirs(inst_dir, exist_ok=True)
        write_to_file(test_dir + inst + "/Makefile", build_makefile(inst=inst))
        write_to_file(f"{inst_dir}/{inst}-1.S", build_sft_r_tests(inst, "0xdad", "0x3"))
        write_to_file(f"{inst_dir}/{inst}-2.S", build_sft_r_tests(inst, "0xdad", "0x2"))

def generate_sft_i():
    def build_sft_i_tests(opcode, value1, imm):
        template = copy.deepcopy(test_case_template.SFT_I_CASE)
        template = template.replace("OPCODE", opcode).replace("VALUE1", value1).replace("IMM", imm)
        return template
    for inst in SFT_I_INST:
        inst_dir = test_dir + inst
        os.makedirs(inst_dir, exist_ok=True)
        write_to_file(test_dir + inst + "/Makefile", build_makefile(inst=inst))
        write_to_file(f"{inst_dir}/{inst}-1.S", build_sft_i_tests(inst, "0xdad", "0x3"))
        write_to_file(f"{inst_dir}/{inst}-2.S", build_sft_i_tests(inst, "0xdad", "0x3"))

def generate_load_i():
    def build_load_i_tests(opcode, imm):
        template = copy.deepcopy(test_case_template.LOAD_IMM_CASE)
        template = template.replace("OPCODE", opcode).replace("IMM", imm)
        return template
    for inst in LOAD_IMM_INST:
        inst_dir = test_dir + inst
        os.makedirs(inst_dir, exist_ok=True)
        write_to_file(test_dir + inst + "/Makefile", build_makefile(inst=inst))
        write_to_file(f"{inst_dir}/{inst}-1.S", build_load_i_tests(inst, "0x3"))
        write_to_file(f"{inst_dir}/{inst}-2.S", build_load_i_tests(inst, "0x3"))

def generate_cmp_r():
    def build_cmp_r_tests(opcode, value1, value2):
        template = copy.deepcopy(test_case_template.CMP_R_CASE)
        template = template.replace("OPCODE", opcode).replace("VALUE1", value1).replace("VALUE2", value2)
        return template
    for inst in CMP_R_INST:
        inst_dir = test_dir + inst
        os.makedirs(inst_dir, exist_ok=True)
        write_to_file(test_dir + inst + "/Makefile", build_makefile(inst=inst))
        write_to_file(f"{inst_dir}/{inst}-1.S", build_cmp_r_tests(inst, "0x1", "0x2"))
        write_to_file(f"{inst_dir}/{inst}-2.S", build_cmp_r_tests(inst, "0x3", "0x2"))


def generate_cmp_i():
    def build_cmp_i_tests(opcode, value1, imm):
        template = copy.deepcopy(test_case_template.CMP_I_CASE)
        template = template.replace("OPCODE", opcode).replace("VALUE1", value1).replace("IMM", imm)
        return template
    for inst in CMP_I_INST:
        inst_dir = test_dir + inst
        os.makedirs(inst_dir, exist_ok=True)
        write_to_file(test_dir + inst + "/Makefile", build_makefile(inst=inst))
        write_to_file(f"{inst_dir}/{inst}-1.S", build_cmp_i_tests(inst, "0xd", "0xf"))
        write_to_file(f"{inst_dir}/{inst}-2.S", build_cmp_i_tests(inst, "0xd", "0xf"))

def generate_br():
    def build_br_tests(opcode, value1, value2):
        template = copy.deepcopy(test_case_template.BR_CASE)
        template = template.replace("OPCODE", opcode).replace("VALUE1", value1).replace("VALUE2", value2)
        return template
    for inst in BR_INST:
        inst_dir = test_dir + inst
        os.makedirs(inst_dir, exist_ok=True)
        write_to_file(test_dir + inst + "/Makefile", build_makefile(inst=inst))
        if inst == "bge" or inst == "bgeu":
            write_to_file(f"{inst_dir}/{inst}-1.S", build_br_tests(inst, "0x2", "0x2"))
            write_to_file(f"{inst_dir}/{inst}-2.S", build_br_tests(inst, "0x1", "0x2"))
        else:
            write_to_file(f"{inst_dir}/{inst}-1.S", build_br_tests(inst, "0x2", "0x2"))
            write_to_file(f"{inst_dir}/{inst}-2.S", build_br_tests(inst, "0x3", "0x2"))

def generate_mem_case():
    def build_mem_tests(opcode, data_addr, data, offset):
        template = copy.deepcopy(test_case_template.MEM_INST_CASE)
        template = template.replace("OPCODE", opcode).replace("DATA_ADDR", data_addr).replace("MEM_DATA", data).replace("OFFSET", offset)
        return template
    for inst in MEM_INST:
        inst_dir = test_dir + inst
        os.makedirs(inst_dir, exist_ok=True)
        write_to_file(test_dir + inst + "/Makefile", build_makefile(inst=inst))
        if inst == "lw" or inst == "sw":
            write_to_file(f"{inst_dir}/{inst}-1.S", build_mem_tests(inst, "num1", "0xabcdacbd", "0"))
            write_to_file(f"{inst_dir}/{inst}-2.S", build_mem_tests(inst, "num2", "0xbbbbaaaa", "0"))
        elif inst == "lh" or inst == "sh" or inst == "lhu": 
            write_to_file(f"{inst_dir}/{inst}-1.S", build_mem_tests(inst, "num1", "0x32", "0"))
            write_to_file(f"{inst_dir}/{inst}-2.S", build_mem_tests(inst, "num2", "0x22", "2"))
        else:
            write_to_file(f"{inst_dir}/{inst}-1.S", build_mem_tests(inst, "num1", "0x2", "0"))
            write_to_file(f"{inst_dir}/{inst}-2.S", build_mem_tests(inst, "num2", "0xa", "5"))
        




def generate_cases():
    generate_alu_r()
    generate_alu_i()
    generate_sft_r()
    generate_sft_i()
    generate_load_i()
    generate_cmp_r()
    generate_cmp_i()
    generate_br()
    generate_mem_case()
    
        
def main():
    os.makedirs(test_dir, exist_ok=True)
    write_to_file(test_dir + "Makefile", PARENT_MAKEFILE)
    generate_cases()
    
if __name__ == "__main__":
    main()



