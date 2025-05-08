name = input('Type your name: ')
print('Welcome', name, 'to my game:)')

choice = input("You're in a garden centre to do some shopping. You can go to the seed or flower section. Which way would you like to go? ").lower()

if choice == 'seed':
    choice = input("You can't find your seed packets so you decide to order it online or go for a cake. Type online or cake: ").lower()

    if choice == 'online':
        print('You ordered the seeds online and went home.')

    elif choice == 'cake':
        print('You ordered a cake and went home.')

    else:
        print('Sorry, not a valid option. Choose again')


elif choice == 'flower':
    choice = input('You found flowers that you wanted to buy, but they look really weak. Do you still want to buy them. Type yes or no: ').lower()

    if choice == 'yes':
        print('You watered the plants at home and they were fine after a few days.')

    elif choice == 'no':
        choice = input('You decided to go to a different garden centre and met a friend. She invited you for a coffee. Do you want to coninue shopping or have a coffe with a friend. Type shop or coffee: ')
        
        if choice == 'shop':
           print('You declined her invitation, arrange a catch up for another day and continued shopping.')

        elif choice == 'coffee':
             print('You went for a coffee with the friend and she offered to give you her spare flowers for free.Win! Win!')

        else:
            print('Sorry, not a valid option. Choose again')

        
else:
    print('Sorry, not a valid option. Choose again')

print('Thank you for playing my game :)')