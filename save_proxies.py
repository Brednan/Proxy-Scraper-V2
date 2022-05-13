class SaveProxies:
    def __init__(self, output):
        self.output = output

    def save_http(self, proxies):
        output_file = open(self.output, 'w')
        output_file.write('Http Proxies:\n')

        for p in proxies:
            output_file.write(f'p\n')

        output_file.close()

    def save_socks(self, proxies):
        output_file = open(self.output, 'a')
        output_file.write('Socks4 Proxies:\n')

        for p in proxies:
            output_file.write(f'p\n')

        output_file.close()