# Test Driven Design

We need a password generator which generates one time password.

The password is for children between the age 6-10 years and hence need to be simple.

The rules of pswd generator to make it simple are
1. The password should be 6 characters in length
1. Should be only alphabets, not include special characters or numbers
1. The password should start with the first letter of the given child's name
1. The password should have combination of 2 words, each of length 3, two words should not be same
1. If the childs name starts with a consonant, the password would be (consonant-vowel-consonent)(consonant-vowel-consonent)
1. If the childs name starts with a vowel, the password would be (vowel-vowel/consonant-vowel/consonant)(consonant-vowel-consonent)
1. 2 consecutive consonants should not be same
1. The password should be in pascal casing for the 2 words joined to make the password
1. The password generated should not be repeated for atleast 100 times or within a week which ever comes first


> **DO NOT** jump into implementation! Read the example and the starting task below.

## Example
### Input

Childs First name

### Functionality

An auto generated 6 letter password that adheres to set of rule

### Example output for every Rules 
Let us consider examples for child name: Nathan and Annie

| No | Rule  | Example | Error Example |
| :--|:----------------------| :-----|:-----|
| 1 | The password should be 6 characters in length | CanMin | CanNotDoThis |
| 2 | The password should have combination of 2 words, each of length 3, two words should not be same | GudFud | GudGud |
| 3 | The password should be only alphabets, not include special characters or numbers | PinTim | Car2#D |
| 4 | The password should start with the first letter of the given child's name |  -- | -- | 
| 5 | If the childs name starts with a consonant, the password would be (consonant-vowel-consonent)(consonant-vowel-consonent) | NetPut, NodFor, NewBuk | NdaFee| 
| 6 | If the childs name starts with a vowel, the password would be (vowel-vowel/consonant-vowel/consonant)(consonant-vowel-consonent) |AntMan, AteMud, AxeLan | AerAir| 
| 7 | 2 consecutive consonants should not be same | See above |NetTuk, AndDad | 
| 8 | The password should be in pascal casing | See above | pasNot, rongon,Notsoo | 
| 9 | The password generated should not be repeated for atleast 100 times or within a week which ever comes first | -- | -- | 

## Tasks

Establish quality parameters: 
- What is the maximum complexity (CCN) per function? _enter CCN and create corresponding yml in the `.github/workflows` folder
- How many lines of duplicate code will you tolerate? _enter the number of lines and create corresponding yml in the `.github/workflows` folder
- Ensure 100% line and branch coverage at every step. Include the coverage yml in the workflows.

Adapt/adopt/extend the `yml` files from one of your previous workflow folders.

Start Test-driven approach
Stage 1:
1. Write the smallest possible failing test: give input `any name`. assert output to be `the pswd starts with first letter of the name`.
1. Write the minimum amount of code that'll make it pass.
1. Refactor any assumptions, continue to pass this test. Do not add any code without a corresponding test.

Stage 2:
1. Write the next failing test: give input `any name`. assert output to pass stage1 and to be `6 letter password`.
1. Write the minimum amount of code that'll make it pass.
1. Refactor any assumptions, continue to pass this test. Do not add any code without a corresponding test.

Stage 3:
1. Write the next failing test: give input `any name`. assert output to pass previous stages and to be `in pascal case`.
1. Write the minimum amount of code that'll make it pass.
1. Refactor any assumptions, continue to pass this test. Do not add any code without a corresponding test.

Similarly, the test and development can be extended to rest of the rules in the password generator requirement.
