`timescale 1ns / 1ps



module cpu_tb;
   
    reg reset;
    reg clock;
    integer clockn;
    wire [15:0] addr_bus_w;
    wire [7:0] data_bus_w;

    program_rom PROG_ROM(
        .addr(addr_bus_w[14:0]),
        .nCE(addr_bus_w[15]),
        .word_out(data_bus_w)
    );

    CPU uut (
        // .RDY,
        .clk(clock),
        .RST(reset),
        // .NMI,
        // .SO,
        // .IRQ,
        .A_BUS(addr_bus_w),
        .D_BUS(data_bus_w)
        // .RW,
        // .SYNC,
        // .PHI_1_OUT,
        // .PHI_2_OUT,

        //aux outputs
        // output [7:0] SR_OUT;
    );

    initial begin
        $dumpfile("cpu_test.vcd");
        $dumpvars();
        clock = 0;
        reset = 0;
        clockn = 0;
    end

    initial begin
        #1;
        reset = 0;
        #6
        reset = 1;
    end

    initial begin
        $display("\n\n\n");
        $display("+--------+---+--------+--------+--------+----+--------+--------+--------+----------------+--------+");
        $display("|Clock # |RST|     PC |   DBus |   Abus | RW | SRWBus |     IR |   MCPC |         CurrMC |     SP |");
        $display("+--------+---+--------+--------+--------+----+--------+--------+--------+----------------+--------+");
        #70 
        $display("+--------+---+--------+--------+--------+----+--------+--------+--------+----------------+--------+");
        $display("\n\n\n");
        $finish;
        
    end

    // always @(posedge clock) begin
        
    // end


    always begin
        #2  clock =  ! clock;
        
    end

    always @(posedge clock) begin
        clockn++;
        if(clockn >=2)
            $display("|%8h| %1d |%8h|%8h|%8h| %1d  |%8h|%8h|%8h|%16b|%8h|",clockn, reset, {uut.PCH,uut.PCL}, addr_bus_w, data_bus_w, uut.RW, {uut.SRWH, uut.SRWL}, uut.IR, uut.MCPC, uut.microcode_out_w, {uut.SPH,uut.SPH});
    end


endmodule