section     .text
global      _start                              ;must be declared for linker (ld)

_start:                                         ;tell linker entry point

    mov     eax, DWORD [x]			;get contents of x
    mov     ebx, DWORD [y]			;get contents of y
    cmp     eax, ebx				;compare them
    jl      .xless				;if x < y
.xgreater:					;else y >= x
    mov     edx,len1                            ;length
    mov     ecx,msg1                            ;content
    mov     ebx,1                               ;file descriptor (stdout)
    mov     eax,4                               ;system call number (sys_write)
    int     0x80                                ;call kernel
    jmp     .done
.xless:
    mov     edx,len2                            ;length
    mov     ecx,msg2                            ;content
    mov     ebx,1                               ;file descriptor (stdout)
    mov     eax,4                               ;system call number (sys_write)
    int     0x80                                ;call kernel
    jmp     .done
.done:
    mov     eax,1                               ;system call number (sys_exit)
    int     0x80                                ;call kernel

section     .data

x:    dd    30
y:    dd    20
msg1: db    "x is greater than y", 0xa
len1  equ   $ - msg1
msg2: db    "x is less than y", 0xa
len2  equ   $ - msg2

