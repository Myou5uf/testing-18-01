stroka = input("Ведите буквы без цифр (не более 100 символов):")
i = 0
while i != 1:
  if (stroka.isdigit() == False & len(stroka)<=100):
      stroka = stroka.upper()
      stroka = stroka.replace(" ","")
      m = ""
      for i in range(len(stroka)):
          for j in range(len(stroka), i, -1):
              if len(m) >= j-i:
                  break
              elif stroka[i:j] == stroka[i:j][::-1]:
                  m = stroka[i:j]
      print(m)
      i = 1
  else:
    print("Введите буквы без цифр")
    stroka = input("Ведите буквы (не более 100 символов):")