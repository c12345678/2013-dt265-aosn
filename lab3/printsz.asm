section     .text
global      _start                              ;must be declared for linker (ld)

_start:                                         ;tell linker entry point

    ; By convention, eax, ecx and edx are designated caller-saved registers
    ; All others are considered callee-saved
    push    eax					;preserve eax contents
    push    ecx					;preserve ecx contents
    push    edx					;preserve edx contents
    mov	    eax, msg				;get the start of the message to print
    push    eax					;put it on the stack (argument to function)
    call    printsz				;call the print function
    add     esp, 4				;restore stack (removing arguments)
    pop     edx					;restore edx contents
    pop     ecx					;restore ecx contents
    pop     eax					;restore eax contents

    mov     eax, 1                              ;system call number (sys_exit)
    int     0x80                                ;call kernel

printsz:
    ; Function to print a zero terminated string
    ; Takes a single argument passed on the stack as the address of the string to print
    ; Preserves working registers ebp, ebx and esi (callee-saved)
    push    ebp					;preserve base pointer register
    mov     ebp, esp 				;set base address of the function argument list
    push    ebx					;preserve ebx contents
    push    esi					;preserve esi contents
    mov     esi, [ebp + 8]			;get address of string to print from stack
    xor     edx, edx				;initialise length to zero
.getlen:
    cmp     BYTE[esi], 0			;compare the next byte of the message string
    jz      .gotlen				;we've hit the zero byte string terminator
    inc     esi					;otherwise, advance to next byte of string
    inc     edx					;increase the length by one
    jmp     .getlen				;and go around again
.gotlen:
    mov     ecx, [ebp + 8]			;get the address of the string for printing
    mov     ebx, 1				;set to output to console (screen)
    mov     eax, 4                              ;set system call number (sys_write)
    int     0x80                                ;call kernel routine
    pop     esi					;restore esi contents
    pop     ebx					;restore ebx contents
    pop     ebp					;restore ebp contents
    ret						;return from this function back to caller

section     .data

msg: db 'This is a zero-terminated string!', 0x0a, 0
