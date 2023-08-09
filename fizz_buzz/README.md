# Test Driven Design

The requirement is to create a program that given a series of numbers outputs an encoded string using fizzbuzz technique

>### **DO NOT** jump into implementation! Read the example and the starting task below.

## Example

### Input
23 5 4 9 23 89 32 15 101 

### Functionality

The task is to encode the number series using the fizzbuzz technique.
Given a number series 
- replace any occurance of multiple of 3 with the word FIZZ
- replace any occurance of multiple of 5 with the word BUZZ
- replace any occurance of multiple of 3 and 5 with the word FIZZBUZZ

### Output

For example,
```
Series : 23 5 4 9 23 89 32 15 101
Encoded: 23 BUZZ 4 FIZZ 23 89 32 FIZZBUZZ 101
```
## Tasks

Establish quality parameters: 

- What is the maximum complexity (CCN) per function? _enter CCN and create corresponding yml in the `.github/workflows` folder
- How many lines of duplicate code will you tolerate? _enter the number of lines and create corresponding yml in the `.github/workflows` folder
- Ensure 100% line and branch coverage at every step. Include the coverage yml in the workflows.

Adapt/adopt/extend the `yml` files from one of your previous workflow folders.

Start Test-driven approach

1. Write the smallest possible failing test: give input `3 5 15`. assert output to be `FIZZ BUZZ FIZZBUZZ`. 
1. Write the minimum amount of code that'll make it pass.
1. Test with different input number series
1. Refactor any assumptions, continue to pass this test. Do not add any code without a corresponding test.

