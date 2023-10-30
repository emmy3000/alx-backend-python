# 0x03. Unittests and Integration Tests

Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

Execute your tests with
```shell
$ python -m unittest path/to/test_file.py
```

## Distinguishing between Unit tests and Integration tests.

Unit tests and integrated tests are two distinct types of software testing that serve different purposes and target different aspects of a software application. Here are the key differences between them:

### Scope:

**Unit Test:** A unit test focuses on testing a small, isolated piece of code, typically a single function, method, or class. It is designed to verify that the individual components of the software (units) work correctly in isolation. Unit tests are concerned with the internal logic and behavior of a specific code unit and do not consider how it interacts with other parts of the application.

**Integrated Test:** An integrated test, on the other hand, tests the interactions between multiple units or components of the software. It verifies that these components work together as expected when integrated into a larger system. Integrated tests assess how different parts of the application interact and share data or functionality.

### Dependencies:

**Unit Test:** Unit tests are typically designed to run independently of external dependencies. Any external dependencies, such as databases or network services, are usually replaced with mock objects or stubs to isolate the unit being tested.

**Integrated Test:** Integrated tests often involve real external dependencies, and they may test how the software interacts with these dependencies. This means that integrated tests may require more setup and may be sensitive to the configuration of the external systems.

### Purpose:

**Unit Test:** Unit tests are primarily focused on verifying the correctness of individual code units. They help catch bugs and issues at a granular level, making it easier to pinpoint the source of problems.

**Integrated Test:** Integrated tests aim to ensure that different parts of the software can work together harmoniously. They help identify issues related to integration, data flow, and the overall system's behavior.

### Execution Time:

**Unit Test:** Unit tests are typically faster to execute since they focus on small, isolated units of code. They are meant to be executed frequently during development.

**Integrated Test:** Integrated tests may take longer to execute due to their broader scope and potential reliance on external systems. They are often run less frequently, such as during integration or system testing phases.

### Isolation:

**Unit Test:** Unit tests are isolated from other parts of the code, ensuring that any failures are specific to the unit being tested. This isolation makes it easier to identify and fix issues.

**Integrated Test:** Integrated tests are inherently less isolated as they assess how different components interact. This can make it more challenging to pinpoint the source of failures.

In a typical software testing strategy, both unit tests and integrated tests play essential roles. Unit tests are used to validate the correctness of individual code units, while integrated tests are used to verify that these units work together as a coherent and functional system. This combination of testing helps ensure the reliability and quality of the software.

## Author

Emeka Emodi
