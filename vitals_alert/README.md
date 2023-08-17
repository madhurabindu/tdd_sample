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
|10 |High/Low     |-            |-  |-            |potential cardiovascular issues                                          |High       |potential cardiovascular issues, such as arrhythmias, heart failure, or shock              |
|11 |-            |High/Low     |-  |-            | severe respiratory distress                                             |High       | lung infections, pneumonia, or respiratory failure                                          |
|12 |-            |-            |Low|-            |inadequate oxygenation of the blood                                      |High       |lung or heart problems                                                                       |
|13 |-            |-            |-  |High/Low     |Severe systemic issue                                                    |High       |severe infections, heatstroke, hypothermia, or other serious underlying medical conditions. |

Requirement is to develop a alerting system that given a vitals for a patient would give the indication and possible underlying issue.


>### **DO NOT** jump into implementation! Read the example and the starting task below.


### Input
Vitals for a patient and the patients PatientId 

### Functionality

The task is to assess the different vitals and their ranges to determine the underlying issue

### Output

The output should contain the following
```
PatientId
Indication
Assessment (Possible underlying issue)
Criticality (Low, Medium, High)
```

For example,
Input  
```
PatientID: 12485
HR: 100
RR: 30
SPO2: 90
Temp: 102
```
Should return
The input patientid received along with indications, criticality and underlying issue from row 9 of the table above.

## Tasks

Establish quality parameters: 

- What is the maximum complexity (CCN) per function? _enter CCN and create corresponding yml in the `.github/workflows` folder
- How many lines of duplicate code will you tolerate? _enter the number of lines and create corresponding yml in the `.github/workflows` folder
- Ensure 100% line and branch coverage at every step. Include the coverage yml in the workflows.

Adapt/adopt/extend the `yml` files from one of your previous workflow folders.

Start Test-driven approach
Step 1:
1. Write the smallest possible failing test to assert the input PatientID is returned in output.
1. Write the minimum amount of code that'll make it pass.
1. Test with different input texts
1. Refactor any assumptions, continue to pass this test. Do not add any code without a corresponding test.

Step 2:
1. Write the smallest possible failing test: give input `SPO2: 90`. assert criticality to  be `High`. 
1. Write the minimum amount of code that'll make it pass.
1. Test with different input texts
1. Refactor any assumptions, continue to pass this test. Do not add any code without a corresponding test.

Step 3: 
1. Write the smallest possible failing test: give input `SPO2: 90`. assert indication to be `inadequate oxygenation of the blood`. 
1. Write the minimum amount of code that'll make it pass.
1. Test with different input texts
1. Refactor any assumptions, continue to pass this test. Do not add any code without a corresponding test.

Step 4: 
1. Write the smallest possible failing test: give input `SPO2: 90`. assert assessment to be `severe infections, heatstroke, hypothermia, or other serious underlying medical conditions.`. 
1. Write the minimum amount of code that'll make it pass.
1. Test with different input texts
1. Refactor any assumptions, continue to pass this test. Do not add any code without a corresponding test.
 
Repeat the above set of tasks to all data in the table above.

