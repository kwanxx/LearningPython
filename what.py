# I don't know writing what in github.
# Python markdown

# input a number ,find a month
def main():
    pos = int(input("input a number:"))
    s = 'JanFebMarAprMayJunJulAugSepOctNovDec'
    print(s[3*(pos-1) : 3 * (pos-1)+3])
main()
