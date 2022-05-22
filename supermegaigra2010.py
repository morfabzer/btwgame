from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from threading import Timer
from random import random
import sys
from time import sleep

app = QtWidgets.QApplication([]) # Создание APP
win = uic.loadUi("Game.ui") # расположение файла дизайна
win.setWindowTitle('btwdermo') # Title
win.setFixedSize(489,454)
# Классы для создания персонажа
class hero():
	def __init__(self,health,armor,damage):
		self.health = health
		self.armor = armor
		self.damage = damage

		hero_label[0](hp_text.replace('*Value',str(health)))
		hero_label[1](armor_text.replace('*Value',str(armor)))
		hero_label[2](damage_text.replace('*Value',str(damage)))

class monster():
	def __init__(self,health,armor,damage):
		self.health = health
		self.armor = armor
		self.damage = damage

def startAttack():
	button.setEnabled(False)
	enemy = monster(100, 5, 5)
	move = 1
	list_items = 0
	while True:
		chance = random()
		if move == 1:
			move = 2
			if player.damage == enemy.armor:
				if chance < 0.5:
					enemy.health -= player.damage
					if enemy.health <= 0:
						move = 1
						logger.addItem('Вы победили')
						break
					else:
						logger.addItem(f'Вы нанесли {player.damage} hp | HP врага: {enemy.health}')
				else:
					logger.addItem(f'Противник отразил ваш удар | HP врага: {enemy.health}')
			elif player.damage > enemy.armor:
				enemy.health -= player.damage
				if enemy.health <= 0:
					move = 1
					logger.addItem('Вы победили')
					break
				else:
					logger.addItem(f'Вы нанесли {player.damage} hp | HP врага: {enemy.health}')
			elif player.damage < enemy.armor:
				logger.addItem(f'Противник отразил ваш удар | HP врага: {enemy.health}')
		elif move == 2:
			move = 1
			if enemy.damage == player.armor:
				if chance < 0.5:
					player.health -= enemy.damage
					hero_label[0](hp_text.replace('*Value',str(player.health)))
					if player.health <= 0:
						move = 1
						logger.addItem('Вы проиграли')
						break
					else:
						logger.addItem(f'Вам нанесли {enemy.damage} hp | HP: {player.health}')
				else:
					logger.addItem(f'Вы отразили удар | HP: {player.health}')
			elif enemy.damage > player.armor:
				player.health -= enemy.damage
				hero_label[0](hp_text.replace('*Value',str(player.health)))
				if player.health <= 0:
					move = 1
					logger.addItem('Вы Проиграли')
					break
				else:
					logger.addItem(f'Вам нанесли {enemy.damage} hp | HP: {player.health}')
			elif player.damage < enemy.armor:
				logger.addItem(f'Вы отразили удар | HP: {player.health}')
		sleep(1)


# Глобальные переменные
hp_text = "HP: *Value"
armor_text = "Armor: *Value"
damage_text = "damage: *Value"

hero_label = [
	win.HP.setText,
	win.Armor.setText,
	win.Damage.setText
]
button = win.B_attack
logger = win.logger
player = hero(100, 5, 5)

# работа с кнопкой
button.clicked.connect(lambda: Timer(0,startAttack).start())

#Запуск приложения
win.show()
sys.exit(app.exec())