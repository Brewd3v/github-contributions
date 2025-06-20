import random
import subprocess


def update_counter():
    with open("counter.txt", "r+") as f:
        contents = f.read()
        counter = 0

        if contents:
            counter = int(contents) + 1

        f.seek(0)
        f.write(str(counter))
        f.truncate()


def add_commit(index, repeat_times):
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f"'Updating counter {index + 1}/{repeat_times}.'"])
    subprocess.run(["git", "push", "origin", "main"])


repeat_times = random.randint(1, 10)

print(f"Repeating: {repeat_times}")

for i in range(0, repeat_times):
    update_counter()
    add_commit(i, repeat_times)
