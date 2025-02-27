#!/usr/bin/env python
# Generates "vsutest.vgm".

# This is effectively a stream of raw VGM commands with some syntactic sugar.
# Quick primer on the relevant VGM commands:
# * C7 - Write a byte to a VSU register.
#   During playback, the address will be shifted left twice.
# * 61 - Wait for some number of samples.
#   The VGM format specifies that the sample rate is 44100Hz.
# * 62 - Wait for 1/60 seconds.
# * 63 - Wait for 1/50 seconds.
# * 66 - End data.
# I have also included a "repeat" block which repeats the given commands,
# and comments on lines starting with '#'.
commands = """
c7 0160 ff

# initial channel setup
c7 0101 ff
c7 0102 64
c7 0103 07
c7 0104 f0
c7 0105 00
c7 0106 00

# sine wave
c7 0000 23
c7 0001 29
c7 0002 2e
c7 0003 33
c7 0004 38
c7 0005 3b
c7 0006 3e
c7 0007 3f
c7 0008 3f
c7 0009 3e
c7 000a 3b
c7 000b 38
c7 000c 33
c7 000d 2e
c7 000e 29
c7 000f 23
c7 0010 1c
c7 0011 16
c7 0012 11
c7 0013 0c
c7 0014 07
c7 0015 04
c7 0016 01
c7 0017 00
c7 0018 00
c7 0019 01
c7 001a 04
c7 001b 07
c7 001c 0c
c7 001d 11
c7 001e 16
c7 001f 1c

# square wave
c7 0020 00
c7 0021 00
c7 0022 00
c7 0023 00
c7 0024 00
c7 0025 00
c7 0026 00
c7 0027 00
c7 0028 40
c7 0029 40
c7 002a 40
c7 002b 40
c7 002c 40
c7 002d 40
c7 002e 40
c7 002f 40
c7 0030 ff
c7 0031 ff
c7 0032 ff
c7 0033 ff
c7 0034 ff
c7 0035 ff
c7 0036 ff
c7 0037 ff
c7 0038 3f
c7 0039 3f
c7 003a 3f
c7 003b 3f
c7 003c 3f
c7 003d 3f
c7 003e 3f
c7 003f 3f

# sawtooth wave
c7 0040 00
c7 0041 02
c7 0042 04
c7 0043 06
c7 0044 08
c7 0045 0a
c7 0046 0c
c7 0047 0e
c7 0048 10
c7 0049 12
c7 004a 14
c7 004b 16
c7 004c 18
c7 004d 1a
c7 004e 1c
c7 004f 1e
c7 0050 21
c7 0051 23
c7 0052 25
c7 0053 27
c7 0054 29
c7 0055 2b
c7 0056 2d
c7 0057 2f
c7 0058 31
c7 0059 33
c7 005a 35
c7 005b 37
c7 005c 39
c7 005d 3b
c7 005e 3d
c7 005f 3f

# triangle wave
c7 0060 00
c7 0061 04
c7 0062 08
c7 0063 0c
c7 0064 10
c7 0065 14
c7 0066 18
c7 0067 1c
c7 0068 21
c7 0069 25
c7 006a 29
c7 006b 2d
c7 006c 31
c7 006d 35
c7 006e 39
c7 006f 3d
c7 0070 3d
c7 0071 39
c7 0072 35
c7 0073 31
c7 0074 2d
c7 0075 29
c7 0076 25
c7 0077 21
c7 0078 1c
c7 0079 18
c7 007a 14
c7 007b 10
c7 007c 0c
c7 007d 08
c7 007e 04
c7 007f 00

# sawtooth again, to be overwritten
c7 0080 00
c7 0081 02
c7 0082 04
c7 0083 06
c7 0084 08
c7 0085 0a
c7 0086 0c
c7 0087 0e
c7 0088 10
c7 0089 12
c7 008a 14
c7 008b 16
c7 008c 18
c7 008d 1a
c7 008e 1c
c7 008f 1e
c7 0090 21
c7 0091 23
c7 0092 25
c7 0093 27
c7 0094 29
c7 0095 2b
c7 0096 2d
c7 0097 2f
c7 0098 31
c7 0099 33
c7 009a 35
c7 009b 37
c7 009c 39
c7 009d 3b
c7 009e 3d
c7 009f 3f

# beeps
c7 0100 ba
61 ac44

c7 0100 ba
repeat 4
    61 2b11
done

c7 0100 ba
repeat 12
    61 0e5b
done

c7 0100 ba
repeat 25
    61 06e4
done

c7 0100 ba
repeat 50
    63
done
c7 0100 9f
repeat 490
    61 002d
done

c7 0100 00
61 5622

# auto shutoff
c7 0100 a0
61 5622

c7 0100 a1
61 5622

c7 0100 a2
61 5622

c7 0100 bf
61 5622

c7 0106 01

# volume / pan test
c7 0102 9d
c7 0103 06

c7 0100 80
61 113a
c7 0101 fe
61 113a
c7 0101 fd
61 113a
c7 0101 fc
61 113a
c7 0101 fb
61 113a
c7 0101 fa
61 113a
c7 0101 f9
61 113a
c7 0101 f8
61 113a
c7 0101 f7
61 113a
c7 0101 f6
61 113a
c7 0101 f5
61 113a
c7 0101 f4
61 113a
c7 0101 f3
61 113a
c7 0101 f2
61 113a
c7 0101 f1
61 113a
c7 0101 f0
61 5622

c7 0101 e1
61 113a
c7 0101 d2
61 113a
c7 0101 c3
61 113a
c7 0101 b4
61 113a
c7 0101 a5
61 113a
c7 0101 96
61 113a
c7 0101 87
61 113a
c7 0101 78
61 113a
c7 0101 69
61 113a
c7 0101 5a
61 113a
c7 0101 4b
61 113a
c7 0101 3c
61 113a
c7 0101 2d
61 113a
c7 0101 1e
61 113a
c7 0101 0f
61 5622

c7 0104 e0
61 113a
c7 0104 d0
61 113a
c7 0104 c0
61 113a
c7 0104 b0
61 113a
c7 0104 a0
61 113a
c7 0104 90
61 113a
c7 0104 80
61 113a
c7 0104 70
61 113a
c7 0104 60
61 113a
c7 0104 50
61 113a
c7 0104 40
61 113a
c7 0104 30
61 113a
c7 0104 20
61 113a
c7 0104 10
61 113a
c7 0104 00
61 5622

# reset pan
c7 0100 00
c7 0101 ff

# quick sine
c7 0106 00
c7 0105 00
c7 0104 f0
c7 0100 80
61 5622
c7 0100 00
c7 0106 01
61 5622

# fades at different speeds
c7 0105 01
c7 0104 08
c7 0100 80
61 5622
c7 0104 f0
c7 0100 80
61 5622

c7 0104 0f
c7 0100 80
61 ac44
61 ac44
61 5622
c7 0104 f7
c7 0100 80
61 ac44
61 ac44
61 5622

# quick sine
c7 0106 00
c7 0105 00
c7 0104 f0
c7 0100 80
61 5622
c7 0100 00
c7 0106 01
61 5622


# update fade during fade
c7 0105 01
c7 0104 0b
c7 0100 80
61 5622
c7 0105 00
61 2b11
c7 0105 01
61 2b11
c7 0104 f5
61 ac44
c7 0104 f5
61 ac44
c7 0105 03
61 ac44
c7 0104 f0
61 ac44
c7 0104 08
61 ac44

c7 0100 00
61 5622

# quick sine
c7 0106 00
c7 0105 00
c7 0104 f0
c7 0100 80
61 5622
c7 0100 00
c7 0106 01
61 5622

c7 0105 01

# set to high volume with fadeout and write to all registers
c7 0104 f0
61 2b11
c7 0104 00
61 2b11

c7 0104 f0
c7 0100 80
61 2b11
c7 0104 00
61 2b11

c7 0104 f0
c7 0101 ff
61 2b11
c7 0104 00
61 2b11

c7 0104 f0
c7 0102 9d
61 2b11
c7 0104 00
61 2b11

c7 0104 f0
c7 0103 06
61 2b11
c7 0104 00
61 2b11

c7 0104 f0
c7 0105 01
61 2b11
c7 0104 00
61 2b11

c7 0104 f0
c7 0106 01
61 2b11
c7 0104 00
61 2b11

# set to low volume with fadein and write to all registers
c7 0104 08
61 2b11

c7 0104 08
c7 0100 80
61 2b11
c7 0104 f8
61 2b11

c7 0104 08
c7 0101 ff
61 2b11
c7 0104 f8
61 2b11

c7 0104 08
c7 0102 9d
61 2b11
c7 0104 f8
61 2b11

c7 0104 08
c7 0103 06
61 2b11
c7 0104 f8
61 2b11

c7 0104 08
c7 0105 01
61 2b11
c7 0104 f8
61 2b11

c7 0104 08
c7 0106 01
61 2b11
c7 0104 f8
61 2b11

# fadeout after fadein is done
c7 0104 f0
61 5622

# quick sine
c7 0106 00
c7 0105 00
c7 0104 f0
c7 0100 80
61 5622
c7 0100 00
c7 0106 01
61 5622

# pause channel during fade
c7 0105 01
c7 0104 f3
c7 0100 80
61 2b11
c7 0100 00
63
c7 0100 80
61 2b11
c7 0104 4b
61 2b11
c7 0100 00
63
c7 0100 80
61 2b11

c7 0100 00
61 2b11

# quick sine
c7 0106 00
c7 0105 00
c7 0104 f0
c7 0100 80
61 5622
c7 0100 00
c7 0106 01
61 5622

# try and set immediately after hitting zero
c7 0105 01
c7 0104 30
c7 0100 80
61 069c
c7 0104 30
61 069c
c7 0104 30
61 069c
c7 0104 30
61 0a94
c7 0104 30
61 069c
c7 0104 30
61 069c
c7 0104 30
61 069c
c7 0100 00
61 2b11

c7 0105 01
c7 0104 c8
c7 0100 80
61 069c
c7 0104 c8
61 069c
c7 0104 c8
61 069c
c7 0104 c8
61 0a94
c7 0104 c8
61 069c
c7 0104 c8
61 069c
c7 0104 c8
61 069c
c7 0100 00
61 2b11

c7 0100 00
61 2b11

# quick sine
c7 0106 00
c7 0105 00
c7 0104 f0
c7 0100 80
61 5622
c7 0100 00
c7 0106 01
61 5622

# lowest frequency
c7 0102 00
c7 0103 00
c7 0104 f0
c7 0105 00

# change wave types a few times

# sine
c7 0106 00
c7 0100 80
63
63
63
# square
c7 0106 01
63
63
63
# saw
c7 0106 02
63
63
63
# triangle
c7 0106 03
63
63
63
# square
c7 0106 01
63
63
63
c7 0100 00
61 2b11

# test when spamming each register

c7 0104 f2
c7 0105 01
repeat 25
    c7 0100 80
    63
done
61 5622
repeat 25
    c7 0100 80
    63
done
c7 0100 00
61 2b11

c7 0104 f2
c7 0100 80
repeat 25
    c7 0101 ff
    63
done
c7 0100 00
61 2b11

c7 0104 f2
c7 0100 80
repeat 25
    c7 0102 00
    63
done
c7 0100 00
61 2b11

c7 0104 f2
c7 0100 80
repeat 25
    c7 0103 00
    63
done
c7 0100 00
61 2b11

c7 0104 f2
c7 0100 80
repeat 25
    c7 0104 f2
    63
done
c7 0100 00
61 2b11

c7 0104 f2
c7 0100 80
repeat 25
    c7 0105 01
    63
done
c7 0100 00
61 2b11

c7 0104 f2
c7 0100 80
repeat 25
    c7 0106 01
    63
done
c7 0100 00
61 2b11

c7 0105 00

# change frequency mid-note
c7 0104 f0
c7 0100 80
61 2b11
c7 0102 ff
61 2b11
c7 0103 ff
61 2b11
c7 0103 07
61 2b11
c7 0102 9d
c7 0103 06
61 2b11
c7 0100 00
61 2b11

# overwriting wave while it's playing
c7 0106 04
c7 0100 80
63
63
c7 0080 00
63
63
c7 0081 00
63
63
c7 0082 00
63
63
c7 0083 00
63
63
c7 0084 00
63
63
c7 0085 00
63
63
c7 0086 00
63
63
c7 0087 00
63
63
c7 0088 00
63
63
c7 0089 00
63
63
c7 008a 00
63
63

# overwriting wave while channel is active but muted
# with S1EV0
c7 0104 00
63
c7 0090 00
c7 0091 00
c7 0092 00
c7 0093 00
c7 0094 00
c7 0095 00
c7 0096 00
c7 0097 00
61 5622
c7 0104 f0
61 2b11
# with S1LRV
c7 0101 00
61 5622
c7 0098 00
c7 0099 00
c7 009a 00
c7 009b 00
c7 009c 00
c7 009d 00
c7 009e 00
c7 009f 00
c7 0101 ff
61 2b11
c7 0100 00
61 5622

# overwriting wave while another is playing

c7 0106 00
c7 0100 80
61 2b11
c7 0080 ff
c7 0081 ff
c7 0082 ff
c7 0083 ff
c7 0084 ff
c7 0085 ff
c7 0086 ff
c7 0087 ff
c7 0088 ff
61 2b11
c7 0106 04
61 2b11
c7 0100 00
61 2b11
c7 0100 80
61 2b11
c7 0100 00
61 5622

# overwriting wave while noise is playing
c7 0151 ff
c7 0152 00
c7 0153 06
c7 0154 f0
c7 0155 00
c7 0150 80
63
c7 0090 ff
c7 0091 ff
c7 0092 ff
c7 0093 ff
c7 0094 ff
c7 0095 ff
c7 0096 ff
c7 0097 ff
61 2b11
c7 0150 00
c7 0100 80
61 2b11
c7 0100 00
61 ac44

# set up channel 5
c7 0141 ff
c7 0142 9d
c7 0143 06
c7 0144 f0
c7 0145 00
c7 0146 00
c7 0147 ff

# test channel 5 frequency limits
# going up at the top
c7 0140 80
61 2b11
c7 0143 ff
61 2b11
c7 0142 ff
61 2b11
c7 0142 9d
c7 0143 06
61 2b11
c7 0140 80
61 2b11
c7 0140 00
61 5622

# going up at the bottom
c7 0140 80
61 2b11
c7 0143 00
61 2b11
c7 0142 00
61 2b11
c7 0142 9d
c7 0143 06
61 2b11
c7 0140 00
61 5622

# going down at the top
c7 0147 f7
c7 0140 80
61 2b11
c7 0143 ff
61 2b11
c7 0142 ff
61 2b11
c7 0142 9d
c7 0143 06
61 2b11
c7 0140 00
61 5622

# going down at the bottom
c7 0140 80
61 2b11
c7 0143 00
61 2b11
c7 0142 00
61 2b11
c7 0142 9d
c7 0143 06
61 2b11
c7 0140 00
61 5622

# test sweep
c7 0145 40
c7 0147 ff
c7 0140 80
61 5622
c7 0140 00
61 2b11
c7 0140 80
61 2b11
c7 0140 80
61 5622
c7 0147 f7
61 5622
c7 0147 f3
61 ac44

# test max shift
c7 0147 f8
61 5622

# try turning on with max shift
c7 0140 80
61 2b11

# max shift down
c7 0147 f0
c7 0140 80
61 2b11
c7 0140 00
61 5622

# square
c7 0146 01
c7 0142 9d
c7 0143 06

# sweep up at a few different speeds
c7 0147 ff
c7 0140 80
61 5622

c7 0142 9d
c7 0143 06
c7 0147 cf
c7 0140 80
61 5622

c7 0142 9d
c7 0143 06
c7 0147 7f
c7 0140 80
61 5622

c7 0142 9d
c7 0143 06
c7 0147 3f
c7 0140 80
61 5622

# sweep up from the bottom
c7 0142 00
c7 0143 01
c7 0147 ff
c7 0140 80
61 5622

c7 0147 fc
61 5622

c7 0147 f9
61 5622

# spam registers
c7 0142 ff
c7 0143 06
c7 0145 40
c7 0147 a6
repeat 25
    c7 0140 80
    63
done
c7 0140 00
61 5622

c7 0142 ff
c7 0143 06
c7 0140 80
repeat 25
    c7 0142 ff
    63
done
c7 0140 00
61 5622

c7 0142 ff
c7 0143 06
c7 0140 80
repeat 25
    c7 0143 06
    63
done
c7 0140 00
61 5622

c7 0142 ff
c7 0143 06
c7 0140 80
repeat 25
    c7 0144 f0
    63
done
c7 0140 00
61 5622

c7 0142 ff
c7 0143 06
c7 0140 80
repeat 25
    c7 0145 40
    63
done
c7 0140 00
61 5622

c7 0142 ff
c7 0143 06
c7 0140 80
repeat 25
    c7 0146 01
    63
done
c7 0140 00
61 5622

c7 0142 ff
c7 0143 06
c7 0140 80
repeat 25
    c7 0147 a6
    63
done
c7 0140 00
61 5622

# set up modulation with maxint
c7 00a0 7f
c7 00a1 7f
c7 00a2 7f
c7 00a3 7f
c7 00a4 7f
c7 00a5 7f
c7 00a6 7f
c7 00a7 7f
c7 00a8 7f
c7 00a9 7f
c7 00aa 7f
c7 00ab 7f
c7 00ac 7f
c7 00ad 7f
c7 00ae 7f
c7 00af 7f
c7 00b0 7f
c7 00b1 7f
c7 00b2 7f
c7 00b3 7f
c7 00b4 7f
c7 00b5 7f
c7 00b6 7f
c7 00b7 7f
c7 00b8 7f
c7 00b9 7f
c7 00ba 7f
c7 00bb 7f
c7 00bc 7f
c7 00bd 7f
c7 00be 7f
c7 00bf 7f

# try max frequency
c7 0142 00
c7 0143 01
c7 0145 70
c7 0146 00
c7 0147 19
c7 0140 80
61 5622
c7 0142 ff
c7 0143 ff
c7 01ff 00
61 5622
c7 0145 00
61 5622
c7 0140 00
61 5622

# change first offset
c7 00a0 80

# start with modulation
c7 0142 00
c7 0143 05
c7 0147 f0
c7 0145 00
61 5622
c7 0145 70
c7 0140 80
61 5622
c7 0140 00
61 5622

# start without changing frequency
c7 0140 80
61 5622
c7 0140 00
61 5622

# show without modulation for a bit
c7 0145 00
c7 0140 80
61 5622
c7 0142 00
61 5622
c7 0140 00
c7 0145 70
61 5622

# start after changing frequency
c7 0142 80
c7 0140 80
61 5622
c7 0140 00
61 5622

# start after rewriting same frequency
c7 0142 80
c7 0140 80
61 5622
c7 0140 00
61 5622

# show without modulation for a bit
c7 0145 00
c7 0140 80
61 5622
c7 0142 80
61 5622
c7 0140 00
c7 0145 70
61 5622

# rewrite frequency then start after
c7 0142 00
61 5622
c7 0140 80
61 5622
c7 0140 00
61 5622

# change high byte
c7 0143 06
c7 0140 80
61 5622
c7 0140 00
61 5622

# change frequency and start, mid-speed
c7 0143 05
c7 0142 80
c7 0147 70
c7 0140 80
61 5622
c7 0140 00
61 5622

# set up modulation with minint
c7 00a0 80
c7 00a1 80
c7 00a2 80
c7 00a3 80
c7 00a4 80
c7 00a5 80
c7 00a6 80
c7 00a7 80
c7 00a8 80
c7 00a9 80
c7 00aa 80
c7 00ab 80
c7 00ac 80
c7 00ad 80
c7 00ae 80
c7 00af 80
c7 00b0 80
c7 00b1 80
c7 00b2 80
c7 00b3 80
c7 00b4 80
c7 00b5 80
c7 00b6 80
c7 00b7 80
c7 00b8 80
c7 00b9 80
c7 00ba 80
c7 00bb 80
c7 00bc 80
c7 00bd 80
c7 00be 80
c7 00bf 80

# try min frequency
c7 0142 00
c7 0143 03
c7 0145 70
c7 0140 80
61 5622
c7 0142 00
c7 0143 00
61 5622
c7 0145 00
61 5622
c7 0140 00
61 5622

# set up modulation
c7 00a0 80
c7 00a1 90
c7 00a2 a0
c7 00a3 b0
c7 00a4 c0
c7 00a5 d0
c7 00a6 e0
c7 00a7 f0
c7 00a8 00
c7 00a9 10
c7 00aa 20
c7 00ab 30
c7 00ac 40
c7 00ad 50
c7 00ae 60
c7 00af 70
c7 00b0 7f
c7 00b1 7f
c7 00b2 7f
c7 00b3 7f
c7 00b4 7f
c7 00b5 7f
c7 00b6 7f
c7 00b7 7f
c7 00b8 7f
c7 00b9 7f
c7 00ba 7f
c7 00bb 7f
c7 00bc 7f
c7 00bd 40
c7 00be 00
c7 00bf c0

# try a few speeds
c7 0142 00
c7 0143 01
c7 0146 00
c7 0145 00
c7 0147 f0
c7 0140 80
61 ac44
c7 0145 70
61 cc44
# attempt a reset
c7 0140 80
61 ac44
c7 0147 90
61 ac44
c7 0147 70
61 ac44
c7 0147 10
61 ac44
c7 0147 80
61 ac44
c7 0140 00
61 ac44

# move pitch, triggering the byte locking bug
c7 0147 90
c7 0142 00
c7 0143 01
c7 0140 80
61 5622
c7 0143 05
61 5622
c7 0142 00
61 5622
c7 0000 00
61 5622
c7 0142 ff
61 5622
c7 0142 80
61 5622
c7 01ff 00
61 5622
c7 0140 00
61 5622

# try without looping, see what resets it
c7 0142 00
c7 0143 05
c7 0147 00
c7 0140 80
61 5622
c7 0147 70
c7 0145 50
61 5622
c7 0140 80
61 5622
c7 0145 50
61 5622
c7 0147 70
61 5622
c7 0142 00
61 5622
c7 0143 05
61 5622
c7 0140 00
61 ac44

# loop then unloop then loop
c7 0145 70
c7 0140 80
61 5622
# change pitch so we know the unloop bit started
c7 0142 ff
c7 0145 50
61 5622
c7 0145 70
61 5622
c7 0140 00
61 5622

# loop but very quickly unloop, the cycle should finish
c7 0140 80
63
c7 0145 50
61 5622
c7 0140 00
61 5622

# don't modulate then unloop
c7 0145 00
c7 0140 80
61 5622
c7 0145 50
61 5622
c7 0140 00
61 ac44

# halt modulation, then unloop, then try to sweep
c7 0145 50
c7 0147 00
c7 0140 80
61 5622
c7 0147 70
61 5622
c7 0145 00
61 5622
c7 0145 50
61 5622
c7 0140 00
61 ac44

# unloop then fadeout
c7 0140 80
61 5622
c7 0145 51
61 ac44

# fadeout then unloop
c7 0144 80
c7 0145 01
c7 0140 80
61 5622
c7 0144 f0
c7 0145 51
61 5622
c7 0140 00
61 5622

# spam registers
c7 0142 ff
c7 0145 04
c7 0146 00
c7 0145 70
c7 0147 90
repeat 25
    c7 0140 80
    63
done
c7 0140 00
61 5622

c7 0140 80
repeat 25
    c7 0142 ff
    63
done
c7 0140 00
61 5622

c7 0140 80
repeat 25
    c7 0143 04
    63
done
c7 0140 00
61 5622

c7 0140 80
repeat 25
    c7 0144 f0
    63
done
c7 0140 00
61 5622

c7 0140 80
repeat 25
    c7 0145 70
    63
done
c7 0140 00
61 5622

c7 0140 80
repeat 25
    c7 0147 90
    63
done
c7 0140 00
61 ac44

# modulation then sweep then modulation
c7 0147 95
c7 0140 80
61 5622
c7 0145 50
61 5622
c7 0145 70
61 5622
c7 0140 00
61 5622

# moduation/sweep combinations
c7 0145 40
c7 0140 80
61 5622
c7 0145 70
61 5622
c7 0145 40
61 5622
c7 0140 80
61 5622
c7 0145 70
61 5622
c7 0145 40
61 5622
c7 0140 80
61 5622
c7 0145 50
61 5622
c7 0145 40
61 5622
c7 0145 50
61 5622
c7 0140 00
61 5622

# modulate then quickly sweep
c7 0145 70
c7 0147 95
c7 0140 80
63
c7 0145 40
61 5622
c7 0140 00
61 5622

# sweep then quickly unlooped modulate
c7 0145 40
c7 0140 80
63
c7 0145 50
61 5622
c7 0140 00
61 ac44

# write modulation data while channel 5 is active
c7 0145 50
c7 0140 80
61 5622
c7 00a0 00
c7 00a1 00
c7 00a2 00
c7 00a3 00
c7 00a4 00
c7 00a5 00
c7 00a6 00
c7 00a7 00
c7 00a8 00
c7 00a9 00
c7 00aa 00
c7 00ab 00
c7 00ac 00
c7 00ad 00
c7 00ae 00
c7 00af 00
c7 0145 00
c7 00b0 00
c7 00b1 00
c7 00b2 00
c7 00b3 00
c7 00b4 00
c7 00b5 00
c7 00b6 00
c7 00b7 00
c7 00b8 00
c7 00b9 00
c7 00ba 00
c7 00bb 00
c7 00bc 00
c7 00bd 00
c7 00be 00
c7 00bf 00
61 5d22
c7 0140 00
61 5d22
c7 0145 50
c7 0140 80
61 5d22
c7 0140 00
61 ac44

# noise
# start with different noise types
c7 0151 ff
c7 0152 00
c7 0153 06
c7 0154 f0
c7 0155 00
c7 0150 80
61 5622
c7 0150 00
61 5622

c7 0150 80
c7 0155 10
61 5622
c7 0150 00
61 5622

c7 0150 80
c7 0155 20
61 5622
c7 0150 00
61 5622

c7 0150 80
c7 0155 30
61 5622
c7 0150 00
61 5622

c7 0150 80
c7 0155 40
61 5622
c7 0150 00
61 5622

c7 0150 80
c7 0155 50
61 5622
c7 0150 00
61 5622

c7 0150 80
c7 0155 60
61 5622
c7 0150 00
61 5622

c7 0150 80
c7 0155 70
61 5622
c7 0150 00
61 ac44

# different frequency
c7 0152 80
c7 0153 04
c7 0150 80
61 5622
c7 0150 00
61 5622

c7 0150 80
c7 0155 60
61 5622
c7 0150 00
61 5622

c7 0150 80
c7 0155 50
61 5622
c7 0150 00
61 5622

c7 0150 80
c7 0155 40
61 5622
c7 0150 00
61 5622

c7 0150 80
c7 0155 30
61 5622
c7 0150 00
61 5622

c7 0150 80
c7 0155 20
61 5622
c7 0150 00
61 5622

c7 0150 80
c7 0155 10
61 5622
c7 0150 00
61 5622

c7 0150 80
c7 0155 00
61 5622
c7 0150 00
61 ac44

# try max and min frequency
c7 0152 00
c7 0153 00
c7 0150 80
61 5622
c7 0152 ff
c7 0153 ff
61 5622
c7 0150 00
61 5622 00

# try spamming registers
c7 0155 00
c7 0152 00
c7 0153 04

c7 0150 80
61 5622
c7 0150 00
61 5622

repeat 25
    c7 0150 80
    63
done
c7 0150 00
61 5622

c7 0150 80
repeat 25
    c7 0151 ff
    63
done
c7 0150 00
61 5622

c7 0150 80
repeat 25
    c7 0152 00
    63
done
c7 0150 00
61 5622

c7 0150 80
repeat 25
    c7 0153 04
    63
done
c7 0150 00
61 5622

c7 0150 80
repeat 25
    c7 0154 f0
    63
done
c7 0150 00
61 5622

c7 0150 80
repeat 25
    c7 0155 00
    63
done
c7 0150 00
61 5622

66
"""

