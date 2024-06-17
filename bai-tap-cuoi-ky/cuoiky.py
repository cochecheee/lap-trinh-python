import math

def cau1_recursion(x, y, i, count, bound):
    # Update bound
    bound = min(len(x), len(y))
    # Base case: return the count when index i reaches the bound
    if i == bound:
        return count + abs(len(x) - len(y))
    # If characters at index i are different, increment count
    if x[i] != y[i]:
        count += 1 
    # Recursive call with incremented index i
    return cau1_recursion(x, y, i + 1, count, bound)

s1 = 'kitten'
s2 = 'sitting'
c = cau1_recursion(s1, s2, 0, 0, 0)
print(c)

# Tính khoảng cách Euclid giữa 2 điểm p1 và p2
import numpy as np
p = 121
p1 = np.array((1, 1, 1))
p2 = np.array((1, 2, 3))
print(np.sqrt(p))
print(np.dot(p1,p2))
print(np.square(p1-p2))
kc = np.sqrt(np.sum(np.square(p1-p2)))
print(kc)

#tích các thừa số nguyên tố
def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors

def product_of_unique_prime_factors(n):
    prime_factors_list = prime_factors(n)
    unique_prime_factors = list(set(prime_factors_list))
    product = 1
    for factor in unique_prime_factors:
        product *= factor
    return product

# Ví dụ sử dụng
number = int(input("Nhập số nguyên: "))
result = product_of_unique_prime_factors(number)
print(f"Tích các thừa số nguyên tố duy nhất của {number} là: {result}")


# câu 3
# Đếm số chuỗi con trong một mảng chuỗi
import numpy as np
iarr = np.array(['Teyenten', ' Teyen ', 'Teyenqubhre'])
oarr = np.char.count(iarr,sub='en')
print(oarr)
arr = np.char.count(iarr,sub='e',start=0,end=7)
print(arr)

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2*np.pi, 2*np.pi, 0.01)
y = np.sin(3*x)/x
y2 = np.sin(2*x)/x
y3 = np.sin(x)/x


plt.plot(x, y, color='blue')
plt.plot(x, y2, color='red')
plt.plot(x, y3, color='green')

plt.axhline(y=0, color='black')  # Thêm đường gạch ngang tại y=0
plt.axvline(x=0, color='black')  # Thêm đường gạch dọc tại x=0

plt.legend()  # Hiển thị chú thích đường cong

plt.annotate('+3', xy=(0.05, 3), xytext=(0.1, 2.8))
plt.annotate('+2', xy=(0.05, 2), xytext=(0.1, 1.8))
plt.annotate('+1', xy=(0.05, 1), xytext=(0.1, 0.8))
plt.annotate('-1', xy=(0.05, -1), xytext=(0.1, -1.2))

plt.annotate('-2$\pi$', xy=(-2*np.pi, -0.1), xytext=(-6.5, -0.3))
plt.annotate('-$\pi$', xy=(-np.pi, -0.1), xytext=(-3.2, -0.3))
plt.annotate('0', xy=(0, -0.1), xytext=(0, -0.3))
plt.annotate('$\pi$', xy=(np.pi, -0.1), xytext=(3.2, -0.3))
plt.annotate('2$\pi$', xy=(2*np.pi, -0.1), xytext=(6.5, -0.3))

plt.box(False)

plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2*np.pi, 2*np.pi, 0.01)
y = np.sin(3*x)/x
y2 = np.sin(2*x)/x
y3 = np.sin(x)/x


plt.plot(x, y, color='blue')
plt.plot(x, y2, color='red')
plt.plot(x, y3, color='green')

plt.axhline(y=0, color='black')  # Thêm đường gạch ngang tại y=0
plt.axvline(x=0, color='black')  # Thêm đường gạch dọc tại x=0

plt.legend()  # Hiển thị chú thích đường cong

plt.annotate('+3', xy=(-0.9, 3))
plt.annotate('+2', xy=(-0.9, 2))
plt.annotate('+1', xy=(-0.9, 1))
plt.annotate('0', xy=(-0.9,0))
plt.annotate('-1', xy=(-0.9, -1))

plt.annotate('-2$\pi$', xy=(-2*np.pi, -0.9))
plt.annotate('-$\pi$', xy=(-np.pi, -0.9))
plt.annotate('0', xy=(0, -0/9))
plt.annotate('$\pi$', xy=(np.pi, -0.9))
plt.annotate('2$\pi$', xy=(2*np.pi, -0.9))


plt.show()

import matplotlib.pyplot as plt
import numpy as np

#data 1
x1 = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y1 = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
#data 2
x2 = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
y2 = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])

#create colors and size for spot
sizes1 = []
sizes2 = []
colors1 = []
colors2 = []
for y in y1:
    if 100 <= y <= 115:
        sizes1.append(300)
        colors1.append("crimson")
    elif 90 <= y < 100:
        sizes1.append(250)
        colors1.append("red")
    elif 80 < y < 90:
        sizes1.append(160)
        colors1.append("salmon")
    else:
        sizes1.append(100)
        colors1.append("mistyrose")
for y in y2:
    if 100 < y <= 115:
        sizes2.append(300)
        colors2.append("mediumblue")
    elif 90 < y <= 100:
        sizes2.append(250)
        colors2.append("blue")
    elif 80 < y <= 90:
        sizes2.append(160)
        colors2.append("dodgerblue") #deepskyblue
    else:
        sizes2.append(100)
        colors2.append("skyblue")
#scatter plot for data 1
plt.scatter(x1, y1, s=sizes1, color=colors1, label='(4 brightness levels): Dữ liệu 1')
#scatter plot for data 2
plt.scatter(x2, y2, s=sizes2, color=colors2, label='(4 brightness levels): Dữ liệu 2')
#title
plt.xlabel('Tọa độ X')
plt.ylabel('Tọa độ Y')
plt.title('ĐỒ THỊ SCATTER')
#range for xaxis and yxis
x_ticks = np.arange(0.0, 18.0, 2.5)
plt.xticks(x_ticks)
plt.xlim(-0.2, 17.8)
plt.ylim(75.1, 115)
#(-. style)
plt.grid(axis='y', linestyle='-.')
#label
plt.legend(fontsize=12)
#show
plt.show()
