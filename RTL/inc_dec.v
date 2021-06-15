
// -----------------------------------------------------------------------------
// Author : Afonso Muralha afonsomuralha(at)gmail.com
// File   : inc_dec.v
// Create : 9/6/2021
// Revise : N/A
// Description:
//  Incrementer and decrementer module.
// -----------------------------------------------------------------------------

module inc_dec #(
    parameter NBIT = 16
) (
    input [NBIT-1:0] in,
    output reg [NBIT-1:0] out,
    input op
    // input w
);

    always @(*) begin
        if(op)
            out <= in + 1;
        else
            out <= in - 1;
    end
    
endmodule