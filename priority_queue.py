import numpy as np
from math import sqrt
from queue import PriorityQueue


def box_conners_to_center(b_box):
    """
    Convert from (top_left, bottom_right) to (center, width, height).
    """
    x1, y1, x2, y2 = b_box[0], b_box[1], b_box[2], b_box[3]

    x_center = (x2 + x1) / 2
    y_center = (y2 + y1) / 2
    w = x2 - x1
    h = y2 - y1

    return np.stack((x_center, y_center, w, h), axis=-1)


def box_center_to_corners(b_box):
    """
    Convert from (center, width, height) to (top_left, bottom_right).
    """
    x_center, y_center, w, h = b_box[0], b_box[1], b_box[2], b_box[3]

    x1 = x_center - 0.5 * w
    y1 = y_center - 0.5 * h
    x2 = x_center + 0.5 * w
    y2 = y_center + 0.5 * h

    return np.array((x1, y1, x2, y2))


def euclid_distance(b_box_1, b_box_2):
    """
    Calculate the Euclid distance between 2 bounding boxes (box with centroid).
    """
    x1, y1, _, _ = b_box_1[0], b_box_1[1], b_box_1[2], b_box_1[3]
    x2, y2, _, _ = b_box_2[0], b_box_2[1], b_box_2[2], b_box_2[3]

    return round(sqrt((x2 - x1)**2 + (y2 - y1)**2), 6)


class BoundingBox:
    # def __init__(self, box_id, color, distance):
    def __init__(self, color, distance):
        # self.box_id = box_id
        self.color = color
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance

# b_box_center = [10, 20, 40, 60]
# print(box_conners_to_center(box_center_to_corners(b_box_center)) == b_box_center)

if __name__ == '__main__':

    # The image size
    # img_width, img_height = map(int, input('Input the image resolution (WxH): ').split('x'))
    img_width, img_height = 400, 600

    # n = int(input('Input number of bboxes: '))
    n = 7
    colors_set = {'red', 'blue', 'orange'}

    # Initialize the queues
    red_queue = PriorityQueue()
    blue_queue = PriorityQueue()
    orange_queue = PriorityQueue()

    # The Crane coordinates
    print('Input the Crane bbox:', end=" ")
    # crane_box = list(map(int, input().split()))
    crane_box = [200, 30, 40, 60]
    print('\nPlease input the coordinates of red, blue, orange boxes...\n')

    object_boxes = [
        ['red', (100, 50, 30, 40)], ['blue', (175, 200, 60, 40)], ['orange', (278, 200, 120, 100)], ['red', (300, 500, 40, 50)],
        ['blue', (320, 410, 80, 87)], ['orange', (240, 120, 100, 120)], ['red', (200, 100, 75, 60)]
    ]

    for box in object_boxes:
        color, offset = box[0], box[1]
        dist = euclid_distance(crane_box, list(offset))

        if color == 'red':
            red_queue.put(BoundingBox(color, dist))
        elif color == 'blue':
            blue_queue.put(BoundingBox(color, dist))
        elif color == 'orange':
            orange_queue.put(BoundingBox(color, dist))


    # i = 1

    # while True:
    #     if i > n:
    #         break
        
    #     # The color of the box
    #     print('\nInput color:', end=' ')
    #     c = input().strip()
    #     if c not in colors_set:
    #         print('Please enter valid color!')
    #         continue
        
    #     try:
    #         print(f'The object bbox {i}:', end=" ")
    #         x, y, w, h = map(int, input().split())
    #     except ValueError:
    #         print('Please input correct coordinates!... \n')
    #         continue
        
    #     if  0 > x > img_width or 0 > y > img_height or w > img_width or h > img_height:
    #         print(f'You entered invalid coordinates, please enter correct value in range of ({img_width}, {img_height}!')
    #         continue
        
        # dist = euclid_distance(crane_box, [x, y, w, h])

        # if c == 'red':
        #     red_queue.put(BoundingBox(c, dist))
        # elif c == 'blue':
        #     blue_queue.put(BoundingBox(c, dist))
        # elif c == 'orange':
        #     orange_queue.put(BoundingBox(c, dist))

    #     i += 1

    print('Red queue:', len(red_queue.queue))
    print('Blue queue:', len(blue_queue.queue))
    print('Orange queue:', len(orange_queue.queue))

    for i in range(red_queue.qsize()):
        print(red_queue.get().distance)

