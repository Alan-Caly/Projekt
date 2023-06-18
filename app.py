# File: app.py
#
# Authors: Firstname Lastname
# Date: TODO: add date
# License: TODO: add license
# Description: TODO: add description

import time
from server import app
from server.src.server.Server import Server

# Start Flask application
if __name__ == '__main__':
    server = Server()

    while True:
        # Get input from user
        operation = input('Enter operation: ').lower()

        match operation:
            case '--start-server':
                # Start server
                server.run()
                break

            case '--init-database':
                # Initialize database
                server.init_db()

            case '--start-test':
                # Start test
                server.run_test()

            case '--help':
                # Show help
                server.help()
                break

            case 'exit':
                exit(0)

            case _:
                # Unknown operation
                print(f'Unknown operation: {operation}')
                print(f'If you need help, please use --help\n')
