%: %.o
	ld -s -g -melf_i386 -o $@ $<

%.o: %.asm
	nasm -f elf -g $<

.PHONY: clean
clean:
	rm *~
