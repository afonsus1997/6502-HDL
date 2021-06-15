cpu_test:
	@iverilog top_tb.v CPU_top.v inc_dec.v microcode_rom.v -o cpu_test.out
	@./cpu_test.out 

cpu_test_wave:
	@iverilog top_tb.v CPU_top.v inc_dec.v microcode_rom.v -o cpu_test.out
	@./cpu_test.out 
	@gtkwave cpu_test.vcd gtkcpu.gtkw &