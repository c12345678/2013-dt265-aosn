%: %.o
	gcc -m32 -o $@ $<

%.o: %.asm
	nasm -f elf $<

.PHONY: clean
clean:
	rm *~
