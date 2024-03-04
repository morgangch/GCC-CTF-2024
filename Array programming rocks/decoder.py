


# The values in chall.ua may be encoded in their ASCII values.
# Meanwhile, the challenge is named "Array programming rocks", so it may be related to array programming.
# ≍ 5_1_1_57_115_29_15_115_53_113_29_23_43_115_119_29_49_23_119_33_41_29_33_35_119_39_7_29_15_119_39_13_113_119_119_63
# What can it be?
# Let's try to convert the numbers to ASCII values and see if we can find anything interesting.
the_challua_file = """
F ← -@\0 &sc
N ← ⧻F
[⍥(⍉↻1⍉.)] N . F
∵(⇌⬚0↙8⋯)
⍥(◿2+) N /∘
ⁿ↯N⇡8⍉⇌⍉×2
/+⍉
≍ 5_1_1_57_115_29_15_115_53_113_29_23_43_115_119_29_49_23_119_33_41_29_33_35_119_39_7_29_15_119_39_13_113_119_119_63
⍤"Sorry this wasn't the flag 😔"
:/+⍉◫7:/+↯9_4.⇌
≍ 844_662_647_745
⍤"So close but yet it's not the flag 😔"
≍ 512_464_506_521_571_546_543_589_607_619_650_601_632_650_647_605_547_552_584_595_531_554_549_576_567_532_560_576_525_548
⍤"You're soooo close 😔"
"Well done ! 🥳🚩"
"""
# The numbers are separated by underscores, so we can split the string by the underscores and convert the numbers to their ASCII values.
# Then, we can convert the ASCII values to their characters and see if we can find anything interesting.
# The following code does that.
# The flag the code finds is : qww?͌ʖʇ˩ȀǐǺȉȻȢȟɍɟɫʊəɸʊʇɝȣȨɈɓȓȪȥɀȷȔȰɀȍȤ. But it's not the flag.
# So, we need to find a different way to decode the numbers.
# The numbers are not encoded in their ASCII values.
# What else can I try ? Base64 ? Hexadecimal ? Binary ?
# Let's try to convert the numbers to their binary values and see if we can find anything interesting.

if __name__ == "__main__":
    flag = ""
    with (open("chall.ua", 'r')) as data_file:
        data = data_file.readlines()
        for line in data:
            if line.startswith("≍"):
                for number in line.split("≍").pop().split("_"):
                    flag += bin(int(number))[2:]

    print(f"Flag : {flag}. Decimal : {int(flag, 2)}")