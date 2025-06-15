import cv2
import math

# Load the background image
img = cv2.imread('replacement.jpg')
temp = img.copy()
points = []

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(temp, (x, y), 5, (0,255,0), -1)
        cv2.imshow('image', temp)
        points.append((x, y))
        print(f"Point {len(points)}: ({x}, {y})")
        if len(points) == 2:
            cv2.destroyAllWindows()

print("Click on: (1) the base of the object; (2) the tip of its shadow")
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()

if len(points) < 2:
    print("You must select two points!")
    exit()

object_base = points[0]
shadow_tip = points[1]

# Calculate shadow (light) direction vector in image plane
light_dir_x = shadow_tip[0] - object_base[0]
light_dir_y = shadow_tip[1] - object_base[1]

# Direction angle (with respect to image x-axis)
angle_rad = math.atan2(light_dir_y, light_dir_x)
angle_deg = math.degrees(angle_rad)
print(f"\nLight (shadow) direction angle in image plane: {angle_deg:.2f} degrees")

# Shadow length in pixels
shadow_length_px = math.sqrt(light_dir_x**2 + light_dir_y**2)
print(f"Shadow length (in pixels): {shadow_length_px:.1f}")

# Estimate elevation angle if object height in pixels is known
response = input("\nDo you know the object HEIGHT in pixels? (y/n): ").strip().lower()
if response == 'y':
    object_height_px = float(input("Enter the object's height in pixels: "))
    elevation_rad = math.atan2(object_height_px, shadow_length_px)
    elevation_deg = math.degrees(elevation_rad)
    print(f"Estimated light (sun/lamps) elevation angle: {elevation_deg:.2f} degrees above ground")
else:
    print("Skipped elevation calculation (need object height in pixels)")