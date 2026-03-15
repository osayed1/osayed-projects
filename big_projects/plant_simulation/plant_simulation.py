import pygame as py
import math

py.init()
width, hight = 1400, 1000 
win = py.display.set_mode((width, hight))
py.display.set_caption("plant_simulation")

sun_c = (255,127,80)
earth_c = (0, 0, 255)
mercury_c = (30, 28, 28)
venus_c = (200, 200, 200)
mars_c = (255, 0, 0)
white = (255, 255, 255)

font = py.font.SysFont("comucsans", 16)

class Planet:
    Au = 149.6e6 * 1000 # وحدة فلكية محوله لي متر
    g = 6.67428e-11 # الجاذبية
    scale = 250 / Au # نحول من وحده فلكيه وحده لي 100 بكسل
    timestep = 3600 * 24 # day

    def __init__(self, x, y, radius, color, mass): # mass= كتله radius=وحدة لي قياس الدائرة 
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.scale + width / 2
        y = self.y * self.scale + hight / 2

        if len(self.orbit) > 2:
            update_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.scale + width / 2
                y = y * self.scale + hight / 2
                update_points.append((x, y))

            py.draw.lines(win, self.color, False, update_points, 2)
        py.draw.circle (win, self.color,(x, y), self.radius)

        if not self.sun:
            distance_text = font.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, white)
            win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2 + 20))


    def cal(self, other):

        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.g * other.mass * self.mass / (distance**2)

        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y
    
    def update_position(self, planets):
        totalFx = totalFy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.cal(planet)
            totalFx += fx
            totalFy += fy

        self.x_vel += totalFx / self.mass * self.timestep
        self.y_vel += totalFy / self.mass * self.timestep

        self.x += self.x_vel * self.timestep
        self.y += self.y_vel * self.timestep
        self.orbit.append((self.x, self.y))



def main():
    run = True
    clock = py.time.Clock()
    
    sun = Planet(0, 0, 30, sun_c, 1.98892 * 10**30)
    sun.sun = True

    earth = Planet(-1 * Planet.Au, 0, 16, earth_c, 5.9722 * 10**24)
    earth.y_vel = 29.783 * 1000

    mars = Planet(-1.524 * Planet.Au, 0, 12, mars_c,  6.417 * 10**23)
    mars.y_vel = 24.077 * 1000

    venus = Planet(0.723 * Planet.Au, 0, 14, venus_c, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000

    mercury = Planet(0.387 * Planet.Au, 0, 8, mercury_c, 3.3011 * 10**23)
    mercury.y_vel = -47.4 * 1000

    planets = [sun, earth, mars, venus, mercury]


    while run:
        clock.tick(60)
        win.fill((0, 0, 0))

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        for p in planets:
            p.update_position(planets)
            p.draw(win)

        py.display.update()

    py.quit()

main()