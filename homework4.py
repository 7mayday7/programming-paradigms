from functools import reduce


def mean(values):
    return sum(values) / len(values)


def pearson_correlation(x, y):
    mean_x, mean_y = mean(x), mean(y)
    deviations_x = [xi - mean_x for xi in x]
    deviations_y = [yi - mean_y for yi in y]

    numerator = sum(map(lambda xi, yi: xi * yi, deviations_x, deviations_y))
    denominator = reduce(lambda acc, xi_yi: acc + xi_yi, map(lambda xi, yi: xi * yi, deviations_x, deviations_y))

    return numerator / denominator


if __name__ == "__main__":
    array1 = [6, 1, 6, 1, 6]
    array2 = [0, 6, 0, 6, 0]

    correlation = pearson_correlation(array1, array2)
    print(f"Корреляция Пирсона: {correlation}")
