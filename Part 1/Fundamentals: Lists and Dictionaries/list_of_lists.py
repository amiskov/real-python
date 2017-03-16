def enrollment_stats(list_of_lists):
    enrolled_students = []
    tuition_fees = []

    for item in list_of_lists:
        enrolled_students.append(item[1])
        tuition_fees.append(item[2])

    return [enrolled_students, tuition_fees]


def mean(items):
    count = 0

    for item in items:
        count += int(item)
    return count / len(items)


def median(items):
    items.sort()
    count = len(items)

    if count % 2 == 0:
        x = items[count / 2 - 1]
        y = items[count / 2]

        return (x + y) / 2
    else:
        return items[count // 2]


universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

students_fees = enrollment_stats(universities)

print("Total students:", sum(students_fees[0]))
print("Total tuition:", "${0}".format(sum(students_fees[1])))
print('')
print("Student mean:", mean(students_fees[0]))
print("Student median:", median(students_fees[0]))
print('')
print("Tuition mean:", mean(students_fees[1]))
print("Tuition median:", median(students_fees[1]))
