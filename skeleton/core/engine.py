from skeleton.core.command_factory import CommandFactory


class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory

    def start(self):
        output: list[str] = []
        while True:
            try:
                input_line = input()
                if input_line.lower() == 'end':
                    break

                try:
                    command = self._command_factory.create(input_line)
                    output.append(command.execute())
                except Exception as e:
                    print(f"Invalid command: {e}. Please try again.")

            except KeyboardInterrupt:
                print("Program interrupted by user.")
                break
            except Exception as e:
                print(f"Unexpected error: {e}")
                break

        print('\n'.join(output))
