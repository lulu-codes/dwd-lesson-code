# match-case: Ask the user to input a command (e.g., "start", "stop", "pause").
# Use match-case to print a different action message for each command (e.g., "Process starting...", "Process stopping...").
# Include a default for unknown commands."

command = input('Command: ')
print(command.lower())
match command.lower():
    case 'start':
        print('Process starting ...')
    case 'stop':
        print('Process stopping ...')
    case 'pause':
        print('Process paused.')
    case _:
        print('Unknown command')


command= input('Enter Command: ')
match command.lower():
    case 'start':
        print('Starting')
    case 'stop':
        print('Stopping')
    case 'pause':
        print('Pausing')
    case _:
        print('Command Unknown')