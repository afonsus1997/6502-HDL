
// -----------------------------------------------------------------------------
// Author : Afonso Muralha afonsomuralha(at)gmail.com
// File   : microcode_rom.v
// Create : 12/6/2021
// Revise : N/A
// Description:
//  Microcode ROM.
// -----------------------------------------------------------------------------

module microcode_rom #(
    parameter WORD_SIZE = 16,
    parameter ROM_SIZE = 1024
) (
    input clk,
    input [$clog2(ROM_SIZE)-1:0] addr,
    output reg [WORD_SIZE-1:0] word_out
);

    

    reg [WORD_SIZE-1:0] mem[ROM_SIZE-1:0];

    initial begin
        $readmemb("microcode.hex", mem, 0); 
    end

    always @(posedge clk) begin
        word_out <= mem[addr];
    end
    
endmodule