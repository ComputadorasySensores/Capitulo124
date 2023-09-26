from machine import I2C, Pin 
import ssd1306
from imu import MPU6050
from time import sleep

i2c = I2C(0, scl=Pin(5), sda=Pin(4))

oled_ancho = 128
oled_alto = 64
oled = ssd1306.SSD1306_I2C(oled_ancho, oled_alto, i2c)

imu = MPU6050(i2c)

while True:
  ax = imu.accel.x
  ay = imu.accel.y
  az = imu.accel.z
  gx = imu.gyro.x
  gy = imu.gyro.y
  gz = imu.gyro.z
  t = imu.temperature
  
  print("ax:", ax, "ay: ", ay, "az:", az)
  #print("gx:", gx, "gy: ", gy, "gz:", gz)
  oled.fill(0)
  oled.text("ax:"+str(ax), 0, 0)
  oled.text("ay:"+str(ay), 0, 9)
  oled.text("az:"+str(az), 0, 18)
  oled.text("gx:"+str(gx), 0, 27)
  oled.text("gy:"+str(gy), 0, 36)
  oled.text("gz:"+str(gz), 0, 45)
  oled.text("Temp:"+str(t), 0, 54)
  oled.show()
  sleep(0.5)
