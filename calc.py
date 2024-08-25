
while True:
    
    choice = input('what do you want to do: addition, subtraction, multiplication, division ')

    if choice == 'addition':
        addition_num1 = int(input('what is the 1st number you would like to add '))
        addition_num2 = int(input('what is the 2nd number you would like to add '))
        print(addition_num1 + addition_num2)
    

    elif choice == 'subtraction':
        subtraction_num1 = int(input('what is the 1st number you would like to subtract '))
        subtraction_num2 = int(input('what is the 2nd number you would like to subtract '))
        print(subtraction_num1 - subtraction_num2)

    elif choice == 'multiplication':
        multiplication_num1 = int(input('what is the 1st number you would like to multiply '))
        multiplication_num2 = int(input('what is the 2nd number you would like to multiply '))
        print(multiplication_num1 * multiplication_num2)


    elif choice == 'division':
        division_num1 = int(input('what is the 1st number you would like to divide '))
        division_num2 = int(input('what is the 2nd number you would like to divide '))
        print(division_num1 / division_num2)


    else:
        print(input('please input a valid operation [addition] [subtraction] [multiplication] [division] '))
