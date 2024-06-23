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