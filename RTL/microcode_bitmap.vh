

parameter mc_END = 0;
parameter mc_IR_DB = 1; //load IR with DB contents
parameter mc_INC_DEC_OP = 2;
parameter mc_INC_DEC = 3; //INC_DEC SRW ACCESS
parameter mc_PC_SRW = 4; //PC GETS registered by SRW bus
parameter mc_PC_AD = 5; //fetches instruction indexed by PC from data bus to IR
parameter mc_SP_AD = 6; //connects stack pointer to abus
parameter mc_SP_SRW = 7; //SP GETS registered by SRW bus

