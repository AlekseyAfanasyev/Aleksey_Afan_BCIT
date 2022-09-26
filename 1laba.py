import sys
import math
import random

def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except:

        print(prompt)
        coef_str = input()
    if not coef_str.isalpha():
        coef = float(coef_str)
    else:
        print("Коэффициент задан некорректно. Он будет задан случайно от 1 до 10")
        coef = random.randint(1,10)
        print(coef)
    return coef


def get_roots(a, b, c):
    result = []
    if a ==0:
        print("Коэффициент А задан некорректно. Он будет задан случайно от 1 до 10")
        a=random.randint(1,10)
    D=b*b-4*a*c
    if D==0.0:
        t=-b/(2.0*a)
        if t>=0:
            x1 = math.sqrt(t)
            x2=-math.sqrt(t)
            result.append(x1)
            if x1 !=0:
                result.append(x2)
    elif D >0.0:
        t1 = (-b+math.sqrt(D))/(2.0*a)
        if t1 > 0.0:
            x1=math.sqrt(t1)
            x2=-math.sqrt(t1)
            result.append(x1)
            result.append(x2)
        elif t1==0:
            result.append(t1)

        t2=(-b-math.sqrt(D))/(2.0*a)
        if t2 > 0.0:
            x3 = math.sqrt(t1)
            x4 = -math.sqrt(t1)
            result.append(x3)
            result.append(x4)
        elif (t2 ==0) and (t2!=t1):
            result.append(t2)
    return result


def main():

    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')

    roots = get_roots(a, b, c)

    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}; {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 2:
        print('Четыре корня: {}; {};'
              ' {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))

if __name__ == "__main__":
    main()
