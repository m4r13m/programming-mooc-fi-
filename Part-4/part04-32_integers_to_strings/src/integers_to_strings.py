def formatted(l):
    f_l = []
    for n in l:
        f_l.append(f"{n:.2f}")
    return f_l


if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)