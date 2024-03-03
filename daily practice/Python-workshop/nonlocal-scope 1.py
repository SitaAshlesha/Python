def outer_function():
    y = 5
    def inner_fun():
      nonlocal y
    y += 10
    inner_fun()
    print(y)
outer_function()