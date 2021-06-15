// -----------------------------------------------------------------------------
// Author : Afonso Muralha afonsomuralha(at)gmail.com
// File   : reg.v
// Create : 9/6/2021
// Revise : N/A
// Description:
//  Register module.
// -----------------------------------------------------------------------------

module register #(
    parameter NBIT = 16;
) (
    input [NBIT-1:0] in,
    output [NBIT-1:0] out,
    input w
);

    always @(posedge w) begin
        out <= in;
    end
    
endmodule