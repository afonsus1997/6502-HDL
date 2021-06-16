`timescale 1ns / 1ps



module cpu_tb;
   
    reg reset;
    reg clock;
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
    end

    initial begin
        #1;
        reset = 0;
        #6
        reset = 1;
    end

    initial begin
        #100 $finish;
    end


    always begin
        #2  clock =  ! clock;
    end

endmodule