data = []


# ---------------- BUILT-IN FUNCTION ----------------
def data_summary(values):
    """Display basic summary using built-in functions"""

    if len(values) == 0:
        print("\nNo data available!")
        return

    print("\nData Summary:")
    print("Total elements :", len(values))
    print("Minimum value  :", min(values))
    print("Maximum value  :", max(values))
    print("Sum of values  :", sum(values))
    print("Average value  :", round(sum(values) / len(values), 2))


# ---------------- RECURSION FUNCTION ----------------
def factorial(num):
    """Calculate factorial using recursion"""

    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


# ---------------- LAMBDA FUNCTION ----------------
def filter_data(values, threshold):
    """Filter values using lambda"""

    result = list(filter(lambda x: x >= threshold, values))

    print("\nFiltered Data:")
    print(result)


# ---------------- SORT FUNCTION ----------------
def sort_data(values):
    """Sort data in ascending or descending order"""

    print("\n1. Ascending")
    print("2. Descending")

    choice = int(input("Enter choice : "))

    if choice == 1:
        values.sort()
        print("\nAscending Order :", values)

    elif choice == 2:
        values.sort(reverse=True)
        print("\nDescending Order :", values)

    else:
        print("Invalid Choice")


# ---------------- *args FUNCTION ----------------
def total_sum(*numbers):
    """Calculate total using *args"""

    total = 0

    for i in numbers:
        total += i

    return total


# ---------------- **kwargs FUNCTION ----------------
def student_info(**details):
    """Display dataset info using **kwargs"""

    print("\nDataset Information")

    for key, value in details.items():
        print(key, ":", value)


# ---------------- RETURN MULTIPLE VALUES ----------------
def dataset_statistics(values):
    """Return multiple values"""

    minimum = min(values)
    maximum = max(values)
    total = sum(values)
    average = round(total / len(values), 2)

    return minimum, maximum, total, average


# ---------------- MAIN PROGRAM ----------------
while True:

    print("\n====== DATA ANALYZER PROGRAM ======")

    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data")
    print("5. Sort Data")
    print("6. Dataset Statistics")
    print("7. *args Example")
    print("8. **kwargs Example")
    print("9. Exit")

    choice = int(input("\nEnter your choice : "))

    # ---------- INPUT DATA ----------
    if choice == 1:

        numbers = input("\nEnter numbers separated by space : ")

        data = list(map(int, numbers.split()))

        print("Data Stored Successfully!")

    # ---------- DATA SUMMARY ----------
    elif choice == 2:

        data_summary(data)

    # ---------- FACTORIAL ----------
    elif choice == 3:

        num = int(input("\nEnter number : "))

        ans = factorial(num)

        print("Factorial is :", ans)

    # ---------- FILTER DATA ----------
    elif choice == 4:

        limit = int(input("\nEnter threshold value : "))

        filter_data(data, limit)

    # ---------- SORT DATA ----------
    elif choice == 5:

        sort_data(data)

    # ---------- RETURN MULTIPLE VALUES ----------
    elif choice == 6:

        if len(data) == 0:
            print("\nNo data available!")

        else:
            a, b, c, d = dataset_statistics(data)

            print("\nDataset Statistics")
            print("Minimum :", a)
            print("Maximum :", b)
            print("Sum     :", c)
            print("Average :", d)

    # ---------- *args ----------
    elif choice == 7:

        answer = total_sum(10, 20, 30, 40)

        print("\nTotal using *args :", answer)

    # ---------- **kwargs ----------
    elif choice == 8:

        student_info(
            Name="Raj",
            Course="Python",
            City="Bhavnagar"
        )

    # ---------- EXIT ----------
    elif choice == 9:

        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice")