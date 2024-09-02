void LOGGER_init__(LOGGER *data__, BOOL retain) {
  __INIT_VAR(data__->EN,__BOOL_LITERAL(TRUE),retain)
  __INIT_VAR(data__->ENO,__BOOL_LITERAL(TRUE),retain)
  __INIT_VAR(data__->TRIG,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->MSG,__STRING_LITERAL(0,""),retain)
  __INIT_VAR(data__->LEVEL,LOGLEVEL__INFO,retain)
  __INIT_VAR(data__->TRIG0,__BOOL_LITERAL(FALSE),retain)
}

// Code part
void LOGGER_body__(LOGGER *data__) {
  // Control execution
  if (!__GET_VAR(data__->EN)) {
    __SET_VAR(data__->,ENO,,__BOOL_LITERAL(FALSE));
    return;
  }
  else {
    __SET_VAR(data__->,ENO,,__BOOL_LITERAL(TRUE));
  }
  // Initialise TEMP variables

  if ((__GET_VAR(data__->TRIG,) && !(__GET_VAR(data__->TRIG0,)))) {
    #define GetFbVar(var,...) __GET_VAR(data__->var,__VA_ARGS__)
    #define SetFbVar(var,val,...) __SET_VAR(data__->,var,__VA_ARGS__,val)

   LogMessage(GetFbVar(LEVEL),(char*)GetFbVar(MSG, .body),GetFbVar(MSG, .len));
  
    #undef GetFbVar
    #undef SetFbVar
;
  };
  __SET_VAR(data__->,TRIG0,,__GET_VAR(data__->TRIG,));

  goto __end;

__end:
  return;
} // LOGGER_body__() 





void PROGRAM0_init__(PROGRAM0 *data__, BOOL retain) {
  __INIT_VAR(data__->PBS,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->EMS,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->PS1,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->PS2,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->PS3,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->IS1,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->CONV,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->CYN,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->RL,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->YL,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->GL,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->SEQUENCE_1,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->SEQUENCE_2,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->SEQUENCE_3,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->RST,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->SEQUENCE_4,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->IS_METAL,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->IS_NON_METAL,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->FLICKER,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->SEQ_WAIT,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->SEQ_WAIT_2,__BOOL_LITERAL(FALSE),retain)
  TON_init__(&data__->TON0,retain);
  TON_init__(&data__->TON1,retain);
  TON_init__(&data__->TON2,retain);
  TON_init__(&data__->TON3,retain);
  TON_init__(&data__->TON4,retain);
  TON_init__(&data__->TON5,retain);
}

