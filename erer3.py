print()
base = float(input("รับค่าฐาน: "))
height = float(input("รับค่าความสูง: "))
triangle_area = 0.5 * base * height
print("เเสดงพื้นที่สามเหลี่ยม")
print(f"{triangle_area:.6f}")
print()

print()
C = float(input("กรอกค่าอุณหภูมิ (องศาเซลเซียส): "))
F = (9/5) * C + 32
K = C + 273.15
print(f"อุณหภูมิในหน่วยฟาเรนไฮต์: {F:.2f} °F")
print(f"อุณหภูมิในหน่วยเคลวิน: {K:.2f} K")
print()

a = {10, 20, 30, 40, 50, 60}
b = {30, 40, 50, 60, 70, 80}
result1 = a.union(b)
result2 = a.intersection(b)
result3 = a.difference(b)
result4 = a.symmetric_difference(b)
print()
import time
time.sleep(.5)
print(result1)
print(result2)  
print(result3)  
print(result4)  
