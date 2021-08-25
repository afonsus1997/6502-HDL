cpu_test:
	@python ../Tools/write_microcode_mem.py
	@iverilog top_tb.v CPU_top.v inc_dec.v microcode_rom.v program_rom.v -o cpu_test.out
	@./cpu_test.out 

# cpu_test:
# 	@iverilog top_tb.v -o cpu_test.out
# 	@./cpu_test.out 

cpu_test_wave:
	@iverilog top_tb.v CPU_top.v inc_dec.v microcode_rom.v program_rom.v -o cpu_test.out
	@./cpu_test.out 
	@gtkwave cpu_test.vcd gtkcpu.gtkw &