// Code part
void PROGRAM0_body__(PROGRAM0 *data__) {
  // Initialise TEMP variables

  __SET_VAR(data__->,SEQUENCE_1,,(((((((!(__GET_VAR(data__->IS1,)) && __GET_VAR(data__->PS3,)) && __GET_VAR(data__->PS2,)) && !(__GET_VAR(data__->PS1,))) && !(__GET_VAR(data__->PBS,))) || __GET_VAR(data__->SEQUENCE_1,)) && __GET_VAR(data__->EMS,)) && !(__GET_VAR(data__->RST,))));
  __SET_VAR(data__->,CONV,,__GET_VAR(data__->SEQUENCE_1,));
  __SET_VAR(data__->TON0.,IN,,__GET_VAR(data__->SEQ_WAIT,));
  __SET_VAR(data__->TON0.,PT,,__time_to_timespec(1, 450, 0, 0, 0, 0));
  TON_body__(&data__->TON0);
  __SET_VAR(data__->,SEQUENCE_2,,(((__GET_VAR(data__->EMS,) && !(__GET_VAR(data__->RST,))) && __GET_VAR(data__->SEQUENCE_2,)) || __GET_VAR(data__->TON0.Q,)));
  __SET_VAR(data__->,IS_METAL,,((__GET_VAR(data__->EMS,) && !(__GET_VAR(data__->RST,))) && (__GET_VAR(data__->IS_METAL,) || ((!(__GET_VAR(data__->IS_NON_METAL,)) && __GET_VAR(data__->IS1,)) && __GET_VAR(data__->SEQUENCE_2,)))));
  __SET_VAR(data__->TON1.,IN,,__GET_VAR(data__->IS_METAL,));
  __SET_VAR(data__->TON1.,PT,,__time_to_timespec(1, 500, 0, 0, 0, 0));
  TON_body__(&data__->TON1);
  __SET_VAR(data__->,SEQUENCE_3,,(!(__GET_VAR(data__->SEQUENCE_4,)) && __GET_VAR(data__->TON1.Q,)));
  __SET_VAR(data__->TON2.,IN,,((__GET_VAR(data__->SEQUENCE_3,) && __GET_VAR(data__->EMS,)) && !(__GET_VAR(data__->RST,))));
  __SET_VAR(data__->TON2.,PT,,__time_to_timespec(1, 100, 0, 0, 0, 0));
  TON_body__(&data__->TON2);
  __SET_VAR(data__->,SEQUENCE_4,,(((__GET_VAR(data__->SEQUENCE_4,) && __GET_VAR(data__->EMS,)) && !(__GET_VAR(data__->RST,))) || __GET_VAR(data__->TON2.Q,)));
  __SET_VAR(data__->TON3.,IN,,__GET_VAR(data__->SEQ_WAIT_2,));
  __SET_VAR(data__->TON3.,PT,,__time_to_timespec(1, 0, 2, 0, 0, 0));
  TON_body__(&data__->TON3);
  __SET_VAR(data__->,RST,,(__GET_VAR(data__->SEQUENCE_4,) || __GET_VAR(data__->TON3.Q,)));
  __SET_VAR(data__->,IS_NON_METAL,,((__GET_VAR(data__->EMS,) && !(__GET_VAR(data__->RST,))) && (__GET_VAR(data__->IS_NON_METAL,) || ((!(__GET_VAR(data__->IS_METAL,)) && !(__GET_VAR(data__->IS1,))) && __GET_VAR(data__->SEQUENCE_2,)))));
  __SET_VAR(data__->,GL,,!(__GET_VAR(data__->PS1,)));
  __SET_VAR(data__->,RL,,!(__GET_VAR(data__->EMS,)));
  __SET_VAR(data__->TON4.,IN,,(!(__GET_VAR(data__->FLICKER,)) && __GET_VAR(data__->SEQUENCE_1,)));
  __SET_VAR(data__->TON4.,PT,,__time_to_timespec(1, 0, 1, 0, 0, 0));
  TON_body__(&data__->TON4);
  __SET_VAR(data__->,YL,,__GET_VAR(data__->TON4.Q,));
  __SET_VAR(data__->TON5.,IN,,__GET_VAR(data__->YL,));
  __SET_VAR(data__->TON5.,PT,,__time_to_timespec(1, 0, 1, 0, 0, 0));
  TON_body__(&data__->TON5);
  __SET_VAR(data__->,FLICKER,,__GET_VAR(data__->TON5.Q,));
  __SET_VAR(data__->,SEQ_WAIT,,((__GET_VAR(data__->EMS,) && !(__GET_VAR(data__->RST,))) && ((!(__GET_VAR(data__->PS2,)) && __GET_VAR(data__->SEQUENCE_1,)) || __GET_VAR(data__->SEQ_WAIT,))));
  __SET_VAR(data__->,SEQ_WAIT_2,,((__GET_VAR(data__->EMS,) && !(__GET_VAR(data__->RST,))) && ((!(__GET_VAR(data__->PS3,)) && __GET_VAR(data__->IS_NON_METAL,)) || __GET_VAR(data__->SEQ_WAIT_2,))));
  __SET_VAR(data__->,CYN,,__GET_VAR(data__->SEQUENCE_3,));

  goto __end;

__end:
  return;
} // PROGRAM0_body__() 





