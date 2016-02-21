from Tkinter import *
from itertools import *
from random import randint

class Elo():

	personas = []
	puntuaciones = []

	def __init__(self):
		self.root = Tk()
		self.root.title("Elo")

		self.nuevonombre = Entry(self.root)
		self.nuevonombre.pack()

		self.addName = Button(self.root, text="Agregar", command=lambda:self.addNewName())
		self.addName.pack()

		self.addName = Button(self.root, text="Comenzar", command=lambda:self.Start())
		self.addName.pack()

		self.root.mainloop()


	def addNewName(self):
		nombre = self.nuevonombre.get()
		self.nuevonombre.delete(0,"end")
		puntuacion = 0
		self.personas.append(nombre)
		self.puntuaciones.append(puntuacion)

	def indexOf(self,arr,find):
		index = -1
		for x in xrange(len(arr)):
			name = arr[x]
			if name == find:
				index = x

		return index

	def Start(self):
		#print self.personas
		infinito = True

		while infinito:
			print self.personas
			combo = combinations(self.personas, 2)
			lista = []
			for x in combo:
				lista.append([x[0],x[1]])

			for i in lista:

				getInd1 = self.indexOf(self.personas,i[0])
				getInd2 = self.indexOf(self.personas,i[1])

				getPoints1 = self.puntuaciones[getInd1]
				getPoints2 = self.puntuaciones[getInd2]

				sum1 = 10
				sum2 = 10

				randomnum = randint(0,1)

				sume = 0
				loser = -1

				if randomnum == 0:
					sume = sum1
					loser = 1

				if randomnum == 1:
					sume = sum2
					loser = 0
				
				ind = self.indexOf(self.personas,i[randomnum])
				self.puntuaciones[ind] = self.puntuaciones[ind] + sume

				#ind2 = self.indexOf(self.personas,i[loser])
				#self.puntuaciones[ind] = self.puntuaciones[ind2] - sume
			
			deleten = 9999999999999999999999999999999
			deletex = -1

			for x in xrange(len(self.puntuaciones)):
				punts = self.puntuaciones[x]
				if punts < deleten:
					deleten = punts
					deletex = x

			self.personas.pop(deletex)
			self.puntuaciones.pop(deletex)

			if len(self.personas) <= 1:
				infinito = False
				print self.personas
			

Elo()
