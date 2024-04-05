import wave
song = wave.open("song_embedded.wav", mode='rb')

frame_bytes = bytearray(list(song.readframes(song.getnframes())))


extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
decoded = string.split("###")[0]

#extracted = [frame_bytes[j] & 1 for i in range(len(frame_bytes))]no
#string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
#decoded = string.split("###")[0]


#extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
#string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
#decoded = string.split("###")[]no


#extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
#string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
#decoded = string("###")[0]no



print("Sucessfully decoded: "+decoded)
song.close()
