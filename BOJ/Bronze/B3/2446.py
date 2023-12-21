def print_star_recursive(n, i=0):
    if i == n:
        return

    print(' ' * i + '*' * (2 * (n - i) - 1))
    print_star_recursive(n, i+1)

    if i < n - 1:  # Avoid printing the last line twice
        print(' ' * i + '*' * (2 * (n - i) - 1))

n = int(input())
print_star_recursive(n)
