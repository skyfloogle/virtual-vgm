!ORG 0xfffff000
!SEEK 0x168

!ALIAS r11, hw_regs
!ALIAS r12, vip_regs
!ALIAS r13, timer_latch
!ALIAS r14, song_count
!ALIAS r15, cursor
!ALIAS r16, current_song_start
!ALIAS r17, current_song_cursor
!ALIAS r18, current_ticks
!ALIAS r19, current_samples
!ALIAS r20, total_samples
!ALIAS r21, last_input
!ALIAS r22, objects

start:
	; init constants
	movhi 0x0200, r0, hw_regs
	?mov 0x5f800, vip_regs
	?mov 0x3ffe8, objects
	; init variables
	mov r0, current_song_cursor
	mov r0, cursor
	mov 2, last_input

	; wait for ram
	movea 0x2000, r0, r6
.wait_for_ram_loop:
	add -1, r6
	bnz .wait_for_ram_loop

	; enable instruction cache
	mov 2, r1
	ldsr r1, chcw

	; not sure whether vram or wram needs reads so do both

	; dummy reads from vram
	movhi 2, r0, r6
	mov 8, r7
.dummy_read_vram:
	add -1, r7
	ld.b 0[r6], r8
	bne .dummy_read_vram

	; dummy reads from wram
	movhi 5, r0, r6
	mov 8, r7
.dummy_read_wram:
	add -1, r7
	ld.b 0[r6], r8
	bne .dummy_read_wram

	; set up column table
	?MOV data.column_table, r6
	movea 0x80, r6, r7
	?MOV 0x3dc00, r8
	mov r7, r9
.column_table_loop:
	add -1, r7
	in.b 0[r6], r10
	st.h r10, 0x000[r8]
	st.h r10, 0x200[r8]
	in.b 0[r7], r10
	st.h r10, 0x100[r8]
	st.h r10, 0x300[r8]
	add 1, r6
	add 2, r8
	cmp r6, r9
	bne .column_table_loop

	; load font
	mov r0, r26
	mov r0, r27
	?MOV 256*8*8*8, r28
	movea 0x6000, r0, r29
	?MOV font, r30
	movbsu

	; clear tilemap
	movhi 2, r0, r29
	mov r0, r26
	mov r0, r27
	?MOV 64*64*8*2*8, r28
	mov r29, r30
	xorbsu

	; set up header
	mov r0, r26
	mov r0, r27
	?MOV 8*2*12, r28
	?MOV 0x22000, r29
	?MOV data.head, r30
	movbsu

	; set up ui
	mov r0, r26
	mov r0, r27
	?MOV 8*2*12, r28
	?MOV 0x24000, r29
	?MOV data.ui, r30
	movbsu

	; load world data
	?MOV 32 * 29 + 0x3d800, r29
	?MOV 0x40, r6
	st.h r6, -64[r29]
	?MOV 0xf000, r6
	st.h r6, -32[r29]
	mov r0, r26
	mov r0, r27
	?MOV 8*3*32, r28
	?MOV data.worlds, r30
	movbsu

	; set up now-playing sprite
	?MOV 1023, r6
	st.h r6, 0x4e[vip_regs]
	add -3, r6
	st.h r6, 0x4c[vip_regs]

	; jx
	mov 8, r6
	st.h r0, 0[objects]
	st.h r0, 8[objects]
	st.h r6, 16[objects]
	; jp
	movea 0xc000, r0, r6
	st.h r6, 2[objects]
	st.h r6, 10[objects]
	st.h r6, 18[objects]
	; jy
	mov -8, r6
	st.h r6, 4[objects]
	st.h r6, 12[objects]
	st.h r6, 20[objects]
	; jca
	movea 0x7f, r0, r6
	st.h r6, 6[objects]
	mov 1, r6
	st.h r6, 14[objects]
	mov 2, r6
	st.h r6, 22[objects]

	; load colours
	movea 32, r0, r6
	st.h r6, 0x24[vip_regs]
	st.h r6, 0x28[vip_regs]
	shl 1, r6
	st.h r6, 0x26[vip_regs]
	st.h r0, 0x2a[vip_regs]
	movea 0xe4, r0, r6
	st.h r6, 0x60[vip_regs]
	st.h r6, 0x68[vip_regs]

	; draw initial cursor
	mov 11, r6
	movhi 2, r0, r7

	st.h r6, 0[r7]
	; draw song names
	movhi 0x0700, r0, r6
	ld.h 0[r6], song_count
	add 2, r6
	mov song_count, r9
