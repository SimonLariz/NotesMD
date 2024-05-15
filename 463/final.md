## Final Exam Notes
- Closed book 
- Code path based
- Specification based

## Chapter 3 Specification-Based, Unit, Boundary Value Testing
Reliability theory: 
    - Failures are rarely the result of the simultaneous failure of multiple components.

Four forms of boundary value testing:
    - *Normal boundary value testing*: Test cases are designed to test the normal operation of the software.
        - Example: If the software is designed to accept a number between 1 and 100, then the test cases would be 1, 2, 99, 100.
        
    - *Robust normal boundary value testing*: Test cases are designed to test the software's ability to handle abnormal input.
        - Example: If the software is designed to accept a number between 1 and 100, then the test cases would be 0, 101.
        
    - *Worst-case boundary value testing*: Test cases are designed to test the software's ability to handle the worst possible input.
        - Example: If the software is designed to accept a number between 1 and 100, then the test cases would be -1, 0, 50, 100, 101.
        
    - *Robust worst-case value testing*: Test cases are designed to test the software's ability to handle the worst possible abnormal input.
        - Test all values around the boundary values.

## Chapter 4 Specification-Based, Unit, Equivalence Class Testing
Single Fault Normal Equivalence Testing:
    - Test cases are designed to test the software's ability to handle a single fault.
    - Example: If the software is designed to accept a number between 1 and 100, then the test cases would be 1, 2, 99, 100, 101.

Multiple Fault Normal Equivalence Testing:
    - Test cases are designed to test the software's ability to handle multiple faults.
    - Example: If the software is designed to accept a number between 1 and 100, then the test cases would be 1, 2, 99, 100, 101.

## Chapter 6 Code-Based, Unit Path Testing (Or, Structure-Based, Unit, Control Flow Testing)
Program Graph:
    - A program graph is a directed graph that represents the control flow of a program.
    - The nodes of the graph represent the statements in the program.
    - The edges of the graph represent the control flow between the statements.

Segment Graph:
    - A segment graph is a directed graph that represents the control flow of a program more abstractly than a program graph.
    - The nodes of the graph represent the segments of the program.
    - The edges of the graph represent the control flow between the segments.

Decision Graph:
    - A decision graph is a directed graph that represents the control flow of a program more abstractly than a segment graph.
    - The nodes of the graph represent the decisions in the program.
    - The edges of the graph represent the control flow between the decisions.

## Chapter 7 Code-Based Data Flow Testing
Code-Based Data Flow Testing:
    - Code-based data flow testing is a testing technique that is used to test the data flow of a program.
    - The goal of code-based data flow testing is to test the data flow of a program to ensure that the program is functioning correctly.

Define/ Use Testing:
    - Define/use testing is a testing technique that is used to test the data flow of a program.
    - The goal of define/use testing is to test the data flow of a program to ensure that the program is functioning correctly.
    - Notate the variables that are defined and used in the program.

Slice-Based Testing:
    - Slice-based testing is a testing technique that is used to test the data flow of a program.
    - Slice away all computations that are not relevant to the variable of interest.

## Chapter 8 Integration Testing
Integration Testing:
    - Integration testing is a testing technique that is used to test the integration of the components of a program.
    - The goal of integration testing is to test the integration of the components of a program to ensure that the program is functioning correctly.

Top-Down Integration Testing:
    - Top-down integration testing starts with the highest level of the program and works down to the lowest level of the program.

Bottom-Up Integration Testing:
    - Bottom-up integration testing starts with the lowest level of the program and works up to the highest level of the program.
