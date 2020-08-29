"""
    惊雷歌词制作
"""
import pyttsx3 as p #播放语音的功能；
import pygame  #界面播放器；
import sys
#pygame从这开始
pygame.init() #初始化驱动
pygame.mixer.init()

music_name = "惊雷.mp3"
music_name = music_name.encode('utf-8') #歌曲中文字体转换

pygame.mixer.music.load(music_name) # 加载歌曲
pygame.mixer.music.play() # 播放

screen = pygame.display.set_mode([300,300]) #界面大小
pygame.mixer.music.set_volume(0.2) #声音设置；
#用于把图片保存到pygame里面；
img = pygame.image.load("./timg.jpg") #界面封面
screen.blit(img,(0,0))
pygame.display.update()
#pygame到这结束

#pyttsx3代码开始
with open('惊雷.txt','r',encoding='utf-8') as f:
    msg_list = f.readline().split(',') #把字符串转换成列表；
engine = p.init() #驱动初始化；
# 调整频率
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)
# 调整音量
volume = engine.getProperty('volume')
engine.setProperty('volume', volume + 2)
engine = p.init()
for k in range(2):
    for each in msg_list:
        engine.say(each)
engine.runAndWait()
# 设置打开界面的关闭方法，没有的话打开的界面没法关闭。
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
#pyttsx3代码结束



