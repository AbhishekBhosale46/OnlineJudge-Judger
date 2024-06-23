# Judger

This project is a judger system designed to compile and run C++, Java, and Python programs inside Docker containers. It ensure that the program stays within specified time and memory limits and handles the cleanup of generated files and artifacts. It also takes input files and compares them with the expected and actual output of the code, providing an appropriate verdict for the program (i.e., TLE, MLE, RE, CE, AC, WA).


## Features

- Isolation using Docker to ensure a secure and consistent execution environment.

- Compile and run C++, Java, and Python programs inside Docker containers.
  
- Handle input test case data for the programs.

- Compare expected and actual output to provide verdicts (TLE, MLE, RE, CE, AC, WA).

- Clean up generated files and artifacts after execution.


## Installation

Clone the project

```bash
  git clone https://github.com/AbhishekBhosale46/OnlineJudge-Judger
```

Go to the project directory

```bash
  cd judger
```

Install dependencies

```bash
  pip install docker
```
## Usage

To run the judger, you need to call the run_judger function with the appropriate parameters. Here's an example of how to use it:

```
from src import judger

print(
    judger.run_judger(
        language='cpp',
        time_limit=1,
        memory_limit=128,
        judger_vol_path=r"PATH_TO_CONTAINER_VOL",
        src_code_path=r".\tests\cpp\cpp_test.cpp",
        expected_path=r".\tests\cpp\cpp_op.txt",
    )
)

print(
    judger.run_judger(
        language='py',
        time_limit=1,
        memory_limit=128,
        judger_vol_path=r"PATH_TO_CONTAINER_VOL",
        src_code_path=r".\tests\python\py_test.py",
        expected_path=r".\tests\python\py_op.txt",
    )
)
```




## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

- 1] Fork the repository.
- 2] Create a new branch (git checkout -b feature-branch).
- 3] Make your changes.
- 4] Commit your changes (git commit -m 'Add some feature').
- 5] Push to the branch (git push origin feature-branch).
- 6] Open a pull request.

