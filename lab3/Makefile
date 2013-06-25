%: %.o
	gcc -m32 -g -o $@ $<

%.o: %.asm
	nasm -f elf -g -F stabs $<

.PHONY: clean
clean:
	rm *~
