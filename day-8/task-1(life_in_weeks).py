def life_in_weeks(age):
    current_weeks = age * 12 * 4

    max_age = 70
    max_weeks = max_age * 12 * 4

    weeks_left = max_weeks - current_weeks

    print(f"You have {weeks_left} weeks left")


age = int(input("Enter your age: "))

life_in_weeks(age)
