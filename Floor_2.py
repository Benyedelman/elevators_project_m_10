
import pygame
from Elevator_2 import Elevator
import time
import threading
class Floor:
    def __init__(self,):
        # self.NUM_FLOORS = 10
        self.FLOORS_IMAGE = "Screenshot from 2024-05-29 10-47-25.png"
        self.floor_img = pygame.image.load(self.FLOORS_IMAGE)
        self.CONTROL_COLOR = (128,128,128)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 190, 0)
        self.RED = (200, 0, 0)
        self.FLOOR_WIDTH = 133.5
        self.FLOOR_HEIGHT = 50
        self.LINE_HEIGHT = 7
        self.button = 0
        self.number_position = 0
        self.button_radius  = 10
        self.SCREEN_HEIGHT = 0
        self.sky_blue = (135, 206, 235)
        self.elevator_on_the_way = False

    #  Builds all floors, black line, button color, button, and number floor
    def floors_builder(self, SCREEN_HEIGHT, floor_num, screen):
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        y = self.SCREEN_HEIGHT - (floor_num + 1) * self.FLOOR_HEIGHT - self.LINE_HEIGHT * floor_num   #floor builder
        x = 0
        screen.blit(self.floor_img, (x, y))
        y = self.SCREEN_HEIGHT - floor_num * self.FLOOR_HEIGHT - self.LINE_HEIGHT * floor_num - self.FLOOR_HEIGHT/2        # draw batten
        x = self.FLOOR_WIDTH / 3
        pygame.draw.circle(screen, self.CONTROL_COLOR, [x, y], 10) 
        self.button = x, y
        y = self.SCREEN_HEIGHT - floor_num * self.FLOOR_HEIGHT - self.LINE_HEIGHT * floor_num  #write a number on each floor
        font = pygame.font.Font(None, 25)
        number = font.render(f"{floor_num}", True, (self.BLACK))
        screen.blit(number, (39, y - 33))
        self.number_position = 39, y - 33
        y = self.SCREEN_HEIGHT - (floor_num + 1) * self.FLOOR_HEIGHT - self.LINE_HEIGHT * floor_num - self.LINE_HEIGHT / 2   # mark black line
        x = 0
        pygame.draw.line(screen, self.BLACK, [x, y], [self.FLOOR_WIDTH-1, y], self.LINE_HEIGHT)
        pygame.display.flip() 

    # After the elevator is finished, returns the original button color 
    def change_button_color(self, screen, x_button_location, y_button_location, num_invitation, x_num_location, y_num_location):
        pygame.draw.circle(screen, self.CONTROL_COLOR, [x_button_location, y_button_location], 10) 
        font = pygame.font.Font(None, 25)
        number = font.render(f"{num_invitation}", True, (self.BLACK))
        screen.blit(number, (x_num_location,y_num_location))

    # Calculates the time and presents it 
    def timer(self, num_invitation, screen, lift):
        timer = abs(lift.position_of_last_floor - num_invitation)/2 + lift.finish_time
        lift.position_of_last_floor = num_invitation
        lift.finish_time +=  timer + 2
        if timer > 0:
            font = pygame.font.Font(None, 25)
            number = font.render(f"{timer}", True, (self.RED))
            screen.blit(number, (100, self.SCREEN_HEIGHT - num_invitation * self.FLOOR_HEIGHT - self.LINE_HEIGHT * num_invitation -  self.FLOOR_HEIGHT/ 2 - 5 ))
            pygame.display.flip()
            thread = threading.Thread(target = lift.stopwatch_for_finish_time, args = ())
            thread.start() 
        while timer > 0:
            timer -= 0.5
            time.sleep(0.5)
            # lift.finish_time  -= 0.5

            pygame.draw.circle(screen, self.sky_blue, [112, self.SCREEN_HEIGHT - num_invitation * self.FLOOR_HEIGHT - self.LINE_HEIGHT * num_invitation -  self.FLOOR_HEIGHT/ 2 - 5  + 8], 20)
            font = pygame.font.Font(None, 25)
            number = font.render(f"{timer}", True, (self.RED))
            screen.blit(number, (100, self.SCREEN_HEIGHT - num_invitation * self.FLOOR_HEIGHT - self.LINE_HEIGHT * num_invitation -  self.FLOOR_HEIGHT/ 2 - 5 ))
            pygame.display.flip() 
        pygame.draw.circle(screen, self.sky_blue, [112, self.SCREEN_HEIGHT - num_invitation * self.FLOOR_HEIGHT - self.LINE_HEIGHT * num_invitation -  self.FLOOR_HEIGHT/ 2 - 5  + 8], 20)
        pygame.display.flip() 
    
    # After the elevator is finished, returns the original button color , and play the ringer
    def back_to_original(self, screen, num_invitation):
        x_button_location, y_button_location = self.button
        x_num_location, y_num_location = self.number_position 
        self.change_button_color(screen, x_button_location, y_button_location, num_invitation, x_num_location, y_num_location)
        pygame.mixer.music.load("ding.mp3")
        pygame.mixer.music.play()
        pygame.display.flip() 
   
    def floor_button(self, screen, num_invitation, building):
        x_button_location, y_button_location = self.button
        pygame.draw.circle(screen, self.GREEN, [x_button_location, y_button_location], 10) 
        x_num_location, y_num_location = self.number_position 
        font = pygame.font.Font(None, 25)
        number = font.render(f"{num_invitation}", True, (self.BLACK))
        screen.blit(number, (x_num_location, y_num_location))
        floor = building.array_floors[num_invitation]
        if floor.elevator_on_the_way == False:
            floor.elevator_on_the_way = True
            building.choose_an_elevator(num_invitation, screen)
            # lift = building.array_elevators[min_index]
            # Elevator.move_elevator(self, screen, num_invitation, lift, building)

   
        
        
    






