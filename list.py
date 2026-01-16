employees = ["Alice", "Bob", "Charlie", "David", "Eve"];
for index, emp in enumerate(employees, start=1):
    print(f"{index}: {emp}")

#without using enumerate
# count= 1
# for emp in employees:
#     print(count, ":", emp)
#     count +=1