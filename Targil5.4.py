def check_id_valid(id_number):
    return sum([sum(divmod(int(digit) * (1 + i % 2), 10)) for i, digit in enumerate(str(id_number))]) % 10 == 0


class IDIterator:
    def __init__(self, id_number):
        self._id_number = id_number

    def __iter__(self):
        self._currentid = self._id_number + 1
        return self

    def __next__(self):
        while self._currentid <= 999999999:
            if check_id_valid(self._currentid):
                current_valid_id = self._currentid
                self._currentid += 1
                return current_valid_id
            self._currentid += 1
        raise StopIteration()


def id_generator(starting_id):
    current_id = starting_id + 1
    while current_id <= 999999999:
        if check_id_valid(current_id):
            yield current_id
        current_id += 1


print("check number 1")
print(check_id_valid(123456780))
print(check_id_valid(123456782))

id_check = int(input("enter your id"))
gen_or_it = input("Generator or Iterator? (gen/it)?")
if gen_or_it == "gen":
    gen = id_generator(id_check)
    for _ in range(10):
        print(next(gen))
elif gen_or_it == "it":
    check = IDIterator(id_check)
    for i, valid_id in zip(range(10), check):
        print(valid_id)
else:
    print("wrong input")