.text_loop:
	add 2, r7
	ld.b 0[r6], r8
	add 1, r6
	cmp r0, r8
	st.b r8, 0[r7]
	bne .text_loop
	; next song
	movea -0x80, r0, r1
	movea 63*2, r7, r7
	and r1, r7
	add -1, r9
	bne .text_loop
	
	; align to 4 bytes
	mov -4, r1
	add 3, r6
	and r1, r6

	; load song pointers
	mov song_count, r9
	movhi 0x0500, r0, r7
.song_pointer_loop:
	st.w r6, 0[r7]
	add 4, r7
	ld.w 4[r6], r8
	add 7, r8 ; align to 4 bytes + the offset of 4
	and r1, r8 ; reusing from earlier
	add r8, r6
	add -1, r9
	bne .song_pointer_loop

	; shrink name world
	?mov 32 * 29 + 0x3d800, r7
	mov song_count, r6
	shl 3, r6
	add -1, r6
	st.h r6, 16[r7]

    ; clear vsu data
    movhi 0x0100, r0, r10
    mov 1, r7
    mov r10, r6
    st.b r7, 0x580[r10]
    movea 0x554, r6, r7
.vsu_clear_loop:
    st.b r0, 0[r6]
    add 4, r6
    cmp r6, r7
    bne .vsu_clear_loop

	; intro chime
	mov r10, r7
	?mov data.wave, r6
	movea 32, r0, r8
.sine_loop:
	ld.b 0[r6], r9
	add 1, r6
	st.b r9, 0[r7]
	add 4, r7
	add -1, r8
	bne .sine_loop

	mov -1, r6
	st.b r6, 0x404[r10]
	movea 0x05ab, r0, r6
	st.b r6, 0x408[r10]
	shr 8, r6
	st.b r6, 0x40c[r10]
	movea 0xf1, r0, r7
	st.b r7, 0x410[r10]
	mov 1, r6
	st.b r6, 0x414[r10]
	shl 7, r6
	st.b r6, 0x400[r10]

	?mov 6000, r6
	st.b r6, 0x18[hw_regs]
	shr 8, r6
	st.b r6, 0x1c[hw_regs]

	mov -0x7, r8
	st.b r8, 0x20[hw_regs]

	mov 1, timer_latch
	; enable interrupts
	ldsr r0, psw
.chime_loop1:
	cmp r0, timer_latch
	bne .chime_loop1

	movea 0x0626, r0, r6
	st.b r7, 0x410[r10]
	st.b r6, 0x408[r10]
	shr 8, r6
	st.b r6, 0x40c[r10]

	st.b r8, 0x20[hw_regs]
	mov 1, timer_latch
.chime_loop2:
	cmp r0, timer_latch
	bne .chime_loop2

	movea 0x0671, r0, r6
	st.b r7, 0x410[r10]
	st.b r6, 0x408[r10]

	st.b r8, 0x20[hw_regs]
	mov 1, timer_latch
.chime_loop3:
	cmp r0, timer_latch
	bne .chime_loop3

	movea 0x06d5, r0, r6
	st.b r7, 0x410[r10]
	st.b r6, 0x408[r10]

	; enable drawing early to prevent glitch flash
	movea 0x0302, r0, r8
	st.h r8, 0x42[vip_regs]

	; wait for mirrors to stabilize
	movea 0x40, r0, r7
.mirror_wait:
	ld.h 0x20[vip_regs], r6
	and r7, r6
	be .mirror_wait

	; enable displaying and vip interrupts
	st.h r8, 0x22[vip_regs]
	movea 0x4010, r0, r6
	st.h r6, 0x02[vip_regs]

!include "playback.s" ; starts with spinloop

!include "ui.s"
!include "font.s"

; rom header
!SEEK 0xde0
?STRING "Virtual VGM         "
?db 0,0,0,0,0
?STRING "FLVGMP"
?db 0

; exception handlers
!SEEK 0xe10
	mov -0xf, r1
	mov r0, timer_latch
	st.b r1, 0x20[hw_regs]
	reti

!SEEK 0xe40
	; load INTPND
	ld.h 0[vip_regs], r6
	; check against framestart
	andi 0x10, r6, r6
	jr ui.vip

; this stuff is small enough to fit into the column table
; so let's save maximum space ayy
!include "data.s"

!SEEK 0xff0
	jr start
	?dw 0,0,0

