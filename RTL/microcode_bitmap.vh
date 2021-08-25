

parameter mc_END            = 0;
parameter mc_TRAP           = 1;
parameter mc_IR_DB          = 2; //load IR with DB contents
parameter mc_INC_DEC_OP     = 3;
parameter mc_INC_DEC        = 4; //INC_DEC SRW ACCESS
parameter mc_PC_SRW         = 5; //PC GETS registered by SRW bus
parameter mc_PC_AD          = 6; //fetches instruction indexed by PC from data bus to IR
parameter mc_SP_AD          = 7; //connects stack pointer to abus
parameter mc_SP_SRW         = 8; //SP GETS registered by SRW bus

