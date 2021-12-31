def numbers(first_name, last_name, kid_name, year, addi):
    a = 0
    fullname1 = first_name + last_name
    fullname2 = last_name + first_name
    first_name_year = first_name + year
    last_name_year = last_name + year
    full_name_year = first_name + last_name + year
    info = [first_name, last_name, kid_name, year, addi, fullname1, fullname2, first_name_year, last_name_year, full_name_year]
    print(fullname1)
    for x in info:
        print(x)
        for i in range(999):
            print(x + str(i))
            print(str(i) + x)
            a += 1


if __name__ == "__main__":
    f=open('C:/Users/ilanm/source/brute.txt', 'w')
    first_name = input("enter first name of victim: ")
    last_name = input("enter last name of victim: ")
    kid_name = input("enter kid name of victim: ")
    year = input("enter year of birth of the victim: ")
    addi = input("enter additional info: ")
    numbers(first_name, last_name, kid_name, year, addi)

