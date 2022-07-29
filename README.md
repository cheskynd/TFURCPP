# ThanatoFenestra Altar
Developed by:
- [Ndizeye Tschesquis](https://github.com/cheskynd) - `Berea College`
- [Blade E. Hicks](https://github.com/BladeHicks) - `Berea College`
- [Nancy Landeros](https://github.com/nancylanderos) - `Berea College`

Libraries:
- OpenCV
- numpy
- Pillow 
- gpiozero 
- screeninfo 
- future
- Click [Here](requirements.txt) to view requirements file 

## Electronic Components

| Component                                      | Quantity |
|------------------------------------------------|----------|
| Raspberry Pi                                   | 1        |
| (TMP36) Temperature Sensor                     | 1        |
| CdS Photoresistor                              | 2        |
| MCP3008 (Digital to Analog Convertor)          | 1        |
| Breadboard or PCB                              | 1        |
| 4.7kΩ Resistor                                 | 2        |
| Miroir M75 Portable Projector (Pico Projector) | 1        |


## Circuit and Schematic
This is the Schematic for the sensor connections to the MCP3008 chip
![Schematic](Schematic.png)


This is the pinout of the Raspberry Pi 3B+
![Raspberry Pi 3B+ Pinout](img.png)

Make the Following connections between the MCP3008 and Raspberry Pi
- MCP3008 CLK to Raspberry Pi SCLK (gpio 11)
- MCP3008 DOUT to Raspberry Pi MISO (gpio 9)
- MCP3008 DIN to Raspberry Pi MOSI (gpio 10)
- MCP3008 CS to Raspberry Pi CEO (gpio 8)
- MCP3008 VDD to Raspberry Pi 3.3V
- MCP3008 VREF to Raspberry Pi 3.3V
- MCP3008 AGND to Raspberry Pi GND
- MCP3008 DGND to Raspberry Pi GND
