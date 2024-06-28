from src import judger

print(
    judger.run_judger(
        language='cpp',
        time_limit=1,
        memory_limit=128,
        judger_vol_path=r"PATH_TO_CONTAINER_VOL",
        src_code_path=r".\tests\cpp\cpp_test.cpp",
        expected_out_path=r".\tests\cpp\cpp_op.txt",
    )
)

print(
    judger.run_judger(
        language='py',
        time_limit=1,
        memory_limit=128,
        in_tc="10\n5",
        judger_vol_path=r"PATH_TO_CONTAINER_VOL",
        src_code="a=int(input())\nb=int(input())\nprint('Sum is', a+b)",
        expected_out="Sum is 15"
    )
)