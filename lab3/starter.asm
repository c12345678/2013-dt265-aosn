section     .text
global      _start                              ;must be declared for linker (ld)

_start:                                         ;tell linker entry point

    ; Your code goes here

    mov     eax,1                               ;system call number (sys_exit)
    int     0x80                                ;call kernel

section     .data

    ; Your labeled data goes here
