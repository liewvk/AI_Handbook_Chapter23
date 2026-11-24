results = [True, True, False, True, True,
           True, False, True, True, True]
successful = sum(results)
rate = successful / len(results)
print(f"Completed: {successful}/{len(results)}")
print(f"Success rate: {rate:.0%}")

