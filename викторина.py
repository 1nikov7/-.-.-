c = 0
b = 0
a = 1
def ABOBA(a):
    while a != 2:
        a = int(input('варианты действий: \n1)пройти викторину ещё раз \n2)закончить викторину \n выберите вариант из предложенного списка и напишите его цифру:'))
        if a == 1:
            f(c,b,a)
            return
        elif a == 2:
            return
def f(c,b,a):
    print('добро пожаловать в викторину по триганометрии. \n вам будет предложено несколько вопросов с вариантами ответов, вам нужно будет выбрать единственно верный ответ')
    c = int(input('чему равен синус двойного угла? \n1)sin2A = 2sinAcosA \n2)sin2A = 1 - 2sin^2(A) \n3)sin2A = 2cos^2(A) - 1 \n выберете из списка цифру с верным ответом:'))
    if c == 1:
        b += 1
        print('верно!')
    else:
        print('неверно(')
    c = int(input('чему равен kосинус двойного угла? \n1)cos2A = 2sinAcosA \n2)cos2A = 1 - 2sin^2(A) \n3)cos2A = 2cos^2(A) - 1 \n выберете из списка цифру с верным ответом:'))
    if c == 2 or c ==3:
        b+=1
        print('верно!')
    else:
        print('неверно(')
    c = int(input('какая формула понижения степени для tg^2(A)? \n1)(1 - cos2A)%2 \n2) (1+cos2A)%2 \n3)(1 - cos2A)%(1 + cos2A) \n4) (1 + cos2A)%(1 - cos2A) \n выберете из списка цифру с верным ответом:'))
    if c == 3:
        b+=1
        print('верно!')
    else:
        print('неверно(')
    c = int(input('какая формула понижения степени для ctg^2(A)? \n1)(1 - cos2A)%2 \n2) (1+cos2A)%2 \n3)(1 - cos2A)%(1 + cos2A) \n4) (1 + cos2A)%(1 - cos2A) \n выберете из списка цифру с верным ответом:'))
    if c == 4:
        b+=1
        print('верно!')
    else:
        print('неверно(')
    c = int(input('какая формула понижения степени для sin^2(A)? \n1)(1 - cos2A)%2 \n2) (1+cos2A)%2 \n3)(1 - cos2A)%(1 + cos2A) \n4) (1 + cos2A)%(1 - cos2A) \n выберете из списка цифру с верным ответом:'))
    if c == 1:
        b+=1
        print('верно!')
    else:
        print('неверно(')
    c = int(input('какая формула понижения степени для cos^2(A)? \n1)(1 - cos2A)%2 \n2) (1+cos2A)%2 \n3)(1 - cos2A)%(1 + cos2A) \n4) (1 + cos2A)%(1 - cos2A) \n выберете из списка цифру с верным ответом:'))
    if c == 2:
        b+=1
        print('верно!')
    else:
        print('неверно(')
    print(f'вы закончили викторину по триганометрии, ваш результат: {b}/6')
    b = 0
    а = 0
    ABOBA(a)
    
f(c,b,a)


