nomreb = int(input("Enter your birth year: "))
blargh = "Your Chinese Zodiac Sign is: "
rat = "Rat (鼠 / Shǔ)"
ox = "Ox (牛 / Niú)"
tiger = "Tiger (虎 / Hǔ)"
rabbit = "Rabbit (兔 / Tù)"
dragon = "Dragon (龙 / Lóng)"
snake = "Snake (蛇 / Shé)"
horse = "Horse (马 / Mǎ)"
goat = "Goat (羊 / Yáng)"
monkey = "Monkey (猴 / Hóu)"
rooster = "Rooster (鸡 / Jī)"
dog = "Dog (狗 / Gǒu)"
pig = "Pig (猪 / Zhū)"

if nomreb < 1900:
  print("Invalid Year, it should not be earlier than 1900")
elif nomreb >= 1900:
  bermon = normeb - 1900
  if bermon % 12 = 0:
    print(blargh, rat)
  elif bermon % 12 = 1:
    print(blargh, ox)
  elif bermon % 12 = 2:
    print(blargh, tiger)
  elif bermon % 12 = 3:
    print(blargh, rabbit)
  elif bermon % 12 = 4:
    print(blargh, dragon)
  elif bermon % 12 = 5:
    print(blargh, snake)
  elif bermon % 12 = 6:
    print(blargh, horse)
  elif bermon % 12 = 7:
    print(blargh, goat)
  elif bermon % 12 = 8:
    print(blargh, monkey)
  elif bermon % 12 = 9:
    print(blargh, rooster)
  elif bermon % 12 = 10:
    print(blargh, dog)
  elif bermon % 12 = 11:
    print(blargh, pig)
