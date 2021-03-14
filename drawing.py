import matplotlib.pyplot as plt
from PIL import Image, ImageDraw 
import numpy as np

class Drawing:
    def __init__(self, lineColor):
        self.image = Image.open('image.jpg')
        self.width, self.height = self.image.size[0], self.image.size[1]
        self.draw = ImageDraw.Draw(self.image)
        self.lineColor = lineColor

    def show_image(self):
        plt.imshow(self.image)
        plt.show()

    def save_image(self):
        img = self.image
        img = img.save("new_image.jpg")

    def draw_line(self, x1, y1, x2, y2):

        dx = x2 - x1
        dy = y2 - y1
            
        sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
        sign_y = 1 if dy > 0 else -1 if dy < 0 else 0
            
        if dx < 0: dx = -dx
        if dy < 0: dy = -dy
            
        if dx > dy:
            pdx, pdy = sign_x, 0
            es, el = dy, dx
        else:
            pdx, pdy = 0, sign_y
            es, el = dx, dy
            
            x, y = x1, y1
            
            error, t = el / 2, 0        
            
            self.draw.point((x, y), fill = self.lineColor)
            
            while t < el:
                error -= es
                if error < 0:
                    error += el
                    x += sign_x
                    y += sign_y
                else:
                    x += pdx
                    y += pdy
                t += 1
                self.draw.point((x, y), fill = self.lineColor) 
                

    def draw_circle(self, x, y, r):    
        
        disp_x = x
        disp_y = y
        x = 0
        y = r
        delta = (1 - 2 * r)
        error = 0

        while y >= 0:
            self.draw.point((disp_x + x, disp_y + y), fill = self.lineColor)
            self.draw.point((disp_x + x, disp_y - y), fill = self.lineColor)
            self.draw.point((disp_x - x, disp_y + y), fill = self.lineColor)
            self.draw.point((disp_x - x, disp_y - y), fill = self.lineColor)
            
            error = 2 * (delta + y) - 1
            if ((delta < 0) and (error <= 0)):
                x += 1
                delta = delta + (2 * x + 1)
                continue
            error = 2 * (delta - x) - 1
            if ((delta > 0) and (error > 0)):
                y -= 1
                delta = delta + (1 - 2 * y)
                continue
            x += 1
            delta = delta + (2 * (x - y))
            y -= 1


    def draw_ellipse(self, x0, y0, x1, y1):

        a = np.abs(x1 - x0) 
        b = np.abs(y1 - y0) 
        b1 = b&1 
        dx = 4 * (1 - a) * b * b
        dy = 4 * (b1 + 1) * a * a 
        err = dx + dy + b1 * a * a

        if (x0 > x1):
            x0 = x1 
            x1 += a 
        if (y0 > y1):
            y0 = y1
        y0 += (b + 1) / 2 
        y1 = y0 - b1
        a *= 8 * a 
        b1 = 8* b* b

        while(x0 <= x1):

            self.draw.point((x1, y0), fill = self.lineColor)
            self.draw.point((x0, y0), fill = self.lineColor)
            self.draw.point((x0, y1), fill = self.lineColor)
            self.draw.point((x1, y1), fill = self.lineColor)
            e2 = 2*err;

            if (e2 <= dy):
                y0 = y0 + 1
                y1 = y1 - 1
                err += dy
                dy += a
            if (e2 >= dx or 2 * err > dy):
                x0 = x0 + 1
                x1 = x1 - 1
                err += dx 
                dx += b1

    
        while (y0 - y1 < b): 
            self.draw.point((x0 - 1, y0), fill = self.lineColor)
            self.draw.point((x1 + 1, y0 + 1), fill = self.lineColor)
            self.draw.point((x0 - 1, y1), fill = self.lineColor)
            self.draw.point((x1 + 1, y1 - 1), fill = self.lineColor)  

def main():
    color = (255,3,2,128)
    drawer = Drawing(color)
    drawer.draw_line(50, 50, 250, 250)
    drawer.draw_circle(drawer.width / 2, drawer.height / 2, 125)
    drawer.draw_ellipse(10, 50, 290, 250)   
    drawer.save_image()  
    drawer.show_image()     
        
if __name__ == '__main__':
    main()