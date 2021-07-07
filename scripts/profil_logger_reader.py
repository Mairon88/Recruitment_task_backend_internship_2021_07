class ProfilLoggerReader:

    def __init__(self, handler):

        self.handler = handler
        self.load_data = self.handler.read()

    def find_by_text(self, text, start_date=None, end_date=None):
        pass
        # return list

    def find_by_regex(self, regex, start_date=None, end_date=None):
        pass
        # return list

    def groupby_level(self, start_date=None, end_date=None):
        pass
        # return dict

    def groupby_month(self, start_date=None, end_date=None):
        pass
        # return dict