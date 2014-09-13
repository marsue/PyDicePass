# Licenced under WTFPL

chars = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.',
         '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<',
         '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
         'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f',
         'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'k', 'y', 'z', '{', '|', '}', '~']

c = 0

for i in chars+chars:
    for j in chars+chars:
        e = []
        c, d = c+1, c+1
        for b in range(6):
            d, r = divmod(d, 6)
            e.append(r+1)
        e.reverse()
        print(str(e)+"  -  "+i+j)
