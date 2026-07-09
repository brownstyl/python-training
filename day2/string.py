
def small_letter(input: str) -> str:
    conv = bytearray(input.encode('ascii'))
    for i in range(len(conv)):
        if 65 <= conv[i] <= 90:
            conv[i] += 32
    return conv.decode('ascii')

print(small_letter("HELLO WORLD"))

#===============string maipulation================#
def cap(input: str) -> str:
    data = open(input, "r")
    try:
        data = open(input, "r")
    except:
        print("file does not exist")
        return ""

    info = data.read()
    data.close()


    join = info

    byte_convo = info.split()
    for i in range(len(byte_convo)):
        if byte_convo[i] == "(low)":
            byte_convo[i-1] = byte_convo[i-1].upper()
            byte_convo[i] = ""
            final = []
            for word in byte_convo:
                if word != "":
                 final.append(word)

            join = " ".join(final)

    writeout = open("result.txt", "w")
    writeout.write(join)
    writeout.close()
    
    return join


print(cap("files.txt"))