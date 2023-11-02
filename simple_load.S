# See LICENSE for license details.

#*****************************************************************************
# addi.S
#-----------------------------------------------------------------------------
#
# Test addi instruction.
#

#include "riscv_test.h"
#include "test_macros.h"

RVTEST_RV64U
RVTEST_CODE_BEGIN
  li	x1, 0xdeadbeef 
  RVTEST_PASS

RVTEST_CODE_END

  .data
RVTEST_DATA_BEGIN

  TEST_DATA

RVTEST_DATA_END
