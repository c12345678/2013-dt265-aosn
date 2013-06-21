; Sum the first 9 numbers and print the result
;
extern      printf				;import external library symbol

section     .text
global      main                                ;standard gcc entry point

main:                                           ;tell linker entry point
    xor     ecx, ecx				;initialise accumulator to zero
    mov     ebx, 9				;starting with the number 9
.loop:
    add     ecx, ebx				;add next in sequence to total
    cmp     ebx, 0				;are we done?
    jz      .done				;yes!
    dec     ebx					;no, so subtract 1
    jmp     .loop
.done:
    
    ; Easiest way to print numbers is to call the printf library (from C)
    ; to do this for us
    push    ecx					;push second parameter (for printf)
    push    fmt					;push first parameter (for printf)
    call    printf				;call printf function
    add     esp, 8				;restore the stack frame (removing args)
    
    mov     eax, 1                              ;system call number (sys_exit)
    int     0x80                                ;call kernel

section     .data

; printf expects a null terminated format string as its first parameter
fmt: db "Sum=%d", 0x0a, 0
