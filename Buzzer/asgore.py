import time

# notes
NULL=1
B0=31
C1=33
CS1=35
D1=37
DS1=39
E1=41
F1=44
FS1=46
G1=49
GS1=52
A1=55
AS1=58
B1=62
C2=65
CS2=69
D2=73
DS2=78
E2=82
F2=87
FS2=93
G2=98
GS2=104
A2=110
AS2=117
B2=123
C3=131
CS3=139
D3=147
DS3=156
E3=165
F3=175
FS3=185
G3=196
GS3=208
A3=220
AS3=233
B3=247
C4=262
CS4=277
D4=294
DS4=311
E4=330
F4=349
FS4=370
G4=392
GS4=415
A4=440
AS4=466
B4=494
C5=523
CS5=554
D5=587
DS5=622
E5=659
F5=698
FS5=740
G5=784
GS5=831
A5=880
AS5=932
B5=988
C6=1047
CS6=1109
D6=1175
DS6=1245
E6=1319
F6=1397
FS6=1480
G6=1568
GS6=1661
A6=1760
AS6=1865
B6=1976
C7=2093
CS7=2217
D7=2349
DS7=2489
E7=2637
F7=2794
FS7=2960
G7=3136
GS7=3322
A7=3520
AS7=3729
B7=3951
C8=4186
CS8=4435
D8=4699
DS8=4978

