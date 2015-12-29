import sys
from random import choice


def comprobar(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def main():
    caracteres = ['abcdefghijklmnopqrstuvwxyz',
                  '0123456789',
                  'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                  ]
    # caracter = choice(caracteres)
    password = []

    if comprobar(sys.argv[1]):
        longitud = int(sys.argv[1])
    else:
        sys.exit('La longitud debe de ser un caracter numerico')

    if len(sys.argv) == 3 and str.upper(sys.argv[2]) == 'NO':
        print('Modo: Sin repeticion de caracteres')
        while len(password) < longitud:
            caracter = choice(choice(caracteres))
            if caracter in password:
                # print('existe' + ' ' + caracter)
                continue
            else:
                password.append(caracter)
                print(password)
                # caracter = choice(list(set(caracteres) - {caracter}))

    else:
        print('Modo: Con repeticion de caracteres')
        while len(password) < longitud:
            caracter = choice(caracteres)
            password.append(choice(caracter))

    return ''.join(password)


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        sys.exit('Uso: pass.py <longitud> [si/no -> Por defecto si]')

    print(main())