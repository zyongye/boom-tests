ALU_R_CASE = \
"""
#include "../../../riscv_test.h"
#include "../../../test_macros.h"

RVTEST_RV64U
RVTEST_CODE_BEGIN

lui         x1, VALUE1
lui         x2, VALUE2

nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop

OPCODE     x3, x1, x2

nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop

RVTEST_PASS

RVTEST_CODE_END

  .data
RVTEST_DATA_BEGIN

  TEST_DATA

RVTEST_DATA_END

"""

ALU_I_CASE = \
"""
#include "../../../riscv_test.h"
#include "../../../test_macros.h"

RVTEST_RV64U
RVTEST_CODE_BEGIN

lui         x1, VALUE1

nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop

OPCODE     x3, x1, IMM

nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop

RVTEST_PASS

RVTEST_CODE_END

  .data
RVTEST_DATA_BEGIN

  TEST_DATA

RVTEST_DATA_END

"""


SFT_R_CASE = \
"""
#include "../../../riscv_test.h"
#include "../../../test_macros.h"

RVTEST_RV64U
RVTEST_CODE_BEGIN

lui         x1, VALUE1
xor         x2, x2, x2
addi        x2, x2, VALUE2

nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop

OPCODE     x3, x1, x2

nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop

RVTEST_PASS

RVTEST_CODE_END

  .data
RVTEST_DATA_BEGIN

  TEST_DATA

RVTEST_DATA_END

"""

SFT_I_CASE = \
"""
#include "../../../riscv_test.h"
#include "../../../test_macros.h"

RVTEST_RV64U
RVTEST_CODE_BEGIN

lui         x1, VALUE1

nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop

OPCODE     x3, x1, IMM

nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop

RVTEST_PASS

RVTEST_CODE_END

  .data
RVTEST_DATA_BEGIN

  TEST_DATA

RVTEST_DATA_END

"""


LOAD_IMM_CASE = \
"""
#include "../../../riscv_test.h"
#include "../../../test_macros.h"

RVTEST_RV64U
RVTEST_CODE_BEGIN

nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop

OPCODE     x1, IMM

nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop

RVTEST_PASS

RVTEST_CODE_END

  .data
RVTEST_DATA_BEGIN

  TEST_DATA

RVTEST_DATA_END

"""


CMP_R_CASE = \
"""
#include "../../../riscv_test.h"
#include "../../../test_macros.h"

RVTEST_RV64U
RVTEST_CODE_BEGIN

lui     x1, VALUE1
lui     x2, VALUE2

nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop

OPCODE     x3, x1, x2

nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop

RVTEST_PASS

RVTEST_CODE_END

  .data
RVTEST_DATA_BEGIN

  TEST_DATA

RVTEST_DATA_END
"""

CMP_I_CASE = \
"""
#include "../../../riscv_test.h"
#include "../../../test_macros.h"

RVTEST_RV64U
RVTEST_CODE_BEGIN

xor     x1, x1, x1
add     x1, x1, VALUE1

nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop

OPCODE     x2, x1, IMM

nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop

RVTEST_PASS

RVTEST_CODE_END

  .data
RVTEST_DATA_BEGIN

  TEST_DATA

RVTEST_DATA_END
"""


BR_CASE = \
"""
#include "../../../riscv_test.h"
#include "../../../test_macros.h"

RVTEST_RV64U
RVTEST_CODE_BEGIN

lui     x1, VALUE1
lui     x2, VALUE2

nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop

OPCODE     x1, x2, branch_loc

nop
nop
nop
nop
nop
nop
branch_loc:
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop

RVTEST_PASS

RVTEST_CODE_END

  .data
RVTEST_DATA_BEGIN

  TEST_DATA

RVTEST_DATA_END

"""

MEM_INST_CASE = \
"""
#include "../../../riscv_test.h"
#include "../../../test_macros.h"

RVTEST_RV64U
RVTEST_CODE_BEGIN

la  x2, DATA_ADDR
li  x1, MEM_DATA

nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop

OPCODE     x1, OFFSET(x2)

nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop

RVTEST_PASS

RVTEST_CODE_END

  .data
RVTEST_DATA_BEGIN
num1:
    .word   0xdeadbeef
num2:
    .word   0xbeefdead

  TEST_DATA

RVTEST_DATA_END

"""







