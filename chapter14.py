import random


def merge(xs, ys, mode=0):
    if mode == 0:
        result = []
        xi = yi = 0
        xs.sort()
        ys.sort()
        xs, ys = rem_adj_dup(xs), rem_adj_dup(ys)
        while True:
            if xi >= len(xs):
                result.extend(ys[yi:])
                return result

            if yi >= len(ys):
                result.extend(xs[xi:])
                return result

            if xs[xi] < ys[yi]:
                result.append(xs[xi])
                xi += 1

            elif ys[yi] < xs[xi]:
                result.append(ys[yi])
                yi += 1

            else:
                result.append(xs[xi])
                xi, yi = xi + 1, yi + 1
    if mode == 1:
        result = []
        for i in xs:
            if i not in ys:
                result.append(i)
        return result
    if mode == 2:
        result = []
        for i in ys:
            if i not in xs:
                result.append(i)
        return result
    if mode == 3:
        result = xs + ys
        result.sort()
        return rem_adj_dup(result)


def rem_adj_dup(list):
    last_value = None
    result = []
    for i in list:
        if i != last_value:
            result.append(i)
            last_value = i
    return result


def share_diagonal(x0, y0, x1, y1):
    dy = abs(y0 - y1)
    dx = abs(x0 - x1)
    return dy == dx


def col_clashes(bs, c):
    for i in range(c):
        if share_diagonal(i, bs[i], c, bs[c]):
            return True
    return False


def has_clashes(board):
    for col in range(1, len(board)):
        if col_clashes(board, col):
            return True
    return False


def mirror_y(list):
    result = []
    for i in range(len(list) - 1, -1, -1):
        result.append(list[i])
    return result


def mirror_x(list):
    result = []
    for i in range(len(list)):
        result.append(abs(list[i] + 1 - len(list)))
    return result


def turn90(list):
    result = [None] * len(list)
    for (i, v) in enumerate(list):
        result[abs(v + 1 - len(list))] = i
    return result


def turn180(list):
    result = [None] * len(list)
    for (i, v) in enumerate(list):
        result[abs(i + 1 - len(list))] = abs(v + 1 - len(list))
    return result


def turn270(list):
    result = [None] * len(list)
    for (i, v) in enumerate(list):
        result[v] = abs(i + 1 - len(list))
    return result


def family(list):
    return [list, turn270(list),
            turn180(list), turn90(list),
            mirror_y(list), mirror_y(turn90(list)),
            mirror_x(list), mirror_x(turn90(list))]


def queens_puzzle(board_size=8, solutions=10):
    rng = random.Random()
    bd = list(range(board_size))
    found = []
    dup = []
    tries = 0
    while len(found) < solutions:
        ba = rng.sample(bd, len(bd))
        tries += 1
        if not has_clashes(ba) and ba not in found and ba not in dup:
            print("Found solution {0} in {1} tries.".format(ba, tries))
            tries = 0
            found.append(ba)
            dup += family(ba)


def sieve(list):
    result = [x for x in list if x >= 2 and type(x) == int]
    i = 2
    while i * i <= max(result):
        if result[i] == 0:
            i += 1
            continue

        j = 2 * i
        while j < max(result):
            result[:] = [y for y in result if y != j]
            j += i

        i += 1
    return result


def lotto_draw():
    return random.sample(sieve(list(range(50))), 6)


def lotto_match(jackpot, draw):
    return len([i for i in draw if i in jackpot])


def lotto_matches(jackpot, draws):
    result = []
    for draw in draws:
        result.append(lotto_match(jackpot, draw))
    return result


def primes_in(list):
    return len(sieve(list))


def prime_misses(draws):
    prime_in = []
    for i in draws:
        prime_in += i
    prime_in.sort()
    prime_ins = rem_adj_dup(prime_in)
    return [x for x in sieve(list(range(50))) if x not in prime_ins]
