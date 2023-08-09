# Test Driven Design
From Wikipedia: In cryptography, a [substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher) is a method of encrypting in which units of plaintext are replaced with the ciphertext, in a defined manner, with the help of a key. The "units" may be single letters (the most common), pairs of letters, triplets of letters, mixtures of the above, and so forth. 

The requirement is to create a program to cipher and decipher a given text using an over simplified algorithm as explained below

Cipher:
- Replace each occurance of the vowels with their corresponding symbol below
- Ensure the input text does not contain any symbol used in cipher

Decipher
- Replace each occurance of the symbol with the corresponding vowel

Note: The casing of input text is not of importance. The deciphered text would always be in small case.
```
A/a = @
E/e = *
I/i = #
O/o = %
U/u = +
```

>### **DO NOT** jump into implementation! Read the example and the starting task below.

## Example

### Input
A sample text.

### Functionality

The task is to encode and decode the text using the algorithm mentioned above.
Make sure the output of decoding is same as the original input text.
Make sure the punctuations (if any) in the input text is retained after decoding back to original text.
Note that the decoded text would always be in small case.

### Output

For example,

| Ex | Input  | Ciphered text | Deciphered text |
| :-- |:------- | :----- |:----- |
| 1 | Quick frozen fox jumps over lazy dog | `q+#ck fr%z*n f%x j+mps %v*r l@zy d%g` | quick frozen fox jumps over lazy dog|
| 2 | PREPARE TO MEET | `pr*p@r* t% m**t` | prepare to meet |
| 3 | where is it the pigs live? | `*wh*r* #s #t th* p#gs l#v*?` | where is it the pigs live? |

## Tasks

Establish quality parameters: 

- What is the maximum complexity (CCN) per function? _enter CCN and create corresponding yml in the `.github/workflows` folder
- How many lines of duplicate code will you tolerate? _enter the number of lines and create corresponding yml in the `.github/workflows` folder
- Ensure 100% line and branch coverage at every step. Include the coverage yml in the workflows.

Adapt/adopt/extend the `yml` files from one of your previous workflow folders.

Start Test-driven approach

1. Write the smallest possible failing test: give input `always act artfact`. assert output to be `@lw@ys @ct @rtf@ct`. 
1. Write the minimum amount of code that'll make it pass.
1. Test with different input texts
1. Refactor any assumptions, continue to pass this test. Do not add any code without a corresponding test.

Repeat the above set of tasks to all conditions in the algorithm

