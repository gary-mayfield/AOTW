def TowerOfHanoi(n, source, destination, auxillary):
    if n == 1:
        print(f"Move disk 1 from source {source} to destination {destination}")
        return
    TowerOfHanoi(n - 1, source, auxillary, destination)
    print(f"Move disk {n} from source {source} to destination {destination}")
    TowerOfHanoi(n - 1, auxillary, destination, source)

n = 4
TowerOfHanoi(n, "Start", "End", "Middle")