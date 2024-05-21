import sqlite3

class Database:
	def __init__(self, db):
		self.conn = sqlite3.connect(db)
		self.cur = self.conn.cursor()

	def query(self, query, args=()):
		self.cur.execute(query, args)
		self.conn.commit()

	def fetch(self, query, args=()):
		self.cur.execute(query, args)
		return self.cur.fetchall()

	def __del__(self):
		self.cur.close()
		self.conn.close()

	def insert(self, table, columns, values):
		self.query("INSERT INTO {} ({}) VALUES ({})".format(table, columns, values))

	def select(self, table, columns, where=None):
		if where:
			self.query("SELECT {} FROM {} WHERE {}".format(columns, table, where))
		else:
			self.query("SELECT {} FROM {}".format(columns, table))

	def update(self, table, columns, values, where):
		self.query("UPDATE {} SET {} WHERE {}".format(table, columns, where))

	def delete(self, table, where):
		self.query("DELETE FROM {} WHERE {}".format(table, where))

	def delete_all(self, table):
		self.query("DELETE FROM {}".format(table))

	def create_index(self, table, column):
		self.query("CREATE INDEX IF NOT EXISTS {} ON {} ({})".format(column, table, column))

	def create_unique_index(self, table, column):
		self.query("CREATE UNIQUE INDEX IF NOT EXISTS {} ON {} ({})".format(column, table, column))

	def create_table(self, table, columns):
		self.query("CREATE TABLE IF NOT EXISTS {} ({})".format(table, columns))

	def drop_table(self, table):
		self.query("DROP TABLE IF EXISTS {}".format(table))

	def rename_table(self, table, new_name):
		self.query("ALTER TABLE {} RENAME TO {}".format(table, new_name))

	def rename_column(self, table, column, new_name):
		self.query("ALTER TABLE {} RENAME COLUMN {} TO {}".format(table, column, new_name))

	def drop_column(self, table, column):
		self.query("ALTER TABLE {} DROP COLUMN {}".format(table, column))

	def create_column(self, table, column):
		self.query("ALTER TABLE {} ADD COLUMN {}".format(table, column))

	def create_column_type(self, table, column, type):
		self.query("ALTER TABLE {} ADD COLUMN {} {}".format(table, column, type))

	def create_column_default(self, table, column, default):
		self.query("ALTER TABLE {} ADD COLUMN {} DEFAULT {}".format(table, column, default))

	def create_column_not_null(self, table, column):
		self.query("ALTER TABLE {} ADD COLUMN {} NOT NULL".format(table, column))

	def create_column_unique(self, table, column):
		self.query("ALTER TABLE {} ADD COLUMN {} UNIQUE".format(table, column))

	def create_column_primary_key(self, table, column):
		self.query("ALTER TABLE {} ADD COLUMN {} PRIMARY KEY".format(table, column))

	def create_column_foreign_key(self, table, column, reference):
		self.query("ALTER TABLE {} ADD COLUMN {} REFERENCES {}".format(table, column, reference))

	def create_column_foreign_key_on_delete(self, table, column, reference, on_delete):
		self.query("ALTER TABLE {} ADD COLUMN {} REFERENCES {} ON DELETE {}".format(table, column, reference, on_delete))

	def create_column_foreign_key_on_update(self, table, column, reference, on_update):
		self.query("ALTER TABLE {} ADD COLUMN {} REFERENCES {} ON UPDATE {}".format(table, column, reference, on_update))

	def create_column_foreign_key_on_delete_on_update(self, table, column, reference, on_delete, on_update):
		self.query("ALTER TABLE {} ADD COLUMN {} REFERENCES {} ON DELETE {} ON UPDATE {}".format(table, column, reference, on_delete, on_update))