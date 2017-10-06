For building the encrypted string:
Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
Do this n times!

Examples:

`"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"`

Write two methods:

`def encrypt(text, n)
def decrypt(encrypted_text, n)`

For both methods:

If the input-string is null or empty return exactly this value!
If n is <= 0 then return the input text.

This kata is part of the Simple Encryption Series:
[Simple Encryption #1 - Alternating Split](https://www.codewars.com/kata/simple-encryption-number-1-alternating-split)
[Simple Encryption #2 - Index-Difference](https://www.codewars.com/kata/simple-encryption-number-2-index-difference)
[Simple Encryption #3 - Turn The Bits Around](https://www.codewars.com/kata/simple-encryption-number-3-turn-the-bits-around)
[Simple Encryption #4 - Qwerty](https://www.codewars.com/kata/simple-encryption-number-4-qwerty)

[Source](https://www.codewars.com/kata/57814d79a56c88e3e0000786)
