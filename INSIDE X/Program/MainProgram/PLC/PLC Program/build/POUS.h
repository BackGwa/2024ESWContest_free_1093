#include "beremiz.h"
#ifndef __POUS_H
#define __POUS_H

#include "accessor.h"
#include "iec_std_lib.h"

__DECLARE_ENUMERATED_TYPE(LOGLEVEL,
  LOGLEVEL__CRITICAL,
  LOGLEVEL__WARNING,
  LOGLEVEL__INFO,
  LOGLEVEL__DEBUG
)
// FUNCTION_BLOCK LOGGER
// Data part
typedef struct {
  // FB Interface - IN, OUT, IN_OUT variables
  __DECLARE_VAR(BOOL,EN)
  __DECLARE_VAR(BOOL,ENO)
  __DECLARE_VAR(BOOL,TRIG)
  __DECLARE_VAR(STRING,MSG)
  __DECLARE_VAR(LOGLEVEL,LEVEL)

  // FB private variables - TEMP, private and located variables
  __DECLARE_VAR(BOOL,TRIG0)

} LOGGER;

void LOGGER_init__(LOGGER *data__, BOOL retain);
// Code part
void LOGGER_body__(LOGGER *data__);
// PROGRAM PROGRAM0
// Data part
typedef struct {
  // PROGRAM Interface - IN, OUT, IN_OUT variables

  // PROGRAM private variables - TEMP, private and located variables
  __DECLARE_VAR(BOOL,PBS)
  __DECLARE_VAR(BOOL,EMS)
  __DECLARE_VAR(BOOL,PS1)
  __DECLARE_VAR(BOOL,PS2)
  __DECLARE_VAR(BOOL,PS3)
  __DECLARE_VAR(BOOL,IS1)
  __DECLARE_VAR(BOOL,CONV)
  __DECLARE_VAR(BOOL,CYN)
  __DECLARE_VAR(BOOL,RL)
  __DECLARE_VAR(BOOL,YL)
  __DECLARE_VAR(BOOL,GL)
  __DECLARE_VAR(BOOL,SEQUENCE_1)
  __DECLARE_VAR(BOOL,SEQUENCE_2)
  __DECLARE_VAR(BOOL,SEQUENCE_3)
  __DECLARE_VAR(BOOL,RST)
  __DECLARE_VAR(BOOL,SEQUENCE_4)
  __DECLARE_VAR(BOOL,IS_METAL)
  __DECLARE_VAR(BOOL,IS_NON_METAL)
  __DECLARE_VAR(BOOL,FLICKER)
  __DECLARE_VAR(BOOL,SEQ_WAIT)
  __DECLARE_VAR(BOOL,SEQ_WAIT_2)
  TON TON0;
  TON TON1;
  TON TON2;
  TON TON3;
  TON TON4;
  TON TON5;

} PROGRAM0;

void PROGRAM0_init__(PROGRAM0 *data__, BOOL retain);
// Code part
void PROGRAM0_body__(PROGRAM0 *data__);
#endif //__POUS_H
