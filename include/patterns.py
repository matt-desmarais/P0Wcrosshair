import cv2
import numpy as np

# number of available patterns:
maxpat = 10

# defining functions for all possible patterns follow, 
# activated by patternswitch function

# pattern1: Bruker style crosshair with circles and ticks
def pattern1( arr, width, height, x, y, rad, col ):
    cv2.line(arr,(0,y),(width,y),col,1)
    cv2.line(arr,(x,0),(x,height),col,1)
    i = 0
    for i in range(1, 8): 
        cv2.circle(arr,(x,y),i*rad,col,1)
        i += 1
    # ticks on the horizontal axis:
    intervalh = np.arange(0,width,float(rad)/10)
    j = 0
    for i in intervalh:
        # make every 5th tick longer, omit every 10th tick:
        diff = int(round(i))
        if j%5 == 0:    
            if not j%10 == 0:
                cv2.line(arr,(x+diff,y-4),(x+diff,y+4),col,1)
                cv2.line(arr,(x-diff,y-4),(x-diff,y+4),col,1)
        else:
            cv2.line(arr,(x+diff,y-2),(x+diff,y+3),col,1)
            cv2.line(arr,(x-diff,y-2),(x-diff,y+3),col,1)
        j += 1
    # ticks on the vertical axis:
    intervalv = np.arange(0,height,float(rad)/10)
    l = 0
    for k in intervalv:
        # make every 5th and 10th tick longer:
        diff = int(round(k))
        if l%5 == 0:    
            if l%10 == 0:
                cv2.line(arr,(x-6,y+diff),(x+6,y+diff),col,1)
                cv2.line(arr,(x-6,y-diff),(x+6,y-diff),col,1)
            else:
                cv2.line(arr,(x-4,y+diff),(x+4,y+diff),col,1)
                cv2.line(arr,(x-4,y-diff),(x+4,y-diff),col,1)
        else:
            cv2.line(arr,(x-2,y+diff),(x+2,y+diff),col,1)
            cv2.line(arr,(x-2,y-diff),(x+2,y-diff),col,1)
        l += 1
    return    

# pattern2: simple crosshair with ticks
def pattern2( arr, width, height, x, y, rad, col ):
    # cv2.circle(arr,(x,y),rad,col,1)
    cv2.line(arr,(0,y),(width,y),col,1)
    cv2.line(arr,(x,0),(x,height),col,1)
    # ticks on the horizontal axis:
    intervalh = np.arange(0,width,float(rad)/10)
    j = 0
    for i in intervalh:
        # make every 5th and 10th tick longer:
        diff = int(round(i))
        if j%5 == 0:    
            if j%10 == 0:
                cv2.line(arr,(x+diff,y-6),(x+diff,y+6),col,1)
                cv2.line(arr,(x-diff,y-6),(x-diff,y+6),col,1)
            else:
                cv2.line(arr,(x+diff,y-4),(x+diff,y+4),col,1)
                cv2.line(arr,(x-diff,y-4),(x-diff,y+4),col,1)
        else:
            cv2.line(arr,(x+diff,y-2),(x+diff,y+3),col,1)
            cv2.line(arr,(x-diff,y-2),(x-diff,y+3),col,1)
        j += 1
    # ticks on the vertical axis:
    intervalv = np.arange(0,height,float(rad)/10)
    l = 0
    for k in intervalv:
        # make every 5th and 10th tick longer:
        diff = int(round(k))
        if l%5 == 0:    
            if l%10 == 0:
                cv2.line(arr,(x-6,y+diff),(x+6,y+diff),col,1)
                cv2.line(arr,(x-6,y-diff),(x+6,y-diff),col,1)
            else:
                cv2.line(arr,(x-4,y+diff),(x+4,y+diff),col,1)
                cv2.line(arr,(x-4,y-diff),(x+4,y-diff),col,1)
        else:
            cv2.line(arr,(x-2,y+diff),(x+2,y+diff),col,1)
            cv2.line(arr,(x-2,y-diff),(x+2,y-diff),col,1)
        l += 1
    return    

# pattern3: simple crosshair without ticks
def pattern3( arr, width, height, x, y, rad, col ):
    cv2.line(arr,(0,y),(width,y),col,1)
    cv2.line(arr,(x,0),(x,height),col,1)
    return    

# pattern4: simple crosshair with circles (no ticks)
def pattern4( arr, width, height, x, y, rad, col ):
    cv2.line(arr,(0,y),(width,y),col,1)
    cv2.line(arr,(x,0),(x,height),col,1)
    i = 0
    for i in range(1, 8): 
        cv2.circle(arr,(x,y),i*rad,col,1)
        i += 1
    return    

# pattern5: simple crosshair with one circle (no ticks)
def pattern5( arr, width, height, x, y, rad, col ):
    cv2.line(arr,(0,y),(width,y),col,2)
    cv2.line(arr,(x,0),(x,height),col,2)
    cv2.circle(arr,(x,y),rad,col,2)
    return    

# pattern6: simple circle
def pattern6( arr, width, height, x, y, rad, col ):
    cv2.circle(arr,(x,y),rad,col,1)
    return

# pattern7: small center crosshair
def pattern7( arr, width, height, x, y, rad, col ):
    cv2.line(arr,(x-10,y),(x+10,y),col,1)
    cv2.line(arr,(x,y-10),(x,y+10),col,1)
    return

# pattern8: small center crosshair without center
def pattern8( arr, width, height, x, y, rad, col ):
    cv2.line(arr,(x-10,y),(x-3,y),col,1)
    cv2.line(arr,(x,y-10),(x,y-3),col,1)
    cv2.line(arr,(x+3,y),(x+10,y),col,1)
    cv2.line(arr,(x,y+3),(x,y+10),col,1)
    return

# pattern9: only a dot
def pattern9( arr, width, height, x, y, rad, col ):
    cv2.circle(arr,(x,y),2,col,-1)
    return

# pattern10: grid
def pattern10( arr, width, height, x, y, rad, col ):
    # center lines:
    cv2.line(arr,(0,y),(width,y),col,1)
    cv2.line(arr,(x,0),(x,height),col,1)
    i = rad
    j = rad
    # horizontal lines:
    while i < height:
        cv2.line(arr,(0,y+i),(width,y+i),col,1)
        cv2.line(arr,(0,y-i),(width,y-i),col,1)
        i += rad
    # vertical lines:
    while j < width:
        cv2.line(arr,(x+j,0),(x+j,height),col,1)
        cv2.line(arr,(x-j,0),(x-j,height),col,1)
        j += rad
    return
