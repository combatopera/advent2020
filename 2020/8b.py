from adventlib import inpath
from adventlib.handheld import Computer, Program

def main():
    with inpath().open() as f:
        program = Program.load(f)
    c = Computer()
    subs = dict(jmp = 'nop', nop = 'jmp')
    for index, instruction in enumerate(program.instructions):
        sub = subs.get(instruction[0])
        if sub is not None and c.exec(program.patched(index, sub)):
            break
    print(c.accumulator)
