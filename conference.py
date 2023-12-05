

def main():
    print('This program manages the conference roster.')
    filename = input('Please provide the filename of the roster database: ')

    myConference = Conference(filename)
    while True:
        action = input('What would you like to do? [ADD, DELETE, VIEW, LIST, FILTER]: ')
        actions = ['ADD', 'DELETE', 'VIEW', 'LIST', 'FILTER']
        if action in actions:
            if action == 'ADD':
                name = input('Please enter the name of the attendee: ')
                company = input('')
                state = input('')
                email = input('')
                myConference.addAttendee(name, company, state, email)
        else:
            print('Not a valid action.')


if __name__ == '__main__':
    main()
