# Test Driven Design
## Programming Paradigms

Health Monitoring Systems

[Here is an article that helps to understand the Adult Vital Signs](https://en.wikipedia.org/wiki/Vital_signs)

[Here is a reference to Medical monitoring](https://en.wikipedia.org/wiki/Monitoring_(medicine))

## Purpose
Monitoring of vitals and the combination of vitals being out of range can give early indication of an impending health issue
Following is the table describing the vitals and and their ranges 

| Vitals | Low  | Normal | Moderate | High |
| :-- |:------- | :----- |:----- |:------|
| Heart Rate (HR) | < 40 | 60 - 100 | 40-60 or 100-120 | > 120|
| Respiratory Rate (RR) | < 10 | 12 - 20 | 10-12 or 20-30 | > 30 |
| Peripheral Oxygen Saturation (SpO2) | < 92 | 98-100 | 92-98 | - |
| Temperature (Temp) | < 95 C | 97 C - 99 C | 95 C - 97 C | > 104 C |
|  |  |  | or 99 C - 102 C | |


The combinations of vitals in different ranges could give indication of underlying issue
|No |HR           |RR           |SPO2|Temp         |Indication                                                               |Criticality|Underlying issue                                                                             |
|---|-------------|-------------|----|-------------|-------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------|
|1  |Moderate     |-            |-   |Moderate     |Fever, systemic infection                                                |Medium     |Indicates a possible infection, further assessment needed                                    |
|2  |-            |Moderate     |Low |-            |Respiratory distress, possible lung or heart issues                      |High       | Indicates compromised oxygenation, immediate attention required                             |
|3  |Moderate     |Moderate     |-   |-            | Physical stress, anxiety, or pain                                       |Low        |Could be due to various factors, monitoring may be needed                                    |
|4  |-            |-            |Low |Moderate     |Severe infection or respiratory compromise                               |High       | Indicates potentially serious condition, urgent medical attention necessary                 |
|5  |Moderate     |-            |Low |-            | Cardiovascular or respiratory issue affecting oxygen delivery           |Medium     |Requires investigation, potential need for intervention                                      |
|6  |Moderate/High|Moderate/High|-   |Moderate/High|Significant stress on the body, potential infection                      |Medium/High|Suggests systemic response, medical evaluation advised                                       |
|7  |-            |Moderate     |Low |High         |Acute respiratory distress and possible infection                        |High       | Indicates serious respiratory compromise, urgent medical attention needed                   |
|8  |Moderate     |Moderate     |Low |-            |Severe respiratory distress, compromised oxygenation, and physical stress|High       | Indicates serious respiratory and cardiovascular compromise, urgent medical attention needed|
|9  |Moderate/High|Moderate/High|Low |Moderate/High|Systemic stress, possible infection, and compromised oxygenation         |High       | Suggests a combination of serious factors, urgent medical attention necessary               |



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