stream = iter(map(str.split, map(str.strip, commands.splitlines())))
total_samples = 0
def parse():
    global total_samples
    dat = b''
    for cmd in stream:
        if not cmd or cmd[0].startswith("#"): continue
        if cmd[0] == 'repeat':
            dat += parse() * int(cmd[1])
        elif cmd[0] == "done":
            break
        elif cmd[0] == 'c7':
            dat += b'\xc7' + int(cmd[1], 16).to_bytes(2, 'big') + bytes([int(cmd[2], 16)])
        elif cmd[0] == '61':
            s = int(cmd[1], 16)
            total_samples += s
            dat += b'\x61' + s.to_bytes(2, 'little')
        else:
            if cmd[0] == '62':
                total_samples += 735
            elif cmd[0] == '63':
                total_samples += 882
            dat += bytes([int(cmd[0], 16)])
    return dat
vgmdat = parse()

gd3 = b''
gd3 += ('VSU Test'.encode('utf-16') + b'\0\0') * 2
gd3 += b'\0\0' * 2
gd3 += ('Virtual Boy'.encode('utf-16') + b'\0\0') * 2
gd3 += ('Floogle'.encode('utf-16') + b'\0\0') * 2
gd3 += '2025/02/15'.encode('utf-16') + b'\0\0'
gd3 += 'Floogle'.encode('utf-16') + b'\0\0'
gd3 += 'A stress test for VSU emulators.'.encode('utf-16') + b'\0\0'

with open("vsutest.vgm", "wb") as f:
    f.write(b'Vgm ')
    f.write((0xc8 + len(vgmdat) + len(gd3) + 12 - 4).to_bytes(4, 'little'))
    f.write(b'\x71\x01\0\0\0\0\0\0\0\0\0\0')
    f.write((0xc8 + len(vgmdat) - 0x14).to_bytes(4, 'little'))
    f.write(total_samples.to_bytes(4, 'little'))
    f.write(b'\0\0\0\0' * 6)
    f.write(b'\x94\0\0\0')
    f.write(b'\0' * (0x8c))
    f.write(b'\x40\x4b\x4c\x00')
    f.write(vgmdat)
    f.write(b'Gd3 \0\x01\0\0')
    f.write(len(gd3).to_bytes(4, 'little'))
    f.write(gd3)
