class Data:
    def _init_(self):
        self.data = []
        
    def add_record(self, record):
        self.data.append(record)
        
    def get_all(self):
        return self.data