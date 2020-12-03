from objetos_midia import Filme, Serie

def main():
    filme1 = Filme("Os Trapalhões e o Rei do Futebol", 1986, 74.0, 10000000)
    serie1 = Serie("Dr House", 2002, 8, 80000)
    serie2 = Serie("The walking dead", 2004, 9, -12)
    serie3 = Serie("Fear the walking dead", 2005, 1, -13)
    serie4 = Serie("The walking dead: um novo universo", 2007, 3, 0)
    serie2.add_spinoff(serie3)
    serie2.add_spinoff(serie4)

    print(filme1)
    for i in range(1, 5):
        print(eval(f'serie{i}'))
    print('-='*30)
    print('the walking dead possui spinoff ?')
    serie2.has_spinoffs()
    print('-='*30)
    print('dr house possui sinoff ?')
    serie1.has_spinoffs()
    print('-='*30)


if __name__ == '__main__':
    main()