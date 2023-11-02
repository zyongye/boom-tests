# Compile RISCV binary and run on BOOM

The tool and instruction is borrow from the official riscv-tests [repo](https://github.com/riscv-software-src/riscv-tests). 

## Precondition: Step up riscv toolchain
Follow the chipyard setup guide in another repo.

## Steps: 
1. Use ```simple.S``` as a skeleton. Thw testcode can be write at the section between ```RVTEST_CODE_BEGIN``` and ```RVTEST_PASS```. 

```
RVTEST_CODE_BEGIN
# Place to insert custom test code. 
RVTEST_PASS
```
2. Use the following riscv gcc commad to compile program
```
riscv64-unknown-elf-gcc -march=rv64g -mabi=lp64 -static -mcmodel=medany -fvisibility=hidden -nostdlib -nostartfiles -T link.ld -o simple simple.S
```
We get binary ```simple```. 

3. We can use riscv binary dump to inspect the binary
```
riscv64-unknown-elf-objdump --disassemble-all --disassemble-zeroes --section=.text --section=.text.startup --section=.text.init --section=.data simple
```

