def clenwold(wold):

    if len(wold) == 1:
        return wold

    print(f"stat function {wold}")

    if wold[0] == wold[1]:
        print(f"stat before condition {wold}")
        return clenwold(wold[1:])
    print(f"stat before return {wold}")
    return wold[0] + clenwold(wold[1:])


print(clenwold("wwwwwooooolddd"))
