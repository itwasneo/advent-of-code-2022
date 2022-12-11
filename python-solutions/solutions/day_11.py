from typing import List
from collections import deque
from operator import add, mul, attrgetter
import math


class Monkey:
    """
    I actually didn't know that you could allocate static
    memory for python objects, but apparently __slots__ function
    provides that with faster access with more memory efficiency
    """
    __slots__ = ('items', 'operation', 'operation_val',
                 'divisor', 'true_case', 'false_case', 'cnt')

    def inspect(self) -> int:
        """
        Operating corresponding operation,popping the item from
        the list.
        """
        item = self.items.popleft()
        if self.operation_val is None:
            return self.operation(item, item)
        return self.operation(item, self.operation_val)

    def __repr__(self):
        return f"items: {self.items},\noperation: {self.operation},\n operation_val: {self.operation_val},\n divisor: {self.divisor}, true_case: {self.true_case}, false_case: {self.false_case}, cnt: {self.cnt}"


def helper_mod(num: str, div: int) -> int:
    """
    I thought this would help but this is way slower.
    """
    res = 0
    for i in range(len(num)):
        res = (res * 10 + int(num[i])) % div
    return res


def solve(part_no: int, rounds: int) -> int:
    """
    LCM approach. Nothing special
    """
    monkeys = read_data("../input/input_11.txt")
    if part_no == 2:
        modulus = math.lcm(*[x.divisor for x in monkeys])
    for i in range(rounds):
        for m in monkeys:
            while m.items:
                worry_value = m.inspect()
                if part_no == 1:
                    worry_value = worry_value // 3
                elif part_no == 2:
                    worry_value = worry_value % modulus
                else:
                    raise("Unknown part no??")

                if worry_value % m.divisor == 0:
                    # if helper_mod(str(worry_value), m.divisor) == 0:
                    monkeys[m.true_case].items.append(worry_value)
                else:
                    monkeys[m.false_case].items.append(worry_value)
                m.cnt += 1
    return mul(*sorted(map(attrgetter('cnt'), monkeys), reverse=True)[:2])


def read_data(file_name: str) -> List[Monkey]:
    with open(file_name) as fp:
        monkeys = []
        monkey_instructions = fp.read().split('\n\n')
        for instruction in monkey_instructions:
            lines = instruction.splitlines()
            new_monkey = Monkey()
            new_monkey.items = deque(
                [int(x.strip()) for x in lines[1].split(":")[1].split(", ")])
            operation_tokens = lines[2].split(
                " = ")[1].split(" ")
            new_monkey.operation = add if operation_tokens[1] == '+' else mul
            tmp = operation_tokens[2].strip()
            new_monkey.operation_val = None if tmp == "old" else int(tmp)
            new_monkey.divisor = int(lines[3].strip().split(" ")[3])
            new_monkey.true_case = int(lines[4].strip().split(" ")[5].strip())
            new_monkey.false_case = int(lines[5].strip().split(" ")[5].strip())
            new_monkey.cnt = 0
            monkeys.append(new_monkey)
        return monkeys


def day_11_1() -> int:
    result = solve(1, 20)
    print(f"day_11_1_solution: {result}")
    return result


def day_11_2() -> int:
    result = solve(2, 10000)
    print(f"day_11_2_solution: {result}")
    return result
