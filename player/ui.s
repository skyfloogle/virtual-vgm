ui:
.framestart:
    mov -2, r7
    ; acknowledge interrupt
    st.h r6, 4[vip_regs]
    ; start hardware read
    st.b r7, 0x28[hw_regs]
    reti

.vip:
    ; if we hit framestart the flag is still there
    bne .framestart
    ; acknowledge interrupt
    mov -1, r6
    mov 2, r7
    st.h r6, 4[vip_regs]
    ; wait for input
.input_wait:
    ld.b 0x28[hw_regs], r6
    and r7, r6
    bne .input_wait
    in.b 0x14[hw_regs], r7
    in.b 0x10[hw_regs], r6
    shl 8, r7
    add r7, r6
    mov last_input, r9
    mov r6, last_input
    ; get pressed keys
    xor r6, r9
    and r6, r9

    ; battery indicator
    shr 1, r6
    setfc r7
    movea 224, r0, r6
    shl 3, r7
    sub r7, r6
    st.h r6, 12[objects]
    st.h r6, 20[objects]

    ; if we pressed a, then start
    mov 4, r6
    and r9, r6
    bne .start_song

    mov 8, r6
    and r9, r6
    bne .stop_song

    ; up/down -> cursor
    movea 0x0c00, r0, r6
    and r9, r6
    bne .cursor_move

    reti

.cursor_move:
    mov cursor, r6
    shl 7, r6
    movhi 2, r6, r6
    st.h r0, 0[r6]

    movea 0x0400, r0, r6
    and r9, r6
    bne .input_down

    movea 0x0800, r0, r6
    and r9, r6
    bne .input_up

.input_up:
    add -1, cursor
    bge .cursor_move_finish
    mov song_count, cursor
    add -1, cursor
    br .cursor_move_finish

.input_down:
    add 1, cursor
    cmp song_count, cursor
    blt .cursor_move_finish
    mov r0, cursor

.cursor_move_finish:
    mov 11, r7
    mov cursor, r6
    shl 7, r6
    movhi 2, r6, r6
    st.h r7, 0[r6]
    reti

.stop_song:
    mov r0, current_song_cursor
    ; stop sound
    movhi 0x0100, r0, r6
    mov 1, r7
    st.b r7, 0x580[r6]
    ; hide now-playing sprite
    mov -8, r6
    st.h r6, 4[objects]
    reti

.start_song:
    mov r0, current_ticks
    mov r0, current_samples
    mov cursor, r6
    shl 2, r6
    movhi 0x0500, r6, r6
    ld.w 0[r6], current_song_start
    ld.w 0x18[current_song_start], total_samples
    ld.w 0x34[current_song_start], current_song_cursor
    addi 0x34, current_song_start, r6
    mov r0, timer_latch
    add r6, current_song_cursor

    ; set now-playing cursor
    mov cursor, r6
    shl 3, r6
    add 8, r6
    st.h r6, 4[objects]

    ; clear vsu data
    movhi 0x0100, r0, r6
    mov 1, r7
    st.b r7, 0x580[r6]
    movea 0x554, r6, r7
.vsu_clear_loop:
    st.b r0, 0[r6]
    add 4, r6
    cmp r6, r7
    bne .vsu_clear_loop

    ; wait for the timer to tick, for consistency
    mov 1, r6
    st.h r6, 0x18[hw_regs]
.timer_loop:
    ld.h 0x18[hw_regs], r6
    cmp r0, r6
    bne .timer_loop

    reti
