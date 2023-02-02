input_data = input()
company_database = {}

while input_data != "End":
    company_name, employee_id = input_data.split(" -> ")

    if company_name not in company_database:
        company_database[company_name] = []
    if employee_id not in company_database[company_name]:
        company_database[company_name].append(employee_id)

    input_data = input()

for name, id1 in company_database.items():
    print(f"{name}")
    for el in id1:
        print(f"-- {el}")
