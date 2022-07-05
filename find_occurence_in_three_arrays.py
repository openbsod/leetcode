"""
https://github.com/Tinkoff/career/blob/main/interview/sections/programming-basic.md

Даны три неубывающих массива чисел. Найти число, которое присутствует во всех трех массивах.

Input: [1,2,4,5], [3,3,4], [2,3,4,5,6]
Output: 4

foreach(var v in x y z) {
  if (x.contains(v) && y.contains(v) && z.contains(v) return v;
}
"""


def find_d(a, b, c):
    for i in a:
        for j in b:
            for k in c:
                if i == j == k:
                    d.append(i)


a = [1, 2, 4, 5]
b = [3, 3, 4]
c = [2, 3, 4, 5, 6]
d = []


find_d(a, b, c)
if len(d) > 0:
    print(d)
else:
    print("No occurrence")
