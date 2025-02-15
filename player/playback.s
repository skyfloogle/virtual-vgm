playback:

.process_song:
	cmp r0, current_song_cursor
	be .process_song

	sei
	; set reload to 0xff so we can add it later
	mov -1, r6
	st.b r6, 0x18[hw_regs]

	; constants
	movea 0xc7, r0, r10
	movhi 0x0100, r0, r1
.data_loop:
	in.b 0[current_song_cursor], r6
	in.b 1[current_song_cursor], r7
	in.b 2[current_song_cursor], r8
	in.b 3[current_song_cursor], r9
	cmp r10, r6
	bne .process_cmd
	add 4, current_song_cursor
	shl 8, r7
	add r8, r7
	shl 2, r7
	add r1, r7
	st.b r9, 0[r7]
	br .data_loop

.process_cmd:
	movea 0x61, r0, r9
	cmp r9, r6
	be .wait_delay
	add 1, r9
	cmp r9, r6
	be .wait_ntsc
	add 1, r9
	cmp r9, r6
	be .wait_pal
	br .song_end
.wait_delay:
	shl 8, r8
	add r8, r7
	add 3, current_song_cursor
	br .wait_commit
.wait_ntsc:
	movea 735, r0, r7
	add 1, current_song_cursor
	br .wait_commit
.wait_pal:
	movea 882, r0, r7
	add 1, current_song_cursor
.wait_commit:
	; r7 contains samples to wait
	add r7, current_samples
	movea 1000, r0, r6
	movea 882, r0, r7
	mul current_samples, r6
	div r7, r6
	ld.b 0x18[hw_regs], r7 ; add additional possible elapsed ticks
	sub current_ticks, r6
	add r6, current_ticks
	add r7, r6
	ble .process_song ; if we somehow exceeded the wait time during processing, don't wait again
	; save wait time
	st.b r6, 0x18[hw_regs]
	shr 8, r6
	st.b r6, 0x1c[hw_regs]
	; activate timer & interrupt
	mov -0x7, r6
	st.b r6, 0x20[hw_regs]
	mov 1, timer_latch
	cli
.wait_spin:
	cmp r0, timer_latch
	bne .wait_spin
	br .process_song
.song_end:
    ld.w 0x1c[current_song_start], r6
    cmp r0, r6
    be .playback_end
    addi 0x1c, current_song_start, current_song_cursor
    add r6, current_song_cursor
    cli
    br .process_song
.playback_end:
    ; stop sound
    mov 1, r6
    movhi 0x0100, r0, r7
    movea 0x0580, r7, r7
    st.b r6, 0[r7]

    ; hide now-playing cursor
    mov -8, r6
    st.h r6, 4[objects]

	mov r0, current_song_cursor
	cli
	br .process_song
