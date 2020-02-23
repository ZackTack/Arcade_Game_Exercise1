import arcade
import random

width = 1280
height = 720
title = "Arcade Game"
radius = 150
sprite_scaling = 0.5
move_speed = 5

class Player(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > width - 1:
            self.right = width - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > height - 1:
            self.top = height - 1

class Coin(arcade.Sprite):
    def update(self):
        coin = arcade.Sprite(":resources:images/items/coinGold.png",sprite_scaling)
        coin.center_x = random.randrange(width)
        coin.center_y = random.randrange(height)

class Game(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)

        self.player_list = None
        self.coin_list = None

        self.player_sprite = None
        self.score = 0

        arcade.set_background_color(arcade.color.GRAY)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = Player(":resources:images/animated_characters/female_person/femalePerson_idle.png",sprite_scaling)
        self.player_sprite.center_y = height/2
        self.player_sprite.center_x = width/2
        self.player_list.append(self.player_sprite)

        for i in range(50):
            coin = arcade.Sprite(":resources:images/items/coinGold.png",sprite_scaling)
            coin.center_x = random.randrange(width)
            coin.center_y = random.randrange(height)

            self.coin_list.append(coin)


    def on_draw(self):
        arcade.start_render()

        self.player_list.draw()
        self.coin_list.draw()

        arcade.draw_text(f"SCORE : {self.score}",width/2,20,arcade.color.WHITE,20)

    def on_update(self, delta_time: float):
        self.player_list.update()

        self.coin_list.update()
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,self.coin_list)

        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.player_sprite.change_y = move_speed
        elif symbol == arcade.key.DOWN:
            self.player_sprite.change_y = -move_speed
        elif symbol == arcade.key.LEFT:
            self.player_sprite.change_x = -move_speed
        elif symbol == arcade.key.RIGHT:
            self.player_sprite.change_x = move_speed

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.player_sprite.change_x = 0



if __name__ == '__main__':
    app = Game(width,height,title)
    app.setup()
    arcade.run()