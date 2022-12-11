import pprint
import sys
import math
printer = pprint.PrettyPrinter(indent=2, depth=10)
sys.set_int_max_str_digits(100000)


OPERATION = {
    "MULTIPLY": '*',
    "ADD": '+'
}


class Monkey:
    def __init__(self, id, items, operation, operation_num, div_test_num, true_case, false_case):
        self.id = id
        self.items = items
        self.operation = operation
        self.operation_num = operation_num
        self.div_test_num = div_test_num
        self.true_case = true_case
        self.false_case = false_case
        self.cnt = 0

    def __repr__(self):
        return f"id: {self.id},\nitems: {self.items},\noperation: {self.operation},\n operation_num: {self.operation_num},\n div_test_num: {self.div_test_num}, true_case: {self.true_case}, false_case: {self.false_case}, cnt: {self.cnt}"


def helper_mod(num: str, div: int) -> int:
    res = 0
    for i in range(len(num)):
        res = (res * 10 + int(num[i])) % div
    return res


def day_11_1() -> int:
    result = 69

    with open("../input/input_11.txt") as fp:
        monkeys = []
        while True:
            for i in range(8):
                line = fp.readline()
                first_line_tokens = line.split(" ")
                m_id = first_line_tokens[1][:-2]

                line = fp.readline().strip()
                tmp = line.split(":")
                items = [int(x.strip()) for x in tmp[1].split(", ")]

                line = fp.readline().strip()
                tmp = line.split(" = ")
                tmp_2 = tmp[1].split(" ")
                operation = tmp_2[1]
                operation_num = tmp_2[2].strip()

                line = fp.readline().strip()
                tokens = line.split(" ")
                div_test_num = int(tokens[3].strip())

                line = fp.readline().strip()
                tokens = line.split(" ")
                true_case = int(tokens[5].strip())

                line = fp.readline().strip()
                tokens = line.split(" ")
                false_case = int(tokens[5].strip())

                monkeys.append(Monkey(
                    m_id, items, operation, operation_num, div_test_num, true_case, false_case))

                redundant_line = fp.readline()
            break

        modulos = math.lcm(*[x.div_test_num for x in monkeys])
        for i in range(10000):
            for j in range(8):
                for item in monkeys[j].items:
                    if monkeys[j].operation == OPERATION["ADD"]:
                        item += int(monkeys[j].operation_num)
                    elif monkeys[j].operation == OPERATION["MULTIPLY"]:
                        if monkeys[j].operation_num == "old":
                            item = item ** 2
                        else:
                            item *= int(monkeys[j].operation_num)
                    else:
                        raise("Unknown behavior")

                    item = item % modulos

                    # if helper_mod(str(int(item[0]) + tmp), int(monkeys[j].div_test_num)) == 0:
                    if item % monkeys[j].div_test_num == 0:
                        monkeys[monkeys[j].true_case
                                ].items.append(item)
                    else:
                        monkeys[monkeys[j].false_case
                                ].items.append(item)
                    monkeys[j].items = monkeys[j].items[1:]
                    monkeys[j].cnt += 1

        printer.pprint(monkeys)
    return result
