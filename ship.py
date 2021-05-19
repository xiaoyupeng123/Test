import pygame
class Ship:
	def __init__(self,ai_game):
		#初始化飞船并设置其初始位置
		self.screen=ai_game.screen
		self.setting=ai_game.setting
		self.screen_rect=ai_game.screen.get_rect()


		#加载飞船图像并获取其外接矩形
		self.image=pygame.image.load('images/ship.bmp')
		self.rect=self.image.get_rect()
		self.x=float(self.rect.x)

		#对于每艘飞船，都将其放在屏幕底部的中央
		self.rect.midbottom=self.screen_rect.midbottom
		self.moving_right=False
		self.moving_left=False
		self.moving_up=False
		self.moving_down=False

	def blitme(self):
		#在指定的位置绘制飞船
		self.screen.blit(self.image,self.rect)

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x+=self.setting.ship_speed
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.x-=self.setting.ship_speed
		if self.moving_up:
			self.rect.y-=1
		if self.moving_down:
			self.rect.y+=1
		self.rect.x=self.x