import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name = "Slither",
    options = {"build_exe":{"packages":["pygame"], "include_files":["apple.png","icon.png","snake_head.png","snake_tail.png"]}},
    description = "Slither Game",
    executables = executables
    )
