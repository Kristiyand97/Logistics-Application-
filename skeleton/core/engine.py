from skeleton.core.command_factory import CommandFactory


class Engine:
    def __init__(self, factory: CommandFactory, output_file="output.txt"):
        self._command_factory = factory
        self.output_file = output_file

    def start(self):
        output: list[str] = []
        while True:
            input_line = input()
            if input_line.lower() == 'end':
                break

            command = self._command_factory.create(input_line)

            output.append(command.execute())

        with open(self.output_file, 'w') as file:
            file.write('\n'.join(output))

        print('\n'.join(output))
