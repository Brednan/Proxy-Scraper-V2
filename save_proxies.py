class SaveProxies:
    def __init__(self, output):
        self.output = output

    def save_proxies(self, proxies):
        output_file = open(self.output, 'a')

        for p in proxies:
            output_file.write(f'{p}\n')

        output_file.close()