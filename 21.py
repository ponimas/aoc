#!/usr/bin/env python3


numeric = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]

moves = {"^": -1 + 0j, "v": 1 + 0j, "<": -1j, ">": 1j}
start = 3 + 2j


def ngbrs(p: complex, keypad):
    ngbr = []
    for d, delta in moves.items():
        n = p + delta
        if (
            n.real < 0
            or n.real >= len(keypad)
            or n.imag < 0
            or n.imag >= len(keypad[0])
            or keypad[n.real][n.imag] is None
        ):
            continue
        ngbr.append((d, n))
    return


def move(start, dest, keypad):
    pass
