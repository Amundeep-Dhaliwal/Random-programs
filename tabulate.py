class Table:
    def __init__(self, data, headers = None):
        self.print_table(data, headers)

    def calculate_max_length(self, transactions, header_length = 0):
        max_str_length = header_length
        for transaction in transactions:
            word_length = max(len(word) for word in transaction)
            if max_str_length < word_length:
                max_str_length = word_length
        return max_str_length

    def calculate_columns(self, data, headers = 0):
        data_rows = max(len(row) for row in data)
        max_columns = data_rows if data_rows > headers else headers
        return max_columns 
        
    def draw_horizontal(self, side, width, columns):
        line = '+'
        for i in range(columns):
            line += width * side
            line += '+'
        print(line)

    def draw_row(self, width, data, columns):
        line = '|'
        for entry in data:
            line += entry.center(width)
            line += '|'
        separators = line.count('|')
        required_separators = columns + 1
        if required_separators > separators:
            repetitions = required_separators - separators
            additional_columns = (''.center(width) + '|') * repetitions
            line += additional_columns
        print(line)

    def print_table(self, data, headers = None):
        if headers:
            max_header_length = max(len(word) for word in headers)
            width = self.calculate_max_length(data, max_header_length)
            columns = self.calculate_columns(data, len(headers))
            self.draw_horizontal('-', width,columns)
            self.draw_row(width, headers, columns)
            self.draw_horizontal('=',width, columns)
        else:
            width = self.calculate_max_length(data)
            columns = self.calculate_columns(data)
            self.draw_horizontal('=',width, columns)
        
        for row in data:
            self.draw_row(width, row, columns)
            self.draw_horizontal('-', width, columns)