def play(Buzz):
    
    song = [
        E4, GS4, FS4, DS4, FS4, E4, CS4, E4, DS4, B3, C4, GS3, E4, GS4, FS4, B4, FS4, GS4, GS4, FS4, GS4, B4, CS5, E5, DS5, E5, DS5, CS5, B4, DS5, CS5,

        E4, GS4, FS4, GS4, CS4, DS4, E4, GS4, E4, GS4, FS4, GS4, CS4, DS4, B4, GS4, CS5, GS4, DS5, A4, FS5, CS5, E4, FS4, E5, DS5, CS5, DS4, DS5, B4, CS5, A4, GS4, FS4, NULL, 

        E4, E4, DS4, DS4,
        CS4, E4, DS4, E4, CS4, CS4, DS4, E4, B4, GS4, NULL,
        CS4, E4, DS4, E4, CS4, CS4, DS4, E4, B4, GS4, NULL,
        CS4, E4, DS4, E4, CS4, CS4, DS4, E4, B4, GS4, NULL,
        B3, FS4, E4, CS4, DS4, CS4, B3, DS4,

        CS5, E5, DS5, E5, CS5, CS5, DS5, E5, B5, GS5, NULL,
        CS5, E5, DS5, E5, CS5, CS5, DS5, E5, B5, GS5, NULL,
        CS5, E5, DS5, E5, CS5, CS5, DS5, E5, B5, GS5, NULL,
        B4, FS5, E5, CS5, DS5, CS5, B4, DS5,

        CS5, E5, DS5, E5, CS5, CS5, DS5, E5, B5, GS5, NULL,
        CS5, E5, DS5, E5, CS5, CS5, DS5, E5, B5, GS5, NULL,
        CS5, E5, DS5, E5, CS5, CS5, DS5, E5, B5, GS5, NULL,
        C5, FS5, E5, CS5, DS5, CS5, C5, DS5,

        CS5, GS4, B4, CS5, E5, FS5, E5, CS5, DS5, E5,
        CS5, GS4, GS4, B4, B4, E5, DS5, CS5, E5, FS5,
        GS5, NULL, FS5, GS5, E6, B5, FS5,
        GS5, E5, FS5, DS5, B4,
        CS5, NULL, FS5, GS5, E6, B5, FS5,
        GS5, FS5, E5, FS5, DS5, A5, AS5, B5,
        GS5, NULL, FS5, GS5, E6, B5, FS5,
        GS5, E5, FS5, DS5, B4,
        CS5, NULL, FS5, GS5, E6, B5, FS5,
        DS5, DS6, CS6, B5, CS6, D6, DS6,
        E6, DS6, CS6, B5, CS6, GS5, AS5, FS5, CS5, DS5,
        E5, FS5, CS5, B5, GS5,

        E6, DS6, CS6, B5, CS6, GS5, AS5, FS5, CS5, DS5,
        E5, DS5, GS4, DS5, CS5,
        E6, DS6, CS6, B5, CS6, GS5, AS5, FS5, CS5, DS5,
        E5, FS5, CS5, B5, GS5,
        E6, DS6, CS6, B5, CS6, GS5, AS5, FS5, CS5, DS5,
        E5, DS5, GS4, DS5, CS5,
        FS5, E5, E5, CS5, DS5, CS5, B4, DS5, CS5, GS4, GS4, CS5,
        FS5, E5, E5, CS5, B4, A4, GS5, FS5, E5, FS5, GS5, AS5,
        B5, AS5, GS5, FS5, GS5, FS5, GS5, AS5, GS5, CS5, CS5, DS5,
        E5, FS5, A5, GS5, DS5, C5, GS4,
        FS5, E5, E5, CS5, DS5, CS5, B4, DS5, CS5, GS4, GS4, CS5,
        FS5, E5, E5, CS5, B4, A4, GS5, FS5, E5, FS5, GS5, AS5,
        B5, AS5, GS5, FS5, GS5, FS5, GS5, AS5, GS5, CS5, CS5, DS5,
        E5, DS5, B4, CS5, CS5, DS5,
        E5, DS5, B4, CS5, CS5, DS5,
        E5, DS5, B4, CS5, CS5, DS5,
        E5, DS5, B4, CS5, B5, CS6,
    
    ]

    beat = [
        16, 16, 32, 16, 16, 32, 16, 16, 32, 16, 16, 32, 16, 16, 32, 16, 16, 32, 8, 8, 8, 8, 16, 16, 8, 2, 2, 8, 8, 8, 16,

        16, 16, 24, 8, 12, 12, 8, 32, 16, 16, 24, 8, 12, 12, 8, 32, 8, 8, 8, 8, 24, 8, 12, 12, 8, 24, 8, 12, 12, 8, 56, 4, 4, 16, 16,

        8, 8, 8, 8,
        4, 4, 4, 4, 12, 8, 4, 4, 4, 8, 4,
        4, 4, 4, 4, 12, 8, 4, 4, 4, 8, 4,
        4, 4, 4, 4, 12, 8, 4, 4, 4, 8, 4,
        12, 12, 8, 2, 4, 8, 12, 8,

        4, 4, 4, 4, 12, 8, 4, 4, 4, 8, 4,
        4, 4, 4, 4, 12, 8, 4, 4, 4, 8, 4,
        4, 4, 4, 4, 12, 8, 4, 4, 4, 8, 4,
        12, 12, 8, 2, 4, 8, 12, 8,

        4, 4, 4, 4, 12, 8, 4, 4, 4, 8, 4,
        4, 4, 4, 4, 12, 8, 4, 4, 4, 8, 4,
        4, 4, 4, 4, 12, 8, 4, 4, 4, 8, 4,
        12, 12, 8, 2, 4, 8, 12, 8,

        48, 8, 8, 24, 8, 4, 8, 2, 12, 8,
        32, 8, 4, 8, 4, 8, 32, 12, 12, 8,
        32, 4, 4, 4, 4, 8, 8,
        32, 8, 6, 12, 8,
        32, 4, 4, 4, 4, 8, 8,
        24, 8, 8, 4, 8, 2, 2, 8,
        32, 4, 4, 4, 4, 8, 8,
        32, 8, 6, 12, 8,
        32, 4, 4, 4, 4, 8, 8,
        32, 4, 8, 8, 2, 2, 8,
        4, 4, 4, 4, 8, 8, 12, 12, 4, 4,
        12, 8, 4, 8, 32,

        4, 4, 4, 4, 8, 8, 12, 12, 4, 4,
        12, 8, 4, 8, 32,
        4, 4, 4, 4, 8, 8, 12, 12, 4, 4,
        12, 8, 4, 8, 32,
        4, 4, 4, 4, 8, 8, 12, 12, 4, 4,
        12, 8, 4, 8, 32,
        4, 4, 4, 4, 4, 4, 4, 4, 12, 12, 4, 4,
        4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 12, 4,
        4, 4, 4, 4, 4, 4, 4, 4, 12, 12, 4, 4,
        12, 12, 8, 8, 8, 8, 8,
        4, 4, 4, 4, 4, 4, 4, 4, 12, 12, 4, 4,
        4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 12, 4,
        4, 4, 4, 4, 4, 4, 4, 4, 12, 12, 4, 4,
        12, 12, 8, 24, 4, 4,
        12, 12, 8, 24, 4, 4,
        12, 12, 8, 24, 4, 4,
        12, 12, 8, 24, 8, 64,

    ]

    for i in range(0, len(song)):
        note = [ k for k,v in globals().items() if v == song[i]][0]
        print(note, "<>", song[i], "Hz" , "-:-", beat[i])
        Buzz.ChangeFrequency(song[i]) 
        time.sleep(beat[i]*0.035) 