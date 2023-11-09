while True:
    try:
        print(input())
    except EOFError: # 그냥 except만 써도 됨
        break
