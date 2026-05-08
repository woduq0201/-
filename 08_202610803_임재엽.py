bus_seat = ['구백년',"서교수","김수뭉"]
bus_line = ["이사슴","박밀레","최자하"]

print("탑승 인원 : ", bus_seat)
print("대기 인원 : ", bus_line)
print()

for i in range(1,4):
    del(bus_seat[0])
    bus_seat.append(bus_line[0])
    del(bus_line[0])
    print("탑승 인원 : ", bus_seat)
    print("대기 인원 : ", bus_line)
    print()
    



