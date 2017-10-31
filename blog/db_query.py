from django.db import connections


class DbHandle:
    results = []

    def __init__(self, model, database=None):
        self.my_model = model
        db = database
        self.coursor = connections[db].cursor()

    def all(self, order=None):
        if order is None:
            self.coursor.execute('select * from %s' % self.my_model)
        else:
            self.coursor.execute('select * from %s order by %s' % (self.my_model, order))
        self.results = self.coursor.fetchall()
        return self.results