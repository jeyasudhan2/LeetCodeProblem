def dimandPtternLeetcode(num):
      # Upperhalf
      for i in range (1,num+1):
          print(" " * (num-i) + "*" * ( 2* i - 1))
       #Downhalf
      for i in range (0,num+1):
          print(" "*i +"*"*(2 * (num-(i+1))+1))
          # print(" "*(num-i)+"*"*(2* i-1))


dimandPtternLeetcode(5)