lines = [
    "hello i am aman raturi\n",
    "i lived in mohali punjab\n",
    "i worked in talentelgia\n"
]

with open("aman.txt", "w") as file:
    file.writelines(lines)
    print("Content added successfully!!")