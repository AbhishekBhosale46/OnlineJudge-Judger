from abc import ABC, abstractmethod


class BaseLanguage(ABC):

    """
    BaseLanguage is an abstract base class for different programming languages.
    """

    @abstractmethod
    def compile(self):
        """
        Abstract method to compile the source code.
        """
        pass

    @abstractmethod
    def run(self):
        """
        Abstract method to run the compiled code.
        """
        pass

    def cleanup(self):
        """
        Remove all the files and directories from the present working directory

        Returns:
        - exit_code - exit code of the executed command
        - run_output - output of the command
        """

        cleanup_cmd = "/bin/sh -c 'rm -rf *' "
        exit_code, cleanup_output = self.container.exec_run(cleanup_cmd)
        return exit_code, cleanup_output.decode('utf-8')
