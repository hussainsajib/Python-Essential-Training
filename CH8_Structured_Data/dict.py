#!/usr/bin/env python3

def main():
    animals = { 'kitten': 'meow', 'puppy': 'ruff', 'lion': 'grrr',
                'giraffe': 'I am giraffe', 'dragon': 'rawr'}
    animalsAlt = dict(kitten='meow', puppy='ruff', lion='grrr',
                    giraffe='I am giraffe', dragon='rawr')
    print_dict(animals)
    print_dict(animalsAlt)

def print_dict(o):
    for x in o:
        print(f'{x}: {o[x]}')

if __name__ == "__main__":
    main()