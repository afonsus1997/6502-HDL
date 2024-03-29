// -----------------------------------------------------------------------------
// Author : Afonso Muralha afonsomuralha(at)gmail.com
// File   : CPU_top.v
// Create : 31/5/2021
// Revise : N/A
// Description:
//  An attempt to make a cycle-accurate 6502 core.
// -----------------------------------------------------------------------------

module CPU (
    input RDY,
    input clk,
    input RST,
    input NMI,
    input SO,
    input IRQ,
    output [15:0] A_BUS,
    input [7:0] D_BUS, //input only for now
    output RW,
    output SYNC,
    output PHI_1_OUT,
    output PHI_2_OUT,

    //aux outputs
    output [7:0] SR_OUT
    

);

    `include "microcode_bitmap.vh"

    assign PHI_1_OUT = clk;
    assign PHI_2_OUT = ~clk;

    //logic to interface the inout data bus
    reg d_bus_we;
    reg [7:0] d_bus_out;
    // assign D_BUS = d_bus_we ? 8'hz : d_bus_w; 

    /*internal registers*/
    reg [8:0] PCL;  //program counter
    reg [8:0] PCH;  //program counter
    reg [8:0] SPL;  //stack pointer
    reg [8:0] SPH;  //stack pointer
    reg [7:0] A;    //Accumulator "A" register
    reg [7:0] X;
    reg [7:0] Y;
    reg [2:0] MCPC;
    reg [8:0] IR;  //intruction register


    //status register flags
    reg sr_N;
    reg sr_V;
    reg sr_D;
    reg sr_I;
    reg sr_Z;
    reg sr_C;
    assign SR_OUT = {sr_N, sr_V, 1'b1, 1'b1, sr_D, sr_I, sr_Z, sr_C};
    //no BRK flag?

    //ALU registers
    reg [7:0] ALU_A;    // ALU input A
    reg [7:0] ALU_B;    // ALU intput B
    wire ALU_Z;         // ALU Zero flag
    wire ALU_AV;        // ALU overflow flag                    
    wire ALU_AN;        // ALU negative flag
    wire ALU_HC;        // ALU half carry

    wire [9:0] microcode_addr_w;
    wire [15:0] microcode_out_w;
    assign microcode_addr_w = {IR,MCPC};
    parameter mc_bit_x = 0;
    microcode_rom microcode(
        .clk(clk),
        .addr(microcode_addr_w),
        .word_out(microcode_out_w)
    );

    //main buses
    wire [7:0] W_bus;
    wire [7:0] R_bus;
    reg [7:0] ADH;
    reg [7:0] ADL;
    reg [7:0] SRWH;
    reg [7:0] SRWL;
    assign A_BUS = {ADH, ADL};

    wire [7:0] inc_dec_in_H;
    wire [7:0] inc_dec_in_L;
    wire [15:0] inc_dec_in;
    assign inc_dec_in_H = ADH; assign inc_dec_in_L = ADL;
    assign inc_dec_in = {inc_dec_in_H, inc_dec_in_L};
    wire [7:0] inc_dec_out_H;
    wire [7:0] inc_dec_out_L;
    inc_dec inc_dec1(
        .in(inc_dec_in), //connected to ADH/L
        .out({inc_dec_out_H, inc_dec_out_L}),
        .op(microcode_out_w[mc_INC_DEC_OP])
        // .w(clk)
    );
    

    //W_bus access
    always @(*) begin
        
    end

    //R_bus access
    always @(*) begin
        
    end

    //ADL access
    always @(*) begin  

    end

    //AD access
    always @(*) begin
        if(!RST) begin
            ADH <= 0;
            ADL <= 0;
        end
        else if(microcode_out_w[mc_PC_AD]) begin
            ADH <= PCH; //loads PCL/PCH onto the AD bus for the inc/dec to read
            ADL <= PCL;
        end
        else if(microcode_out_w[mc_SP_AD]) begin
            ADH <= SPH; //loads SPL/SPH onto the AD bus
            ADL <= SPL; //loads SPL/SPH onto the AD bus
        end
    end

    //SRW access
    always @(*) begin
        if(microcode_out_w[mc_INC_DEC] | microcode_out_w[mc_SP_SRW]) begin
            SRWH <= inc_dec_out_H; //connects the output of the inc/dec to the special reg bus
            SRWL <= inc_dec_out_L;
        end
    end

    //ALU module instatiation
    // ALU ALU(

    // );

    //microinstruction counter logic
    always @(posedge clk) begin
        if(!RST || microcode_out_w[mc_END]) begin
            MCPC <= 0;
            IR <= 0;
        end
        else
            MCPC <= MCPC + 1;
        if(microcode_out_w[mc_IR_DB]) //
            IR <= D_BUS;
        
    end

    //PC logic
    always @(posedge clk) begin
        if(!RST) begin
            PCL <= 0;
            PCH <= 0;
        end
        else if (microcode_out_w[mc_PC_SRW]) begin
            PCL <= SRWL;
            PCH <= SRWH;
        end

    end

    //SP Logic
    always @(posedge clk) begin
        if(!RST) begin
            SPH <= 0;
            SPL <= 0;
        end
        else if (microcode_out_w[mc_SP_SRW]) begin
            SPL <= SRWL;
            SPH <= SRWH;
        end
    end

    always @(posedge clk) begin
        if(microcode_out_w[mc_TRAP]) begin
            $display("+--------+---+--------+--------+--------+----+--------+--------+--------+----------------+--------+\n");

            $display("Trap activated!");

            $display("\n+--------+---+--------+--------+--------+----+--------+--------+--------+----------------+--------+");
            $display("|Clock # |RST|     PC |   DBus |   Abus | RW | SRWBus |     IR |   MCPC |         CurrMC |     SP |");
            $display("+--------+---+--------+--------+--------+----+--------+--------+--------+----------------+--------+");
        end
    end
    
    
endmodule