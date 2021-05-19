import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
	""" 管理游戏资源和行为的类"""
	def __init__(self):
		pygame.init()
		self.setting=Settings()
		self.screen=pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))
		pygame.display.set_caption("Alien Invasion")
		self.ship=Ship(self)
		
	def _check_events(self):
		#监听键盘和鼠标事件
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					sys.exit()
				elif event.type==pygame.KEYDOWN:
					self._check_keydown_events(event)
				elif event.type == pygame.KEYUP:
					self._check_keyup_events(event)
					
	def _check_keydown_events(self,event):
		if event.key==pygame.K_RIGHT:
			self.ship.moving_right=True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left=True
		elif event.key == pygame.K_q:
			sys.exit()

	def _check_keyup_events(self,event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right=False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left=False
		

	def _update_screen(self):
		self.screen.fill(self.setting.bg_color)
		self.ship.blitme()
		#让最近绘制的屏幕可见
		pygame.display.flip()

	def run_game(self):
		while True:
			self._check_events()
			#每次循环时都会重绘屏幕
			self.ship.update()
			self._update_screen()
			

if __name__=='__main__':
	ai = AlienInvasion()
	ai.run_game()