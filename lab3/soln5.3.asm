; Sum and average an array of numbers and print the results
;
extern      printf				;import external library symbol

section     .text
global      main                                ;standard gcc entry point

main:                                           ;tell linker entry point
    ; Compute the sum
    xor     eax, eax				;initialise accumulator to zero
    mov     ecx, count				;count of numbers in the list
    mov     esi, nums				;addess of first number
.loop:
    add     eax, [esi]				;add next in list to total
    cmp     ecx, 0				;are we done?
    jz      .done				;yes!
    dec     ecx					;no, so subtract 1 from count
    add     esi, 4				;advance to the next number in the list
    jmp     .loop
.done:

    ; Compute the average from the sum and count
    mov     ebx, eax				;make a copy of the computed sum
    xor     edx, edx				;clear top half of dividend, eax is lower half
    mov     ecx, count				;divisor is count
    div     ecx					;get the average (result is placed in eax)
    
    ; Easiest way to print numbers is to call the printf library (from C)
    ; to do this for us
    push    eax					;third parameter (for printf) is average
    push    ebx					;second parameter (for printf) is sum
    push    fmt					;first parameter (for printf) format string
    call    printf				;call printf function
    add     esp, 12				;restore the stack frame (removing args)
    
    mov     eax, 1                              ;system call number (sys_exit)
    mov     ebx, 0                              ;program return code (0 means no error)
    int     0x80                                ;call kernel

section     .data

; printf expects a null terminated format string as its first parameter
fmt: db "Sum=%d, Average=%d", 0x0a, 0

nums: dd 12, 14, 45, 24, 76, 23, 65, 2, 54, 65, 65, 76, 34, 100, 32, 1
count equ ($ - nums) / 4			;each number occupies 4 bytes of memory
