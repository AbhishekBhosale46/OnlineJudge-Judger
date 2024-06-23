import os
import shutil
from docker_manager import DockerManager
from languages.cpp import CppLanguage
from languages.python import PythonLanguage


def get_language_instance(language, container, time_limit, memory_limit):
    """
    Returns an instance of the language-specific class based on the provided language.

    Parameters:
    - language (str): The programming language ('cpp', 'java', 'python').
    - container : The Docker container.
    - time_limit: Time limit in seconds.
    - memory_limit: Memory limit in mbs.

    Returns:
    - BaseLanguage: An instance of the language-specific class.
    """

    if language == 'cpp':
        return CppLanguage(container, time_limit, memory_limit)
    elif language == "py":
        return PythonLanguage(container, time_limit, memory_limit)
    else:
        raise ValueError("Unsupported language")


def run_judger(language, time_limit, memory_limit, judger_vol_path, src_code_path, expected_path, ip_tc_path=None):
    """
    Orchestrates the compilation and execution of the provided source code within a Docker container.

    Parameters:
    - language (str): The programming language ('cpp', 'java', 'py').
    - time_limit (int): Time limit in seconds.
    - memory_limit (int): Memory limit in mbs.
    - judger_vol_path (path): Path of the directory to be mounted as container volume.
    - source_code_path (path): Source code file path.
    - expected_path (path): Expected output file path.
    - ip_tc_path (str, optional): Input testcase file path.

    Returns:
        dict: A dictionary containing the compile and run results.
    """

    # Get the container instance
    dm = DockerManager(time_limit=time_limit, memory_limit=memory_limit, judger_vol_path=judger_vol_path)
    container = dm.get_container()

    # Get the specific language instance
    language_instance = get_language_instance(language, container, time_limit, memory_limit)

    try:

        # Create empty input file
        open(f"{judger_vol_path}/ip.txt", "x")

        # Copy user program, ip, expected op to container
        shutil.copy(src_code_path, os.path.join(judger_vol_path, f"UserProgram.{language}"))
        shutil.copy(expected_path, os.path.join(judger_vol_path, "expected_op.txt"))
        if ip_tc_path:
            shutil.copy(ip_tc_path, os.path.join(judger_vol_path, "ip.txt"))

        # Compile the code
        if language in ["cpp", "java"]:
            compile_exit_code, compile_output = language_instance.compile()
            if compile_exit_code == 1:
                return "CE"

        # Run the code
        run_exit_code, run_output = language_instance.run()

        # If no errors then check for WA or AC
        if run_exit_code == 0:
            with open(f"{judger_vol_path}/expected_op.txt", "r") as f:
                expected_op_data = f.read()
            with open(f"{judger_vol_path}/actual_op.txt", "r") as f:
                actual_op_data = f.read()
            if actual_op_data.strip() == expected_op_data.strip():
                return "AC"
            else:
                return "WA"

        # Return the status if run_exit_code is non zero
        if run_exit_code == 1:
            return "RE"
        elif run_exit_code == 143:
            return "TLE"
        elif run_exit_code == 137:
            return "MLE"
        else:
            return "UNKNOWN"

    except Exception as e:

        print(f"EXCEPTION OCCURED : {e}")

    finally:

        # Cleanup the mounted volume
        language_instance.cleanup()