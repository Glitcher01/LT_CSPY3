def func14_1(xs, ys, mode = 0):
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

print(col_clashes([0, 1], 1))