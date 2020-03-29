import datetime

class Card:

	def __init__(self, num_doc, date):
		self.num_doc = num_doc
		self.date = date
		self.services = {}

	def addService(self, service, credit = 0, debt = 0):
		self.services[service] = [credit, debt]

	def delService(self, service):
		credit, debt = self.services.pop(service)


	def getServices(self):
		return list(self.services.items())


def addPer(diction, date, value):
	if date in diction:
		diction[date].append(value)
	else:
		diction[date] = [value]

	return diction


class Cards:

	def __init__(self):
		self.days = {}
		self.month = {}
		self.years = {}
		self.memory = []
		self.count_elem = 0



	def addCard(self, num_doc, date, services, values):

		month_index = datetime.datetime(date.year,date.month,1)
		year_index = datetime.datetime(date.year,1,1)


		self.days = addPer(self.days, date, self.count_elem)
		self.month = addPer(self.month, month_index, self.count_elem)
		self.year = addPer(self.years, year_index, self.count_elem)


		card = Card(num_doc, date)
		for i in range(len(services)):
			card.addService(services[i], values[i])
		self.memory.append(card)
		self.count_elem +=1

	def delCard(self, num_doc, date):
		if date not in self.days:
			return 0

		indxs = self.days.pop(date)

		for i in indxs:
			if self.memory[i].num_doc == num_doc:
				self.memory = self.memory[0:i] + self.memory[i+1:len(self.memory)]
				break

	def _getCards(self, indexes):
		rez = {}
		total_credit = 0
		total_debt = 0
		if len(indexes) == 0:
			return rez, total_credit, total_debt
		for i in indexes:
			card = self.memory[i]
			services = card.getServices()
			for serv, [credit, debt] in services:
				total_credit += credit
				total_debt += debt
				if serv in rez:
					rez[serv][0] += credit
					rez[serv][1] += debt
					continue
				rez[serv] = [credit, debt]
		return rez, total_credit, total_debt


	def _getValueFromDict(self, key, diction):
		if key not in diction:
			return []
		return diction[key]

	def getCards(self, date, period = 'month'):

		if period == 'day':
			day = date
			indexes = self._getValueFromDict(day, self.days)
		if period == 'month':
			month = datetime.datetime(date.year, date.month, 1)
			indexes = self._getValueFromDict(month, self.month)
		if period == 'year':
			year = datetime.datetime(date.year, 1, 1)
			indexes = self._getValueFromDict(year, self.year)
		
		return self._getCards(indexes)