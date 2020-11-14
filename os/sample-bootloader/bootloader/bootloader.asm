
; the starting address point
org 0x7c00

bits 16
start:
	jmp boot


; const definitions

; the constants after are probably something such as '\n\r\0'
msg db "Hi", 0ah, 0dh, 0h

boot:
	cli
	cld

	mov ax, 0x50

	mov es, ax
	xor bx, bx


	; Read the OS from disk

	; AL -> Num of sector reads
	; CH -> Track/cylinder num
	; CL -> Sector num
	; DH -> Head num
	; DL -> Drive num (floppy, drive 1, drive 2, etc.)
	; ES:BX -> Ptr to buffer storage
	; Return:
	; AH -> Status
	; AL -> Num of sector reads
	; CF -> 0 (success) or 1 (error)
	mov al, 2
	mov ch, 0
	mov cl, 2
	mov dh, 0
	mov dl, 0

	mov ah, 0x02
	int 0x13

	; jump there and execute
	jmp 0x50:0x0

	hlt

times 510 - ($-$$) db 0
dw 0xaa55
