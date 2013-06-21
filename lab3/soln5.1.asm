; Show the x86 add instruction in practice
;
extern      printf				;import external library symbol

section     .text
global      main                                ;standard gcc entry point

main:                                           ;tell linker entry point
    mov     ebx, 10				;first number
    mov     ecx, 20				;second number
    add     ecx, ebx				;sum them, leaving the result in ecx
    
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
