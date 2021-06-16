
// -----------------------------------------------------------------------------
// Author : Afonso Muralha afonsomuralha(at)gmail.com
// File   : program_rom.v
// Create : 12/6/2021
// Revise : N/A
// Description:
//  Program ROM.
// -----------------------------------------------------------------------------

module program_rom #(
    parameter WORD_SIZE = 8,
    parameter NBIT = 15
) (
    input [NBIT-1:0] addr,
    input nCE,
    output reg [WORD_SIZE-1:0] word_out
);

    

    reg [WORD_SIZE-1:0] mem [2**NBIT-1:0];

    initial begin
        $readmemh("program_ROM.hex", mem, 0); 
    end

    always @(*) begin
        //if(nCE)//!nCE
            word_out <= mem[addr];
    end
    
endmodule