import pygame
from pygame.locals import *
import sys
import random
import math
pygame.init()
FPS=30
fpsclock=pygame.time.Clock()
screen=pygame.display.set_mode((1280,720))
pygame.display.set_caption('Covid game')
pygame.mouse.set_visible(False)




def game(choosenplayerconstant,choosenplayerupthrust,choosenplayerlowthrust,choosenplayerscating,choosenplayerdead,Highscore):
    
    playerconstant=choosenplayerconstant
    playerupthrust=choosenplayerupthrust
    playerlowthrust=choosenplayerlowthrust
    playerscating=choosenplayerscating
    playerdead=choosenplayerdead
    deadangle=0

    #health
    life_=100
    coronaeffect_=0
    coronaeff=0
    ceffmid=cbarmid
    lifeeff=((life_-1)*7)+1
    lifeeffmid=pygame.transform.scale(lifebarmid,(lifeeff,10))
    Dead=False
    Covidpositive=False
    alearttime=pygame.time.get_ticks()
    endgame=False
    
    #distance
    Distancecovered=0
    dist=Distancecovered
    Distance_=0
    distlist=[]
    for j in range(len(str(dist))):
        distlist.insert(0,dist%10)
        dist=dist//10
    #goldcoin
    Goldcollected=0
    gcoin=Goldcollected
    coinlist=[]
    for j in range(len(str(gcoin))):
        coinlist.insert(0,gcoin%10)
        gcoin=gcoin//10

    #game items
    Heartlist=[]
    Sanitizerlist=[]
    Vaccinelist=[]
    Spraylist=[]
    Ppekitlist=[]
    Woodlist=[]
    Viruslist=[]
    Giantviruslist=[]
    Coinlist=[]
    Gind=0
    GVind=0

    giantvirusexplodelist=[]
    healefflist=[]
    affectefflist=[]
    virusexplodelist=[]
    woodbreaklist=[]
    movegold=[]

    #banner
    showbanner=False
    showbannertime=pygame.time.get_ticks()
    pointbanner=healthplus25

        
    #pocket
    Pocketitems=[]
    
    Wall=[]
    Topbrick=[]
    Bottomroad=[]
    bgX=0
    for j in range(5):
        Wall.append({'index':random.randint(0,3),'x':bgX,'y':0})
        Topbrick.append({'index':random.randint(0,3),'x':bgX,'y':0})
        Bottomroad.append({'index':random.randint(0,3),'x':bgX,'y':620})
        bgX+=320
    move=False
    timego=pygame.time.get_ticks()
    speed=6
    timeacc=pygame.time.get_ticks()
    constant=False
    playerpos={'x':400,'y':310}
    thrust=10
    player=playerconstant
    goup=False
    godown=False
    onroad=False
    Scateboard=[]
    i=0#player index
    Blast=False
    blasttime=pygame.time.get_ticks()#blast shake effect time
    bshake=0
    timeshake=pygame.time.get_ticks()#stable shake effect time
    stablex,stabley=0,0
    ppekittime=pygame.time.get_ticks()#ppekit time
    ppeprotectiontime=pygame.time.get_ticks()#ppeprotection time
    ppei=0#ppeprotection index
    ppekiton=False
    

    
    Vaccined=False#true while using vaccine
    vaccinetime=pygame.time.get_ticks()
    Sanitized=False#true while using sanitizer
    Handrubtime=pygame.time.get_ticks()
    rubbingtime=pygame.time.get_ticks()
    rubind=0
    Sprayonhand=False#true if holding spray
    Spraying=False#true while using spray
    sprayleft=150#spray left in the bottle
    Throwing=[]
    Sprayending=False
    Stopspray=False

    starting=True
    ti=0
    countindex=0
    showsurvive=False
    showtime=pygame.time.get_ticks()

    Spawn=False
    spawnno=1
    spawnx=1380
    occupy=[1,2,3]
    empty=[1,2,3]

    Showtimer=False
    timerimg=ppetimer[10]

    countdownsound.play()
    
    
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN and event.key==K_ESCAPE:
                transitionblind()
                return Highscore
            if move and not Dead:
                if event.type==KEYDOWN and (event.key==K_UP or event.key==K_w):
                    if onroad:
                        Scateboard.append({'x':playerpos['x']+15,'y':playerpos['y']+80})
                        onroad=False
                    player=playerupthrust
                    goup=True
                    godown=False
                if event.type==KEYUP and (event.key==K_UP or event.key==K_w):
                    goup=False
                    if not godown:
                        player=playerconstant
                if not onroad and (event.type==KEYDOWN and (event.key==K_DOWN or event.key==K_s)):
                    player=playerlowthrust
                    godown=True
                    goup=False
                if not onroad and (event.type==KEYUP and (event.key==K_DOWN or event.key==K_s)):        
                    godown=False
                    if not goup:
                        player=playerconstant
                       
                if event.type==KEYDOWN and (event.key==K_RIGHT or event.key==K_d):#select right
                    if len(Pocketitems)>1:
                        for j in range(len(Pocketitems)-1,0,-1):
                            if Pocketitems[j-1]['selected']:
                                Pocketitems[j]['selected']=True
                                Pocketitems[j-1]['selected']=False
                                break
                if event.type==KEYDOWN and (event.key==K_LEFT or event.key==K_a):#select left
                    if len(Pocketitems)>1:
                        for j in range(len(Pocketitems)-1):
                            if Pocketitems[j+1]['selected']:
                                Pocketitems[j]['selected']=True
                                Pocketitems[j+1]['selected']=False
                                break
                if (event.type==KEYDOWN and (event.key==K_RETURN or event.key==K_e)) and not Sprayonhand and not Sanitized and not ppekiton:#use pocket item
                    if len(Pocketitems)>0:
                        for j in range(len(Pocketitems)):
                            if Pocketitems[j]['selected']:
                                
                                if Pocketitems[j]['item']==0:
                                    Vaccined=True
                                    Showtimer=True
                                    timerimg=vaccinetimer[10]
                                    vaccinetime=pygame.time.get_ticks()
                                    ppeprotectiontime=pygame.time.get_ticks()
                                    showbanner=True
                                    pointbanner=affectedminus100
                                    showbannertime=pygame.time.get_ticks()
                                    coronaeffect_=0
                                    Throwing.append({'image':emptyvaccine,'bottle':emptyvaccine,'x':playerpos['x']+70,'y':playerpos['y']+70,'angle':0})
                                if Pocketitems[j]['item']==1:
                                    Sanitized=True
                                    sanitizingsound.play()
                                    if coronaeffect_>50 and not Covidpositive:
                                        coronaeffect_-=50
                                        coronaeff=((coronaeffect_-1)*8)+2
                                        ceffmid=pygame.transform.scale(cbarmid,(coronaeff,10))
                                        showbanner=True
                                        pointbanner=affectedminus50
                                        showbannertime=pygame.time.get_ticks()
                                    elif not Covidpositive:
                                        coronaeffect_=0
                                        showbanner=True
                                        pointbanner=affectedminus50
                                        showbannertime=pygame.time.get_ticks()
                                        
                                    Handrubtime=pygame.time.get_ticks()
                                    rubbingtime=pygame.time.get_ticks()
                                    rubind=0
                                    Throwing.append({'image':emptysanitizer,'bottle':emptysanitizer,'x':playerpos['x']+70,'y':playerpos['y']+70,'angle':0})
                                if Pocketitems[j]['item']==2:
                                    Sprayonhand=True
                                    Spraying=False
                                    sprayimage=spraying[0]
                                    sprayleft=150
                                    splashind=0
                                    
                                if j==0:
                                    if len(Pocketitems)==1:
                                        Pocketitems.pop(0)
                                        break
                                    if len(Pocketitems)>1:
                                        Pocketitems[1]['selected']=True
                                        Pocketitems.pop(0)
                                        break
                                    
                                if j==1:
                                    if len(Pocketitems)==2:
                                        Pocketitems[0]['selected']=True
                                        Pocketitems.pop(1)
                                        break
                                    if len(Pocketitems)==3:
                                        Pocketitems[2]['selected']=True
                                        Pocketitems.pop(1)
                                        break
                                    
                                if j==2:
                                    Pocketitems[1]['selected']=True
                                    Pocketitems.pop(2)
                                    break

                                    
                if (event.type==KEYDOWN and event.key==K_SPACE) and Sprayonhand:
                    sprayingsound.play(-1)
                    Spraying=True
                    splashind=0
                if (event.type==KEYUP and event.key==K_SPACE) and Sprayonhand:
                    sprayingsound.stop()
                    Spraying=False
                    Stopspray=True
                    Sprayending=False
                    sprayind=5
                    if 120<sprayleft<=150:
                        sprayimage=spraying[0]
                    elif 90<sprayleft<=120:
                        sprayimage=spraying[2]
                    elif 60<sprayleft<=90:
                        sprayimage=spraying[4]
                    elif 30<sprayleft<=60:
                        sprayimage=spraying[6]
                    elif 0<sprayleft<=30:
                        sprayimage=spraying[8]
                if (event.type==KEYDOWN and (event.key==K_RSHIFT or event.key==K_q)) and Sprayonhand:
                    if 120<sprayleft<=150:
                        Throwing.append({'image':emptyspray[0],'bottle':emptyspray[0],'x':playerpos['x']+70,'y':playerpos['y']+70,'angle':0})
                    elif 90<sprayleft<=120:
                        Throwing.append({'image':emptyspray[1],'bottle':emptyspray[1],'x':playerpos['x']+70,'y':playerpos['y']+70,'angle':0})
                    elif 60<sprayleft<=90:
                        Throwing.append({'image':emptyspray[2],'bottle':emptyspray[2],'x':playerpos['x']+70,'y':playerpos['y']+70,'angle':0})
                    elif 30<sprayleft<=60:
                        Throwing.append({'image':emptyspray[3],'bottle':emptyspray[3],'x':playerpos['x']+70,'y':playerpos['y']+70,'angle':0})
                    elif 0<sprayleft<=30:
                        Throwing.append({'image':emptyspray[4],'bottle':emptyspray[4],'x':playerpos['x']+70,'y':playerpos['y']+70,'angle':0})
                    if not Spraying:
                        Sprayonhand=False
                        Sprayending=False
                        Stopspray=False
                    else:
                        Sprayending=True
                        Stopspray=True
                        Sprayonhand=False
                        Spraying=False
                        sprayind=5


        if Spawn:#-------------------------------spawns new game items
            column=random.randint(6,10)
            if speed<=10:
                emptyspace=random.randint(4,6)
            elif speed<=15:
                emptyspace=random.randint(5,7)
            elif speed<=20:
                emptyspace=random.randint(6,8)
            elif speed<=25:
                emptyspace=random.randint(7,9)
            else:
                emptyspace=random.randint(8,10)
            if random.randint(1,2)==1:
                cno=random.choice(occupy)
                occupy=[1,2,3]
                occupy.remove(cno)
                noofwood=random.randint(0,2)
                w=[]
                for j in range(noofwood):
                    while True:
                        win=random.randint(0,column-1)
                        if win not in w:
                            w.append(win)
                            break
                if random.randint(0,2)==2:
                    for c in range(column):
                        if c not in w:
                            for r in range(3):
                                Coinlist.append({'x':spawnx+c*40,'y':(140+(cno-1)*170)+(40*r)})
                        else:
                            Woodlist.append({'x':spawnx+c*40,'y':(135+(cno-1)*170)})
                else:
                    for c in range(column):
                        if c not in w:
                            for r in range(3):
                                Viruslist.append({'x':spawnx+c*40,'y':(140+(cno-1)*170)+(40*r)})
                        else:
                            Woodlist.append({'x':spawnx+c*40,'y':(135+(cno-1)*170)})

                if spawnno%2==0:
                    cno=random.choice(occupy)
                    if random.randint(0,2)==1:
                        Heartlist.append({'x':spawnx+((column*40)-50)/2,'y':cno*170})
                    else:
                        Giantviruslist.append({'x':spawnx+((column*40)-120)/2,'y':(135+(cno-1)*170)})            
            else:
                nno=random.choice(empty)
                empty=[1,2,3]
                empty.remove(nno)
                for cno in empty:
                    noofwood=random.randint(0,2)
                    w=[]
                    for j in range(noofwood):
                        while True:
                            win=random.randint(0,column-1)
                            if win not in w:
                                w.append(win)
                                break
                    if random.randint(0,2)==2:
                        for c in range(column):
                            if c not in w:
                                for r in range(3):
                                    Coinlist.append({'x':spawnx+c*40,'y':(140+(cno-1)*170)+(40*r)})
                            else:
                                Woodlist.append({'x':spawnx+c*40,'y':(135+(cno-1)*170)})
                    else:
                        for c in range(column):
                            if c not in w:
                                for r in range(3):
                                    Viruslist.append({'x':spawnx+c*40,'y':(140+(cno-1)*170)+(40*r)})
                            else:
                                Woodlist.append({'x':spawnx+c*40,'y':(135+(cno-1)*170)})
            if spawnno%5==0:
                if random.randint(1,2)==1:
                    cno=random.randint(1,3)
                    bl=random.randint(1,3)
                    if bl==1:
                        Spraylist.append({'x':spawnx+(column*40)+((emptyspace*40)-26)/2,'y':cno*170})
                    elif bl==2:
                        Vaccinelist.append({'x':spawnx+(column*40)+((emptyspace*40)-26)/2,'y':cno*170})
                    else:
                        Sanitizerlist.append({'x':spawnx+(column*40)+((emptyspace*40)-26)/2,'y':cno*170})
            elif spawnno%6==0:
                if random.randint(1,3)==2:
                    cno=random.randint(1,3)
                    Ppekitlist.append({'x':spawnx+(column*40)+((emptyspace*40)-50)/2,'y':cno*170})
            spawnx+=(column+emptyspace)*40
            spawnno+=1
            Spawn=False

                       
                    
        if not Dead:              
            if goup:#thrust up
                playerpos['y']-=thrust+math.trunc(speed/10)*2
            if godown:#low thrust
                playerpos['y']+=thrust+math.trunc(speed/10)*2
            if playerpos['y']+ph>=645:
                playerpos['y']=645-ph
                onroad=True
                godown=False
                player=playerscating
            if playerpos['y']<85:
                playerpos['y']=85

        if Spraying:
            sprayleft-=1
            if 120<sprayleft<=150:
                sprayimage=spraying[1]
            elif 90<sprayleft<=120:
                sprayimage=spraying[3]
            elif 60<sprayleft<=90:
                sprayimage=spraying[5]
            elif 30<sprayleft<=60:
                sprayimage=spraying[7]
            elif 0<sprayleft<=30:
                sprayimage=spraying[9]
            elif sprayleft==0:
                Throwing.append({'image':emptyspray[5],'bottle':emptyspray[5],'x':playerpos['x']+70,'y':playerpos['y']+70,'angle':0})
                sprayingsound.stop()
                Sprayending=True
                Stopspray=True
                sprayind=5
                Sprayonhand=False
                Spraying=False
            
        if not move:#delay
            if pygame.time.get_ticks() >= timego+1000:
                countindex=1
                if pygame.time.get_ticks() >= timego+2000:
                    countindex=2
                    if pygame.time.get_ticks() >= timego+3000:
                        move=True
                        Spawn=True
                        showsurvive=True
                        showtime=pygame.time.get_ticks()
                        timeacc=pygame.time.get_ticks()
        if showsurvive and pygame.time.get_ticks()>showtime+1000:
            showsurvive=False
            


        if not constant and (move and pygame.time.get_ticks() >= timeacc+15000):#increases speed after every 15 seconds
            speed+=1
            timeacc=pygame.time.get_ticks()
            if speed>=30:
                speed=30
                constant=True
                print('max speed reached')

          
        if move and not Dead:
            for j in range(5):#motion
                Wall[j]['x']-=speed
                Topbrick[j]['x']-=speed
                Bottomroad[j]['x']-=speed
                
            if Wall[0]['x']<=-320:#replace walls road and brick
                Wall.pop(0)
                Topbrick.pop(0)
                Bottomroad.pop(0)
                Wall.append({'index':random.randint(0,3),'x':Wall[3]['x']+320,'y':0})
                Topbrick.append({'index':random.randint(0,3),'x':Topbrick[3]['x']+320,'y':0})
                Bottomroad.append({'index':random.randint(0,3),'x':Bottomroad[3]['x']+320,'y':620})

            spawnx-=speed
                
            removeitem=[]
            for j in range(len(Heartlist)):#heartlist
                Heartlist[j]['x']-=speed
                if Heartlist[j]['x']<-120:
                    removeitem.append(j)
            removeitem.sort()
            passed=0
            for j in removeitem:
                Heartlist.pop(j-passed)
                passed+=1
                print('done')
                
            removeitem=[]
            for j in range(len(Sanitizerlist)):#sanitizerlist
                Sanitizerlist[j]['x']-=speed
                if Sanitizerlist[j]['x']<-120:
                    removeitem.append(j)
            removeitem.sort()
            passed=0
            for j in removeitem:
                Sanitizerlist.pop(j-passed)
                passed+=1
                
            removeitem=[]
            for j in range(len(Vaccinelist)):#vaccinelist
                Vaccinelist[j]['x']-=speed
                if Vaccinelist[j]['x']<-120:
                    removeitem.append(j)
            removeitem.sort()
            passed=0
            for j in removeitem:
                Vaccinelist.pop(j-passed)
                passed+=1
                
            removeitem=[]
            for j in range(len(Spraylist)):#spraylist
                Spraylist[j]['x']-=speed
                if Spraylist[j]['x']<-120:
                    removeitem.append(j)
            removeitem.sort()
            passed=0
            for j in removeitem:
                Spraylist.pop(j-passed)
                passed+=1

            removeitem=[]
            for j in range(len(Ppekitlist)):#ppekitlist
                Ppekitlist[j]['x']-=speed
                if Ppekitlist[j]['x']<-120:
                    removeitem.append(j)
            removeitem.sort()
            passed=0
            for j in removeitem:
                Ppekitlist.pop(j-passed)
                passed+=1
                
            removeitem=[]
            for j in range(len(Woodlist)):#woodlist
                Woodlist[j]['x']-=speed
                if Woodlist[j]['x']<-120:
                    removeitem.append(j)
            removeitem.sort()
            passed=0
            for j in removeitem:
                Woodlist.pop(j-passed)
                passed+=1
                
            removeitem=[]
            for j in range(len(Viruslist)):#smallvirus list
                Viruslist[j]['x']-=speed
                if Viruslist[j]['x']<-120:
                    removeitem.append(j)
            removeitem.sort()
            passed=0
            for j in removeitem:
                Viruslist.pop(j-passed)
                passed+=1
                
            removeitem=[]
            for j in range(len(Giantviruslist)):#giantvirus list
                Giantviruslist[j]['x']-=speed
                if Giantviruslist[j]['x']<-120:
                    removeitem.append(j)
            removeitem.sort()
            passed=0
            for j in removeitem:
                Giantviruslist.pop(j-passed)
                passed+=1
                
            removeitem=[]
            for j in range(len(Coinlist)):#goldcoin list
                Coinlist[j]['x']-=speed
                if Coinlist[j]['x']<-120:
                    removeitem.append(j)
            removeitem.sort()
            passed=0
            for j in removeitem:
                Coinlist.pop(j-passed)
                passed+=1
                    
                
            Distancecovered+=speed
            dist=math.trunc(Distancecovered/50)
            Distance_=dist
            distlist=[]
            for j in range(len(str(dist))):
                distlist.insert(0,dist%10)
                dist=dist//10
                
        if not Spawn:
            if spawnx<1380:
                Spawn=True

        #pocket items
        if not Dead:
            Sanitizerlist,Pocketitems=sanitizercollected(playerpos,Sanitizerlist,Pocketitems)
            Vaccinelist,Pocketitems=vaccinecollected(playerpos,Vaccinelist,Pocketitems)
            Spraylist,Pocketitems=spraycollected(playerpos,Spraylist,Pocketitems)
            Coinlist,Goldcollected,coinlist,movegold=coincollection(playerpos,Coinlist,Goldcollected,movegold)
            Ppekitlist,ppekiton,Vaccined,ppeprotectiontime,ppekittime,playerconstant,playerupthrust,playerlowthrust,playerscating,player,Showtimer,timerimg,speed=ppekitcollected(playerpos,Ppekitlist,ppekiton,Vaccined,ppeprotectiontime,ppekittime,playerconstant,playerupthrust,playerlowthrust,playerscating,goup,godown,onroad,player,Showtimer,timerimg,speed)
            Heartlist,life_,showbanner,showbannertime,pointbanner,lifeeff,lifeeffmid,healefflist=heartcollected(playerpos,Heartlist,life_,showbanner,showbannertime,pointbanner,lifeeff,lifeeffmid,healefflist)
            Woodlist,life_,showbanner,showbannertime,pointbanner,lifeeff,lifeeffmid,woodbreaklist,Blast,blasttime=hitbywood(Blast,blasttime,playerpos,Woodlist,life_,showbanner,showbannertime,pointbanner,lifeeff,lifeeffmid,woodbreaklist,ppekiton)
            Viruslist,coronaeffect_,showbanner,showbannertime,pointbanner,coronaeff,ceffmid,affectefflist=hitbyvirus(playerpos,Viruslist,coronaeffect_,showbanner,showbannertime,pointbanner,coronaeff,ceffmid,Vaccined,ppekiton,affectefflist)        
            Giantviruslist,coronaeffect_,showbanner,showbannertime,pointbanner,coronaeff,ceffmid,giantvirusexplodelist,Blast,blasttime=hitbygiantvirus(Blast,blasttime,playerpos,Giantviruslist,coronaeffect_,showbanner,showbannertime,pointbanner,coronaeff,ceffmid,giantvirusexplodelist,Vaccined,ppekiton)
            if Spraying:
                Viruslist,virusexplodelist=killsmallvirus(playerpos,Viruslist,virusexplodelist)
        if life_==0:
            Dead=True
        elif coronaeffect_==100 and not Covidpositive:
            Covidpositive=True
            alarmsound.play()
            alearttime=pygame.time.get_ticks()
            player=playerconstant
        elif coronaeffect_<100:
            Covidpositive=False

        if Covidpositive and not Dead:
            life_-=1
            if life_==0:
                hurtsound.play()
                Dead=True
            else:
                lifeeff=((life_-1)*7)+1
                lifeeffmid=pygame.transform.scale(lifebarmid,(lifeeff,10))
                



        for j in range(len(Scateboard)):#scateboard
            Scateboard[j]['x']-=speed/2
        if len(Scateboard)!=0:#popscateboard
            while True:
                if Scateboard[0]['x']<-50:
                    Scateboard.pop(0)
                    if len(Scateboard)==0:
                        break
                else:
                    break
        #blast effect
        if Blast:      
            if pygame.time.get_ticks()>blasttime+100:
                if pygame.time.get_ticks()>blasttime+175:
                    if pygame.time.get_ticks()>blasttime+225:
                        if pygame.time.get_ticks()>blasttime+250:      
                            Blast=False
                            bshake=0
                        else:
                            bshake=blastshake(0,2)
                    else:
                        bshake=blastshake(2,5)
                else:
                    bshake=blastshake(5,8)
            else:
                bshake=blastshake(8,12)

                
        #stable player
        if pygame.time.get_ticks()>timeshake+150 and not onroad:
            stablex,stabley=stableplayer()
            timeshake=pygame.time.get_ticks()
        elif onroad:
            stablex,stabley=0,0
            
        removeitem=[]
        for j in range(len(movegold)):
            if 160<movegold[j]['x']<190 and 10<movegold[j]['y']<40:
                removeitem.append(j)
                pointsound.play()
            else:
                movegold[j]['x']+=movegold[j]['cx']
                movegold[j]['y']+=movegold[j]['cy']
        removeitem.sort()
        passed=0
        for j in removeitem:
            movegold.pop(j-passed)
            passed+=1

        #blitting images

        if Blast:
            screen.fill((102,17,17))
        for k in range(5):
            screen.blit(wall[Wall[k]['index']],(Wall[k]['x'],Wall[k]['y']+bshake))
            screen.blit(topbrick[Topbrick[k]['index']],(Topbrick[k]['x'],Topbrick[k]['y']+bshake))
            screen.blit(bottomroad[Bottomroad[k]['index']],(Bottomroad[k]['x'],Bottomroad[k]['y']+bshake))
        for k in range(len(Scateboard)):
            screen.blit(scateboard[i],(Scateboard[k]['x'],Scateboard[k]['y']+bshake))#scateboard

        for k in range(len(Viruslist)):#small virus
            screen.blit(smallvirus,(Viruslist[k]['x'],Viruslist[k]['y']+bshake))
        for k in range(len(Coinlist)):#coins
            screen.blit(goldcoin[Gind],(Coinlist[k]['x'],Coinlist[k]['y']+bshake))
        for k in range(len(Woodlist)):#wood
            screen.blit(wood,(Woodlist[k]['x'],Woodlist[k]['y']+bshake))
        for k in range(len(Heartlist)):#heart
            screen.blit(collectheart,(Heartlist[k]['x'],Heartlist[k]['y']+bshake))
        for k in range(len(Giantviruslist)):#giantvirus
            screen.blit(giantvirus[GVind],(Giantviruslist[k]['x'],Giantviruslist[k]['y']+bshake))
        for k in range(len(Sanitizerlist)):#sanitizer
            screen.blit(collectsanitizer,(Sanitizerlist[k]['x'],Sanitizerlist[k]['y']+bshake))
        for k in range(len(Vaccinelist)):#vaccine
            screen.blit(collectvaccine,(Vaccinelist[k]['x'],Vaccinelist[k]['y']+bshake))
        for k in range(len(Spraylist)):#spray
            screen.blit(collectspray,(Spraylist[k]['x'],Spraylist[k]['y']+bshake))
        for k in range(len(Ppekitlist)):#ppekit
            screen.blit(collectppekit,(Ppekitlist[k]['x'],Ppekitlist[k]['y']+bshake))

        removeitem=[]
        for k in range(len(virusexplodelist)):#virus death effect
            screen.blit(virusdead[virusexplodelist[k]['index']],(virusexplodelist[k]['x'],virusexplodelist[k]['y']+bshake))
            virusexplodelist[k]['index']+=1
            if virusexplodelist[k]['index']==8:
                removeitem.append(k)
        removeitem.sort()
        passed=0
        for j in removeitem:
            virusexplodelist.pop(j-passed)
            passed+=1

            

        if Dead:
            screen.blit(playerdead,(playerpos['x'],playerpos['y']+bshake))
            playerdead=pygame.transform.rotate(choosenplayerdead, deadangle)
            playerpos['x']+=(speed/4)*3
            playerpos['y']+=10
            deadangle-=1
            if playerpos['y']>720:
                transitionblind()
                print(speed)
                Highscore=show_score(Highscore,Distance_,distlist)
                return Highscore
                
        elif Vaccined:#player with vaccineprotection
            screen.blit(vaccineprotectiondown[ppei],(playerpos['x']+stablex,playerpos['y']+stabley+bshake))
            screen.blit(player[i],(playerpos['x']+stablex,playerpos['y']+stabley+bshake))
            screen.blit(vaccineprotectionup[ppei],(playerpos['x']+stablex,playerpos['y']+stabley+bshake))
        elif ppekiton:#player with ppekitprotection
            screen.blit(ppekitprotectiondown[ppei],(playerpos['x']+stablex,playerpos['y']+stabley+bshake))
            screen.blit(player[i],(playerpos['x']+stablex,playerpos['y']+stabley+bshake))
            screen.blit(ppekitprotectionup[ppei],(playerpos['x']+stablex,playerpos['y']+stabley+bshake))
        else:#only player
            screen.blit(player[i],(playerpos['x']+stablex,playerpos['y']+stabley+bshake))

        if Sprayonhand or Sprayending:#using spray
            if not Sprayending:
                screen.blit(sprayimage,(playerpos['x']+70+stablex,playerpos['y']+35+stabley+bshake))
            if Spraying or Stopspray:
                screen.blit(splashes[splashind],(playerpos['x']+106+stablex,playerpos['y']+stabley+bshake))
                splashind+=1
                if not Stopspray:
                    if splashind>4:
                        splashind=2
                elif splashind>7:
                    Stopspray=False
                    Sprayending=False
                    splashind=0
        if Sanitized:
            screen.blit(handrub[rubind],(playerpos['x']+70+stablex,playerpos['y']+35+stabley+bshake))
            if pygame.time.get_ticks() > rubbingtime+30:
                rubind+=1
                if rubind>11:
                    rubind=0
                rubbingtime=pygame.time.get_ticks()
            if pygame.time.get_ticks() > Handrubtime+3000:
                Sanitized=False

        removeitem=[]
        for k in range(len(affectefflist)):#virus affected effect
            screen.blit(affectedeffect[affectefflist[k]['index']],(playerpos['x']+stablex,playerpos['y']+stabley+bshake))
            affectefflist[k]['index']+=1
            if affectefflist[k]['index']==6:
                removeitem.append(k)
        removeitem.sort()
        passed=0
        for j in removeitem:
            affectefflist.pop(j-passed)
            passed+=1

        removeitem=[]
        for k in range(len(healefflist)):#heal effect
            screen.blit(healeffect[healefflist[k]['index']],(playerpos['x']+10+stablex,playerpos['y']+stabley+bshake))
            healefflist[k]['index']+=1
            if healefflist[k]['index']==12:
                removeitem.append(k)
        removeitem.sort()
        passed=0
        for j in removeitem:
            healefflist.pop(j-passed)
            passed+=1

        for k in range(len(Throwing)):# empty bottles throw
            screen.blit(Throwing[k]['image'],(Throwing[k]['x'],Throwing[k]['y']+bshake))
            Throwing[k]['y']+=10
            Throwing[k]['x']-=5
            Throwing[k]['image']=pygame.transform.rotate(Throwing[k]['bottle'], Throwing[k]['angle'])
            Throwing[k]['angle']-=2
        if len(Throwing)!=0:#pop empty bottles
            while True:
                if Throwing[0]['y']>720:
                    Throwing.pop(0)
                    if len(Throwing)==0:
                        break
                else:
                    break

        if showbanner:
            screen.blit(pointbanner,(playerpos['x']+25+stablex,playerpos['y']-25+stabley+bshake))
            if pygame.time.get_ticks()>showbannertime+3000:
                showbanner=False


        removeitem=[]
        for k in range(len(woodbreaklist)):#woodbreak effect
            screen.blit(woodbreak[woodbreaklist[k]['index']],(woodbreaklist[k]['x'],woodbreaklist[k]['y']+bshake))
            woodbreaklist[k]['index']+=1
            if woodbreaklist[k]['index']==9:
                removeitem.append(k)
        removeitem.sort()
        passed=0
        for j in removeitem:
            woodbreaklist.pop(j-passed)
            passed+=1
            
        removeitem=[]
        for k in range(len(giantvirusexplodelist)):#giantvirus explode effect
            screen.blit(giantvirusexplode[giantvirusexplodelist[k]['index']],(giantvirusexplodelist[k]['x'],giantvirusexplodelist[k]['y']+bshake))
            giantvirusexplodelist[k]['index']+=1
            if giantvirusexplodelist[k]['index']==9:
                removeitem.append(k)
        removeitem.sort()
        passed=0
        for j in removeitem:
            giantvirusexplodelist.pop(j-passed)
            passed+=1
            
        for k in range(len(movegold)):
            screen.blit(goldcoin[0],(movegold[k]['x'],movegold[k]['y']))

        if Covidpositive:#aleart
            if pygame.time.get_ticks()<alearttime+300:
                screen.blit(aleart,(0,0))
            if pygame.time.get_ticks()>alearttime+600:
                alarmsound.play()
                alearttime=pygame.time.get_ticks()



            


                    
                    
                


        #health
        screen.blit(healthbar,(0,620))
        if life_!=0:
            screen.blit(lifebarstart,(140,682.5))
            screen.blit(lifeeffmid,(143,682.5))
            screen.blit(lifebarend,(143+lifeeff,682.5))
        if coronaeffect_!=0:
            screen.blit(cbarstart,(90,702.5))
            screen.blit(ceffmid,(93,702.5))
            screen.blit(cbarend,(93+coronaeff,702.5))
        #pocket
        screen.blit(pocket,(15,15))
        pix=25
        for k in range(len(Pocketitems)):
            if Pocketitems[k]['selected']:
                screen.blit(onpocketitem,(pix-2.5,22.5))
            if Pocketitems[k]['item']==2:
                screen.blit(spraylogo,(pix,25))
            elif Pocketitems[k]['item']==1:
                screen.blit(sanitizerlogo,(pix,25))
            else:
                screen.blit(vaccinelogo,(pix,25))
            pix+=42.5
        #goldcoin
        pointx=165
        screen.blit(coinicon,(pointx,15))
        pointx+=50
        screen.blit(_x,(pointx,35))
        pointx+=30
        for k in coinlist:
            screen.blit(_numbers[k],(pointx,35))
            pointx+=30
        pointx+=15
        #distance
        screen.blit(distanceicon,(pointx,15))
        pointx+=210
        screen.blit(_x,(pointx,35))
        pointx+=30
        for k in distlist:
            screen.blit(_numbers[k],(pointx,35))
            pointx+=30
        screen.blit(_m,(pointx,35))

        if ppekiton:
            if pygame.time.get_ticks()<ppekittime+1000:
                timerimg=ppetimer[10]
            elif pygame.time.get_ticks()<ppekittime+2000:
                timerimg=ppetimer[9]
            elif pygame.time.get_ticks()<ppekittime+3000:
                timerimg=ppetimer[8]
            elif pygame.time.get_ticks()<ppekittime+4000:
                timerimg=ppetimer[7]
            elif pygame.time.get_ticks()<ppekittime+5000:
                timerimg=ppetimer[6]
            elif pygame.time.get_ticks()<ppekittime+6000:
                timerimg=ppetimer[5]
            elif pygame.time.get_ticks()<ppekittime+7000:
                timerimg=ppetimer[4]
            elif pygame.time.get_ticks()<ppekittime+8000:
                timerimg=ppetimer[3]
            elif pygame.time.get_ticks()<ppekittime+9000:
                timerimg=ppetimer[2]
            elif pygame.time.get_ticks()<ppekittime+10000:
                timerimg=ppetimer[1]
        elif Vaccined:
            if pygame.time.get_ticks()<vaccinetime+1000:
                timerimg=vaccinetimer[10]
            elif pygame.time.get_ticks()<vaccinetime+2000:
                timerimg=vaccinetimer[9]
            elif pygame.time.get_ticks()<vaccinetime+3000:
                timerimg=vaccinetimer[8]
            elif pygame.time.get_ticks()<vaccinetime+4000:
                timerimg=vaccinetimer[7]
            elif pygame.time.get_ticks()<vaccinetime+5000:
                timerimg=vaccinetimer[6]
            elif pygame.time.get_ticks()<vaccinetime+6000:
                timerimg=vaccinetimer[5]
            elif pygame.time.get_ticks()<vaccinetime+7000:
                timerimg=vaccinetimer[4]
            elif pygame.time.get_ticks()<vaccinetime+8000:
                timerimg=vaccinetimer[3]
            elif pygame.time.get_ticks()<vaccinetime+9000:
                timerimg=vaccinetimer[2]
            elif pygame.time.get_ticks()<vaccinetime+10000:
                timerimg=vaccinetimer[1]

        #timer
        if Showtimer:
            screen.blit(timerimg,(50,310))
            if pygame.time.get_ticks()>ppekittime+11000 and pygame.time.get_ticks()>vaccinetime+11000:
                Showtimer=False
        
        #escback
        screen.blit(escback,(1115,15))

        if not move:
            screen.blit(countdown[countindex],(590,285))
        elif showsurvive:
            screen.blit(survive,(480,325))
        

        if starting:#transition
            ti=transitionopen(ti)
            if ti>16:
                starting=False
                ti=0








        #change index

        GVind+=1
        if GVind==4:#giantvirus
            GVind=0
            
        Gind+=1
        if Gind==8:#gold coin
            Gind=0
            
        i+=1
        if i==4:#player
            i=0
        if pygame.time.get_ticks()>ppeprotectiontime+100 and (ppekiton or Vaccined):
            ppei+=1
            if ppei==10:#ppekitprotection
                ppei=0
            ppeprotectiontime=pygame.time.get_ticks()
        if  pygame.time.get_ticks()>ppekittime+10000 and ppekiton:#ppekit for 10 seconds
            ppei=0
            ppekiton=False
            speed-=5
            playerconstant=choosenplayerconstant
            playerupthrust=choosenplayerupthrust
            playerlowthrust=choosenplayerlowthrust
            playerscating=choosenplayerscating
            if goup:
                player=playerupthrust
            if godown:
                player=ppekitlowthrust
            if onroad:
                player=playerscating
            else:
                player=playerconstant
            timerimg=ppetimer[0]
        if pygame.time.get_ticks()>vaccinetime+10000 and Vaccined:
            ppei=0
            Vaccined=False
            timerimg=vaccinetimer[0]
                
            
            
        
        pygame.display.update()
        fpsclock.tick(FPS)





def menu():
    Highscore=0
    hsno=Highscore
    hslist=[]
    for j in range(len(str(hsno))):
        hslist.insert(0,hsno%10)
        hsno=hsno//10
    Viruses=[]
    for j in range(random.randint(10,15)):
        vw=random.randint(50,100)
        vx=random.randint(0,1280-vw)
        vy=random.randint(0,720-vw)
        Viruses.append({'virus':pygame.transform.scale(Virus[random.randint(0,1)],(vw,vw)),'x':vx,'y':vy,'width':vw})
    Buttonsmenu=(
        {'w':400,'h':100,'x':440,'y':105,'state':False,'name':startbutton},
        {'w':400,'h':100,'x':440,'y':310,'state':False,'name':playerbutton},
        {'w':400,'h':100,'x':440,'y':515,'state':False,'name':settingsbutton},
        {'w':50,'h':50,'x':1205,'y':25,'state':False,'name':quitbutton}
        )
    Buttonplayer=(
        {'w':300,'h':300,'x':95,'y':210,'state':False,'name':doctorbutton},
        {'w':300,'h':300,'x':490,'y':210,'state':False,'name':avatarbutton},
        {'w':300,'h':300,'x':885,'y':210,'state':False,'name':policebutton},
        {'w':50,'h':50,'x':1205,'y':25,'state':False,'name':backbutton}
        )
    Buttonsetting=(
        {'w':400,'h':100,'x':440,'y':105,'state':False,'name':soundsbutton},
        {'w':400,'h':100,'x':440,'y':310,'state':False,'name':scorebutton},
        {'w':400,'h':100,'x':440,'y':515,'state':False,'name':aboutbutton},
        {'w':50,'h':50,'x':1205,'y':25,'state':False,'name':backbutton}
        )
    Buttonsounds=(
        {'w':400,'h':100,'x':440,'y':205,'state':False,'name':musiconbutton},
        {'w':400,'h':100,'x':440,'y':410,'state':False,'name':vfxonbutton},
        {'w':50,'h':50,'x':1205,'y':25,'state':False,'name':backbutton}
        )
    Buttonabout=(#same for about and highscore
        {'w':50,'h':50,'x':1205,'y':25,'state':False,'name':backbutton},
        )
    #default player is avatar when game is opened
    choosenplayerconstant=avatarconstant
    choosenplayerupthrust=avatarupthrust
    choosenplayerlowthrust=avatarlowthrust
    choosenplayerscating=avatarscating
    choosenplayerdead=avatardead
    
    Musicon=True
    Vfxon=True
    
    buttons=Buttonsmenu
    Showabout=False
    Showhighscore=False
    _Playermenu=False
    psx,psy=490,210

    starting=True
    ti=0
    bgmusic.play(-1)


    
    while True:
        mx,my=pygame.mouse.get_pos()
        buttons=checkonbuttons(mx,my,buttons)
        
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons==Buttonsmenu:#--------------------main menu
                    if buttons[0]['state']:#checks play
                        buttonclickedsound.play()
                        screen.blit(buttons[0]['name'][2],(buttons[0]['x'],buttons[0]['y']))
                        screen.blit(mouse,(mx,my))
                        pygame.display.update()
                        fpsclock.tick(FPS)
                        transitionblind()
                        bgmusic.stop()
                        Highscore=game(choosenplayerconstant,choosenplayerupthrust,choosenplayerlowthrust,choosenplayerscating,choosenplayerdead,Highscore)
                        bgmusic.play(-1)
                        hsno=Highscore
                        hslist=[]
                        for j in range(len(str(hsno))):
                            hslist.insert(0,hsno%10)
                            hsno=hsno//10
                        starting=True
                        ti=0

                    elif buttons[1]['state']:#checks player
                        buttonclickedsound.play()
                        screen.blit(buttons[1]['name'][2],(buttons[1]['x'],buttons[1]['y']))
                        screen.blit(mouse,(mx,my))
                        pygame.display.update()
                        fpsclock.tick(FPS)
                        buttons=Buttonplayer
                        _Playermenu=True
                    elif buttons[2]['state']:#checks settings
                        buttonclickedsound.play()
                        screen.blit(buttons[2]['name'][2],(buttons[2]['x'],buttons[2]['y']))
                        screen.blit(mouse,(mx,my))
                        pygame.display.update()
                        fpsclock.tick(FPS)
                        buttons=Buttonsetting
                    elif buttons[3]['state']:#checks exit
                        bgmusic.stop()
                        buttonclickedsound.play()
                        screen.blit(buttons[3]['name'][2],(buttons[3]['x'],buttons[3]['y']))
                        screen.blit(mouse,(mx,my))
                        pygame.display.update()
                        fpsclock.tick(FPS)
                        transitionblind()
                        pygame.quit()
                        sys.exit()
                elif buttons==Buttonplayer:#----------------player
                    if buttons[0]['state']:
                        buttonclickedsound.play()
                        screen.blit(buttons[0]['name'][2],(buttons[0]['x'],buttons[0]['y']))
                        screen.blit(mouse,(mx,my))
                        pygame.display.update()
                        fpsclock.tick(FPS)
                        psx,psy=buttons[0]['x'],buttons[0]['y']
                        choosenplayerconstant=avatarconstant
                        choosenplayerupthrust=avatarupthrust
                        choosenplayerlowthrust=avatarlowthrust
                        choosenplayerscating=avatarscating
                        choosenplayerdead=avatardead
                        #doctor
                    elif buttons[1]['state']:
                        buttonclickedsound.play()
                        screen.blit(buttons[1]['name'][2],(buttons[1]['x'],buttons[1]['y']))
                        screen.blit(mouse,(mx,my))
                        pygame.display.update()
                        fpsclock.tick(FPS)
                        psx,psy=buttons[1]['x'],buttons[1]['y']
                        choosenplayerconstant=avatarconstant
                        choosenplayerupthrust=avatarupthrust
                        choosenplayerlowthrust=avatarlowthrust
                        choosenplayerscating=avatarscating
                        choosenplayerdead=avatardead
                        #avatar
                    elif buttons[2]['state']:
                        buttonclickedsound.play()
                        screen.blit(buttons[2]['name'][2],(buttons[2]['x'],buttons[2]['y']))
                        screen.blit(mouse,(mx,my))
                        pygame.display.update()
                        fpsclock.tick(FPS)
                        psx,psy=buttons[2]['x'],buttons[2]['y']
                        choosenplayerconstant=avatarconstant
                        choosenplayerupthrust=avatarupthrust
                        choosenplayerlowthrust=avatarlowthrust
                        choosenplayerscating=avatarscating
                        choosenplayerdead=avatardead
                        #police
                    elif buttons[3]['state']:#checks back to main menu
                        buttonclickedsound.play()
                        screen.blit(buttons[3]['name'][2],(buttons[3]['x'],buttons[3]['y']))
                        screen.blit(mouse,(mx,my))
                        pygame.display.update()
                        fpsclock.tick(FPS)
                        buttons=Buttonsmenu
                        _Playermenu=False

                elif buttons==Buttonsetting:#------------------settings
                    if buttons[0]['state']:#checks sounds
                        buttonclickedsound.play()
                        screen.blit(buttons[0]['name'][2],(buttons[0]['x'],buttons[0]['y']))
                        screen.blit(mouse,(mx,my))
                        pygame.display.update()
                        fpsclock.tick(FPS)
                        buttons=Buttonsounds
                    elif buttons[1]['state']:#checks score
                        buttonclickedsound.play()
                        screen.blit(buttons[1]['name'][2],(buttons[1]['x'],buttons[1]['y']))
                        screen.blit(mouse,(mx,my))
                        pygame.display.update()
                        fpsclock.tick(FPS)
                        buttons=Buttonabout
                        Showhighscore=True
                    elif buttons[2]['state']:#checks about
                        buttonclickedsound.play()
                        screen.blit(buttons[2]['name'][2],(buttons[2]['x'],buttons[2]['y']))
                        screen.blit(mouse,(mx,my))
                        pygame.display.update()
                        fpsclock.tick(FPS)
                        buttons=Buttonabout
                        Showabout=True
                    elif buttons[3]['state']:#checks back to main menu
                        buttonclickedsound.play()
                        screen.blit(buttons[3]['name'][2],(buttons[3]['x'],buttons[3]['y']))
                        screen.blit(mouse,(mx,my))
                        pygame.display.update()
                        fpsclock.tick(FPS)
                        buttons=Buttonsmenu
                elif buttons==Buttonsounds:#----------------sounds
                    if buttons[0]['state']:#checks music
                        buttonclickedsound.play()
                        if Musicon:
                            buttons[0]['name']=musicoffbutton
                            Musicon=False
                        else:
                            buttons[0]['name']=musiconbutton
                            Musicon=True                       
                    elif buttons[1]['state']:#checks vfx
                        buttonclickedsound.play()
                        if Vfxon:
                            buttons[1]['name']=vfxoffbutton
                            Vfxon=False
                        else:
                            buttons[1]['name']=vfxonbutton
                            Vfxon=True   
                    elif buttons[2]['state']:#checks back to settings
                        buttonclickedsound.play()
                        screen.blit(buttons[2]['name'][2],(buttons[2]['x'],buttons[2]['y']))
                        screen.blit(mouse,(mx,my))
                        pygame.display.update()
                        fpsclock.tick(FPS)
                        buttons=Buttonsetting
                elif buttons==Buttonabout:#--------------about
                     if buttons[0]['state']:#checks back to settings
                        buttonclickedsound.play()
                        screen.blit(buttons[0]['name'][2],(buttons[0]['x'],buttons[0]['y']))
                        screen.blit(mouse,(mx,my))
                        pygame.display.update()
                        fpsclock.tick(FPS)
                        Showabout=False
                        Showhighscore=False
                        buttons=Buttonsetting                        

        for j in range(len(Viruses)):
            if random.randint(0,1)==0:
                if random.randint(0,1)==0:
                    Viruses[j]['x']+=random.randint(0,2)
                else:
                    Viruses[j]['y']+=random.randint(0,2)
            else:
                if random.randint(0,1)==0:
                    Viruses[j]['x']-=random.randint(0,2)
                else:
                    Viruses[j]['y']-=random.randint(0,2)

            if Viruses[j]['x']<0:
                Viruses[j]['x']=0
            elif Viruses[j]['x']+Viruses[j]['width']>1280:
                Viruses[j]['x']=1280-Viruses[j]['width']
            if Viruses[j]['y']<0:
                Viruses[j]['y']=0
            elif Viruses[j]['y']+Viruses[j]['width']>720:
                Viruses[j]['y']=720-Viruses[j]['width']
                

        screen.blit(menubg,(0,0))#bg for menu page
        screen.blit(mouseshadow,(mx-10,my+10))#mouse shadow
        for k in range(len(Viruses)):
            screen.blit(Viruses[k]['virus'],(Viruses[k]['x'],Viruses[k]['y']))#blits all the viruses

        if Showabout:
            screen.blit(aboutgame,(0,0))
        if Showhighscore:
            screen.blit(_highscore,(390,295))
            hsx=(1280-((30*len(hslist))+30))/2
            for k in hslist:
                screen.blit(_numbers[k],(hsx,395))
                hsx+=30
            screen.blit(_m,(hsx,395))

        if _Playermenu:
            screen.blit(playerselected,(psx,psy))
        for k in range(len(buttons)):#blits buttons
            if buttons[k]['state']==False:
                screen.blit(buttons[k]['name'][0],(buttons[k]['x'],buttons[k]['y']))
            else:
                screen.blit(buttons[k]['name'][1],(buttons[k]['x'],buttons[k]['y']))
            
        screen.blit(mouse,(mx,my))#blits mouse
        
        if starting:#transition
            ti=transitionopen(ti)
            if ti>16:
                starting=False
                ti=0
                
        pygame.display.update()
        fpsclock.tick(FPS)
def show_score(Highscore,score,distlist):
    index=[0,1,2,3,4,5,6,7,8,9]
    nl=[]
    changetime=pygame.time.get_ticks()
    Change=True
    starting=True
    ti=0
    if Highscore<=score:
        HS=score
    else:
        HS=Highscore
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN and event.key==K_ESCAPE:
                transitionblind()
                return HS
        if Highscore<=score:
            if Change:
                nl=[]
                for i in range(10):
                    a=random.choice(index)
                    screen.blit(colours[a],(128*i,0))
                    index.remove(a)
                    nl.append(a)
                Change=False
                changetime=pygame.time.get_ticks()
                index=[0,1,2,3,4,5,6,7,8,9]
            else:
                a=0
                for i in nl:
                    screen.blit(colours[i],(128*a,0))
                    a+=1
                if pygame.time.get_ticks()>changetime+500:
                    Change=True
            screen.blit(_umadeahs,(440,285))

        else:
            screen.fill((255,255,255))
            
        pointx=(1280-((40*len(distlist))+45))/2
        for i in distlist:
            screen.blit(_Numbers[i],(pointx,330))
            pointx+=40
        screen.blit(_M,(pointx,330))

        screen.blit(escback,(1115,15))
        if starting:#transition
            ti=transitionopen(ti)
            if ti>16:
                starting=False
                ti=0
        
        pygame.display.update()
        fpsclock.tick(FPS)
    
        

        

def stableplayer():#player trying to be steady
    shake=1
    if random.randint(0,1)==0:
        stablex=random.randint(0,shake)
    else:
        stablex=-random.randint(0,shake)
    if random.randint(0,1)==0:
        stabley=random.randint(0,shake)
    else:
        stabley=-random.randint(0,shake)
    return stablex,stabley

def blastshake(shakemin,shakemax):#player hit by wood or giant virus
    if random.randint(0,1)==0:
        bshake=random.randint(shakemin,shakemax)
    else:
        bshake=-random.randint(shakemin,shakemax)
    return bshake

    

def sanitizercollected(playerpos,Sanitizerlist,Pocketitems):#sanitizer collection
    removeitem=[]
    for i in range(len(Sanitizerlist)):
        if Sanitizerlist[i]['x']+bottlew-50>playerpos['x']>Sanitizerlist[i]['x']-pw and Sanitizerlist[i]['y']+bottleh>playerpos['y']>Sanitizerlist[i]['y']-ph:
            if len(Pocketitems)<3:
                if len(Pocketitems)==0:
                    Pocketitems.append({'item':1,'selected':True})
                else:
                    Pocketitems.append({'item':1,'selected':False})
                removeitem.append(i)
                catchsound.play()
    removeitem.sort()
    passed=0
    for i in removeitem:
        Sanitizerlist.pop(i-passed)
        passed+=1
    return Sanitizerlist,Pocketitems

def vaccinecollected(playerpos,Vaccinelist,Pocketitems):#vaccine collection
    removeitem=[]
    for i in range(len(Vaccinelist)):
        if Vaccinelist[i]['x']+bottlew-50>playerpos['x']>Vaccinelist[i]['x']-pw and Vaccinelist[i]['y']+bottleh>playerpos['y']>Vaccinelist[i]['y']-ph:
            if len(Pocketitems)<3:
                if len(Pocketitems)==0:
                    Pocketitems.append({'item':0,'selected':True})
                else:
                    Pocketitems.append({'item':0,'selected':False})
                removeitem.append(i)
                catchsound.play()
    removeitem.sort()
    passed=0
    for i in removeitem:
        Vaccinelist.pop(i-passed)
        passed+=1
    return Vaccinelist,Pocketitems

def spraycollected(playerpos,Spraylist,Pocketitems):#spray collection
    removeitem=[]
    for i in range(len(Spraylist)):
        if Spraylist[i]['x']+bottlew-50>playerpos['x']>Spraylist[i]['x']-pw and Spraylist[i]['y']+bottleh>playerpos['y']>Spraylist[i]['y']-ph:
            if len(Pocketitems)<3:
                if len(Pocketitems)==0:
                    Pocketitems.append({'item':2,'selected':True})
                else:
                    Pocketitems.append({'item':2,'selected':False})
                removeitem.append(i)
                catchsound.play()
    removeitem.sort()
    passed=0
    for i in removeitem:
        Spraylist.pop(i-passed)
        passed+=1
    return Spraylist,Pocketitems

def ppekitcollected(playerpos,Ppekitlist,ppekiton,Vaccined,ppeprotectiontime,ppekittime,playerconstant,playerupthrust,playerlowthrust,playerscating,goup,godown,onroad,player,Showtimer,timerimg,speed):#ppekit collection
    removeitem=[]
    for i in range(len(Ppekitlist)):
        if Ppekitlist[i]['x']+ppew-50>playerpos['x']>Ppekitlist[i]['x']-pw and Ppekitlist[i]['y']+ppeh>playerpos['y']>Ppekitlist[i]['y']-ph:
            if not ppekiton:
                speed+=5
            ppekiton=True
            Vaccined=False
            Showtimer=True
            timerimg=ppetimer[10]
            ppeprotectiontime=pygame.time.get_ticks()
            ppekittime=pygame.time.get_ticks()
            
            playerconstant=ppekitconstant
            playerupthrust=ppekitupthrust
            playerlowthrust=ppekitlowthrust
            playerscating=ppekitscating
            if goup:
                player=playerupthrust
            if godown:
                player=ppekitlowthrust
            if onroad:
                player=playerscating
            else:
                player=playerconstant
            removeitem.append(i)
            catchsound.play()
    removeitem.sort()
    passed=0
    for i in removeitem:
        Ppekitlist.pop(i-passed)
        passed+=1
    return Ppekitlist,ppekiton,Vaccined,ppeprotectiontime,ppekittime,playerconstant,playerupthrust,playerlowthrust,playerscating,player,Showtimer,timerimg,speed

def coincollection(playerpos,Coinlist,Goldcollected,movegold):#coins collection
    removeitem=[]
    coin=0
    for i in range(len(Coinlist)):
        if Coinlist[i]['x']+cvw-50>playerpos['x']>Coinlist[i]['x']-pw and Coinlist[i]['y']+cvh>playerpos['y']>Coinlist[i]['y']-ph:
            coin+=1
            cx= (Coinlist[i]['x']-175)*25/math.sqrt( (Coinlist[i]['x']-175)**2 + (Coinlist[i]['y']-25)**2 )
            cy= (Coinlist[i]['y']-25)*25/math.sqrt( (Coinlist[i]['x']-175)**2 + (Coinlist[i]['y']-25)**2 )
            movegold.append({'x':Coinlist[i]['x'],'y':Coinlist[i]['y'],'cx':-cx,'cy':-cy})
            coincollectsound.play()
            removeitem.append(i)
    removeitem.sort()
    passed=0
    for i in removeitem:
        Coinlist.pop(i-passed)
        passed+=1
    Goldcollected+=coin
    gcoin=Goldcollected
    coinlist=[]
    for j in range(len(str(gcoin))):
        coinlist.insert(0,gcoin%10)
        gcoin=gcoin//10
    return Coinlist,Goldcollected,coinlist,movegold
    
def heartcollected(playerpos,Heartlist,life_,showbanner,showbannertime,pointbanner,lifeeff,lifeeffmid,healefflist):
    removeitem=[]
    for i in range(len(Heartlist)):
        if Heartlist[i]['x']+heartw-50>playerpos['x']>Heartlist[i]['x']-pw and Heartlist[i]['y']+hearth>playerpos['y']>Heartlist[i]['y']-ph:
            if life_<75:
                life_+=25
                lifeeff=((life_-1)*7)+1
                lifeeffmid=pygame.transform.scale(lifebarmid,(lifeeff,10))
            else:
                life_=100
                lifeeff=((life_-1)*7)+1
                lifeeffmid=pygame.transform.scale(lifebarmid,(lifeeff,10))
            healefflist.append({'index':0})
            healsound.play()
            showbanner=True
            pointbanner=healthplus25
            showbannertime=pygame.time.get_ticks()
            removeitem.append(i)
    removeitem.sort()
    passed=0
    for i in removeitem:
        Heartlist.pop(i-passed)
        passed+=1
    return Heartlist,life_,showbanner,showbannertime,pointbanner,lifeeff,lifeeffmid,healefflist

def hitbywood(Blast,blasttime,playerpos,Woodlist,life_,showbanner,showbannertime,pointbanner,lifeeff,lifeeffmid,woodbreaklist,ppekiton):
    removeitem=[]
    for i in range(len(Woodlist)):
        if Woodlist[i]['x']+woodw-50>playerpos['x']>Woodlist[i]['x']-pw and Woodlist[i]['y']+woodh>playerpos['y']>Woodlist[i]['y']-ph:
            if life_>25 and not ppekiton:
                life_-=25
                lifeeff=((life_-1)*7)+1
                lifeeffmid=pygame.transform.scale(lifebarmid,(lifeeff,10))
            elif not ppekiton:
                life_=0
            woodbreaklist.append({'x':Woodlist[i]['x']-5,'y':Woodlist[i]['y']-40,'index':0})
            if not ppekiton:
                showbanner=True
                pointbanner=healthminus25
                showbannertime=pygame.time.get_ticks()
            woodbreaksound.play()
            Blast=True
            blasttime=pygame.time.get_ticks()
            removeitem.append(i)
            
    removeitem.sort()
    passed=0
    for i in removeitem:
        Woodlist.pop(i-passed)
        passed+=1
    return Woodlist,life_,showbanner,showbannertime,pointbanner,lifeeff,lifeeffmid,woodbreaklist,Blast,blasttime
    

def hitbyvirus(playerpos,Viruslist,coronaeffect_,showbanner,showbannertime,pointbanner,coronaeff,ceffmid,Vaccined,ppekiton,affectefflist):
    removeitem=[]
    for i in range(len(Viruslist)):
        if Viruslist[i]['x']+cvw-50>playerpos['x']>Viruslist[i]['x']-pw and Viruslist[i]['y']+cvh>playerpos['y']>Viruslist[i]['y']-ph:
            if coronaeffect_<100 and not Vaccined and not ppekiton:
                coronaeffect_+=1
                coronaeff=((coronaeffect_-1)*8)+2
                ceffmid=pygame.transform.scale(cbarmid,(coronaeff,10))
            if not Vaccined and not ppekiton:
                affectefflist.append({'index':0})
                showbanner=True
                pointbanner=affectedplus1
                showbannertime=pygame.time.get_ticks()
            virusaffectsound.play()
            removeitem.append(i)
    removeitem.sort()
    passed=0
    for i in removeitem:
        Viruslist.pop(i-passed)
        passed+=1
    return Viruslist,coronaeffect_,showbanner,showbannertime,pointbanner,coronaeff,ceffmid,affectefflist


def hitbygiantvirus(Blast,blasttime,playerpos,Giantviruslist,coronaeffect_,showbanner,showbannertime,pointbanner,coronaeff,ceffmid,giantvirusexplodelist,Vaccined,ppekiton):
    removeitem=[]
    for i in range(len(Giantviruslist)):
        if Giantviruslist[i]['x']+giantw-50>playerpos['x']>Giantviruslist[i]['x']-pw and Giantviruslist[i]['y']+gianth>playerpos['y']>Giantviruslist[i]['y']-ph:
            if coronaeffect_<50 and not Vaccined and not ppekiton:
                coronaeffect_+=50
                coronaeff=((coronaeffect_-1)*8)+2
                ceffmid=pygame.transform.scale(cbarmid,(coronaeff,10))
            elif not Vaccined and not ppekiton:
                coronaeffect_=100
                coronaeff=((coronaeffect_-1)*8)+2
                ceffmid=pygame.transform.scale(cbarmid,(coronaeff,10))
            giantvirusexplodelist.append({'x':Giantviruslist[i]['x']-270,'y':Giantviruslist[i]['y']-300,'index':0})
            if not Vaccined and not ppekiton:
                showbanner=True
                pointbanner=affectedplus50
                showbannertime=pygame.time.get_ticks()
            giantvirusblastsound.play()
            Blast=True
            blasttime=pygame.time.get_ticks()
            removeitem.append(i)
    removeitem.sort()
    passed=0
    for i in removeitem:
        Giantviruslist.pop(i-passed)
        passed+=1
    return Giantviruslist,coronaeffect_,showbanner,showbannertime,pointbanner,coronaeff,ceffmid,giantvirusexplodelist,Blast,blasttime

def killsmallvirus(playerpos,Viruslist,virusexplodelist):
    X,Y=playerpos['x']+156,playerpos['y']
    removeitem=[]
    coin=0
    for i in range(len(Viruslist)):
        if Viruslist[i]['x']+cvw-50>X>Viruslist[i]['x']-65 and Viruslist[i]['y']+cvh>Y>Viruslist[i]['y']-100:
            virusexplodelist.append({'x':Viruslist[i]['x'],'y':Viruslist[i]['y']-10,'index':0})
            removeitem.append(i)
            viruskilledsound.play()
    removeitem.sort()
    passed=0
    for i in removeitem:
        Viruslist.pop(i-passed)
        passed+=1
    return Viruslist,virusexplodelist

def transitionblind():
    for i in range(16,-1,-1):
        screen.blit(transition[i],(0,0))
        pygame.display.update()
        fpsclock.tick(FPS)
    return
def transitionopen(ti):
    screen.blit(transition[ti],(0,0))
    return ti+1

def checkonbuttons(mx,my,buttons):#checks if mouse howers on any of the buttons
    for j in range(len(buttons)):
        if buttons[j]['x']<mx<buttons[j]['w']+buttons[j]['x'] and buttons[j]['y']<my<buttons[j]['h']+buttons[j]['y']:
            if buttons[j]['state'] !=True:
                onbuttonsound.play()
                buttons[j]['state']=True
        else:
            buttons[j]['state']=False
    return buttons
def WelcomeToCovidSurvivirs():
    introsound.play()
    ti=0
    Starting=True
    introtime=pygame.time.get_ticks()
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(GameBanner,(0,0))
        if Starting:
            ti=transitionopen(ti)
            if ti>16:
                Starting=False
        if pygame.time.get_ticks()>introtime+4000:
            transitionblind()
            menu()
        pygame.display.update()
        fpsclock.tick(FPS)
        
    

#menu images
GameBanner=pygame.image.load('sprites/images/menu/gameBanner.png')
Virus=(
    pygame.image.load('sprites/images/menu/virus1.png'),
    pygame.image.load('sprites/images/menu/virus2.png')
    )
menubg=pygame.image.load('sprites/images/menu/menubg.png')
mouse=pygame.image.load('sprites/images/menu/mouse.png')
mouseshadow=pygame.image.load('sprites/images/menu/mouseshadow.png')
aboutgame=pygame.image.load('sprites/images/menu/aboutgame.png')
startbutton=(
    pygame.image.load('sprites/images/menu/start.png'),
    pygame.image.load('sprites/images/menu/onstart.png'),
    pygame.image.load('sprites/images/menu/startclicked.png')
    )
playerbutton=(
    pygame.image.load('sprites/images/menu/player.png'),
    pygame.image.load('sprites/images/menu/onplayer.png'),
    pygame.image.load('sprites/images/menu/playerclicked.png')
    )
settingsbutton=(
    pygame.image.load('sprites/images/menu/settings.png'),
    pygame.image.load('sprites/images/menu/onsettings.png'),
    pygame.image.load('sprites/images/menu/settingsclicked.png')
    )
aboutbutton=(
    pygame.image.load('sprites/images/menu/about.png'),
    pygame.image.load('sprites/images/menu/onabout.png'),
    pygame.image.load('sprites/images/menu/aboutclicked.png')
    )
soundsbutton=(
    pygame.image.load('sprites/images/menu/sounds.png'),
    pygame.image.load('sprites/images/menu/onsounds.png'),
    pygame.image.load('sprites/images/menu/soundsclicked.png')
    )
scorebutton=(
    pygame.image.load('sprites/images/menu/score.png'),
    pygame.image.load('sprites/images/menu/onscore.png'),
    pygame.image.load('sprites/images/menu/scoreclicked.png')
    )
quitbutton=(
    pygame.image.load('sprites/images/menu/quit.png'),
    pygame.image.load('sprites/images/menu/onquit.png'),
    pygame.image.load('sprites/images/menu/quitclicked.png')
    )
backbutton=(
    pygame.image.load('sprites/images/menu/back.png'),
    pygame.image.load('sprites/images/menu/onback.png'),
    pygame.image.load('sprites/images/menu/backclicked.png')
    )


musiconbutton=(
    pygame.image.load('sprites/images/menu/musicon.png'),
    pygame.image.load('sprites/images/menu/onmusicon.png')
    )
musicoffbutton=(
    pygame.image.load('sprites/images/menu/musicoff.png'),
    pygame.image.load('sprites/images/menu/onmusicoff.png')
    )
vfxonbutton=(
    pygame.image.load('sprites/images/menu/vfxon.png'),
    pygame.image.load('sprites/images/menu/onvfxon.png')
    )
vfxoffbutton=(
    pygame.image.load('sprites/images/menu/vfxoff.png'),
    pygame.image.load('sprites/images/menu/onvfxoff.png')
    )

avatarbutton=(
    pygame.image.load('sprites/images/menu/player1.png'),
    pygame.image.load('sprites/images/menu/onplayer1.png'),
    pygame.image.load('sprites/images/menu/player1clicked.png')
    )
doctorbutton=(
    pygame.image.load('sprites/images/menu/player1.png'),
    pygame.image.load('sprites/images/menu/onplayer1.png'),
    pygame.image.load('sprites/images/menu/player1clicked.png')
    )
policebutton=(
    pygame.image.load('sprites/images/menu/player1.png'),
    pygame.image.load('sprites/images/menu/onplayer1.png'),
    pygame.image.load('sprites/images/menu/player1clicked.png')
    )
playerselected=pygame.image.load('sprites/images/menu/playerselected.png')
#background images
wall=(
    pygame.image.load('sprites/images/bg/walls1.png'),
    pygame.image.load('sprites/images/bg/walls2.png'),
    pygame.image.load('sprites/images/bg/walls3.png'),
    pygame.image.load('sprites/images/bg/walls4.png')
    )
bottomroad=(
    pygame.image.load('sprites/images/bg/road1.png'),
    pygame.image.load('sprites/images/bg/road2.png'),
    pygame.image.load('sprites/images/bg/road3.png'),
    pygame.image.load('sprites/images/bg/road4.png')
    )
topbrick=(
    pygame.transform.flip(pygame.image.load('sprites/images/bg/brick1.png'),False,True),
    pygame.transform.flip(pygame.image.load('sprites/images/bg/brick2.png'),False,True),
    pygame.transform.flip(pygame.image.load('sprites/images/bg/brick3.png'),False,True),
    pygame.transform.flip(pygame.image.load('sprites/images/bg/brick4.png'),False,True)
    )
#number images
_numbers=(
    pygame.image.load('sprites/images/menu/numbers/0.png'),
    pygame.image.load('sprites/images/menu/numbers/1.png'),
    pygame.image.load('sprites/images/menu/numbers/2.png'),
    pygame.image.load('sprites/images/menu/numbers/3.png'),
    pygame.image.load('sprites/images/menu/numbers/4.png'),
    pygame.image.load('sprites/images/menu/numbers/5.png'),
    pygame.image.load('sprites/images/menu/numbers/6.png'),
    pygame.image.load('sprites/images/menu/numbers/7.png'),
    pygame.image.load('sprites/images/menu/numbers/8.png'),
    pygame.image.load('sprites/images/menu/numbers/9.png')
    )
_Numbers=(
    pygame.image.load('sprites/images/menu/numbers/number0.png'),
    pygame.image.load('sprites/images/menu/numbers/number1.png'),
    pygame.image.load('sprites/images/menu/numbers/number2.png'),
    pygame.image.load('sprites/images/menu/numbers/number3.png'),
    pygame.image.load('sprites/images/menu/numbers/number4.png'),
    pygame.image.load('sprites/images/menu/numbers/number5.png'),
    pygame.image.load('sprites/images/menu/numbers/number6.png'),
    pygame.image.load('sprites/images/menu/numbers/number7.png'),
    pygame.image.load('sprites/images/menu/numbers/number8.png'),
    pygame.image.load('sprites/images/menu/numbers/number9.png')
    )
_umadeahs=pygame.image.load('sprites/images/menu/numbers/hs.png')
_M=pygame.image.load('sprites/images/menu/numbers/M_.png')
_x=pygame.image.load('sprites/images/menu/numbers/x.png')
_km=pygame.image.load('sprites/images/menu/numbers/km.png')
_m=pygame.image.load('sprites/images/menu/numbers/m.png')
_highscore=pygame.image.load('sprites/images/menu/highscore.png')
#countdown
countdown=(
    pygame.image.load('sprites/images/items/countdown3.png'),
    pygame.image.load('sprites/images/items/countdown2.png'),
    pygame.image.load('sprites/images/items/countdown1.png')
    )
survive=pygame.image.load('sprites/images/items/survive.png')
#healthbar
healthbar=pygame.image.load('sprites/images/items/healthbar.png')
lifebarstart=pygame.image.load('sprites/images/items/lifebarstart.png')
lifebarmid=pygame.image.load('sprites/images/items/lifebarmid.png')
lifebarend=pygame.image.load('sprites/images/items/lifebarend.png')
cbarstart=pygame.image.load('sprites/images/items/cbarstart.png')
cbarmid=pygame.image.load('sprites/images/items/cbarmid.png')
cbarend=pygame.image.load('sprites/images/items/cbarend.png')
#escape hint
escback=pygame.image.load('sprites/images/items/escback.png')
#game collection items
goldcoin=(#goldcoin
    pygame.image.load('sprites/images/items/coin/coin1.png'),
    pygame.image.load('sprites/images/items/coin/coin2.png'),
    pygame.image.load('sprites/images/items/coin/coin3.png'),
    pygame.image.load('sprites/images/items/coin/coin4.png'),
    pygame.image.load('sprites/images/items/coin/coin5.png'),
    pygame.image.load('sprites/images/items/coin/coin6.png'),
    pygame.image.load('sprites/images/items/coin/coin7.png'),
    pygame.image.load('sprites/images/items/coin/coin8.png')
    )

smallvirus=pygame.image.load('sprites/images/items/virus/virus.png')#small virus
virusdead=(
    pygame.image.load('sprites/images/items/virus/virusdead1.png'),
    pygame.image.load('sprites/images/items/virus/virusdead2.png'),
    pygame.image.load('sprites/images/items/virus/virusdead3.png'),
    pygame.image.load('sprites/images/items/virus/virusdead4.png'),
    pygame.image.load('sprites/images/items/virus/virusdead5.png'),
    pygame.image.load('sprites/images/items/virus/virusdead6.png'),
    pygame.image.load('sprites/images/items/virus/virusdead7.png'),
    pygame.image.load('sprites/images/items/virus/virusdead8.png')
    )
affectedeffect=(
    pygame.image.load('sprites/images/items/virus/affected1.png'),
    pygame.image.load('sprites/images/items/virus/affected2.png'),
    pygame.image.load('sprites/images/items/virus/affected3.png'),
    pygame.image.load('sprites/images/items/virus/affected4.png'),
    pygame.image.load('sprites/images/items/virus/affected5.png'),
    pygame.image.load('sprites/images/items/virus/affected6.png')
    )

giantvirus=(#giant virus
    pygame.image.load('sprites/images/items/virus/giantvirus1.png'),
    pygame.image.load('sprites/images/items/virus/giantvirus2.png'),
    pygame.image.load('sprites/images/items/virus/giantvirus3.png'),
    pygame.image.load('sprites/images/items/virus/giantvirus4.png')
    )
giantvirusexplode=(
    pygame.image.load('sprites/images/items/virus/giantvirusexplode1.png'),
    pygame.image.load('sprites/images/items/virus/giantvirusexplode2.png'),
    pygame.image.load('sprites/images/items/virus/giantvirusexplode3.png'),
    pygame.image.load('sprites/images/items/virus/giantvirusexplode4.png'),
    pygame.image.load('sprites/images/items/virus/giantvirusexplode5.png'),
    pygame.image.load('sprites/images/items/virus/giantvirusexplode6.png'),
    pygame.image.load('sprites/images/items/virus/giantvirusexplode7.png'),
    pygame.image.load('sprites/images/items/virus/giantvirusexplode8.png'),
    pygame.image.load('sprites/images/items/virus/giantvirusexplode9.png')
    )
collectppekit=pygame.image.load('sprites/images/items/ppekit.png')#ppe kit
collectsanitizer=pygame.image.load('sprites/images/items/sanitizer.png')#sanitizer
collectspray=pygame.image.load('sprites/images/items/spray.png')#spray
collectvaccine=pygame.image.load('sprites/images/items/vaccine.png')#vaccine
collectheart=pygame.image.load('sprites/images/items/heart.png')

aleart=pygame.image.load('sprites/images/items/aleart.png')#aleart

healeffect=(
    pygame.image.load('sprites/images/items/heal effect/heal1.png'),
    pygame.image.load('sprites/images/items/heal effect/heal2.png'),
    pygame.image.load('sprites/images/items/heal effect/heal3.png'),
    pygame.image.load('sprites/images/items/heal effect/heal4.png'),
    pygame.image.load('sprites/images/items/heal effect/heal5.png'),
    pygame.image.load('sprites/images/items/heal effect/heal6.png'),
    pygame.image.load('sprites/images/items/heal effect/heal7.png'),
    pygame.image.load('sprites/images/items/heal effect/heal8.png'),
    pygame.image.load('sprites/images/items/heal effect/heal9.png'),
    pygame.image.load('sprites/images/items/heal effect/heal10.png'),
    pygame.image.load('sprites/images/items/heal effect/heal11.png'),
    pygame.image.load('sprites/images/items/heal effect/heal12.png')
    )

healthminus25=pygame.image.load('sprites/images/items/health-25.png')
healthplus25=pygame.image.load('sprites/images/items/health+25.png')
affectedplus1=pygame.image.load('sprites/images/items/affected+1.png')
affectedplus50=pygame.image.load('sprites/images/items/affected+50.png')
affectedminus50=pygame.image.load('sprites/images/items/affected-50.png')
affectedminus100=pygame.image.load('sprites/images/items/affected-100.png')

wood=pygame.image.load('sprites/images/items/wood/wood.png')#wood
woodbreak=(
    pygame.image.load('sprites/images/items/wood/woodbreak1.png'),
    pygame.image.load('sprites/images/items/wood/woodbreak2.png'),
    pygame.image.load('sprites/images/items/wood/woodbreak3.png'),
    pygame.image.load('sprites/images/items/wood/woodbreak4.png'),
    pygame.image.load('sprites/images/items/wood/woodbreak5.png'),
    pygame.image.load('sprites/images/items/wood/woodbreak6.png'),
    pygame.image.load('sprites/images/items/wood/woodbreak7.png'),
    pygame.image.load('sprites/images/items/wood/woodbreak8.png'),
    pygame.image.load('sprites/images/items/wood/woodbreak9.png')
    )

transition=(
    pygame.image.load('sprites/images/transition/transition1.png'),
    pygame.image.load('sprites/images/transition/transition2.png'),
    pygame.image.load('sprites/images/transition/transition3.png'),
    pygame.image.load('sprites/images/transition/transition4.png'),
    pygame.image.load('sprites/images/transition/transition5.png'),
    pygame.image.load('sprites/images/transition/transition6.png'),
    pygame.image.load('sprites/images/transition/transition7.png'),
    pygame.image.load('sprites/images/transition/transition8.png'),
    pygame.image.load('sprites/images/transition/transition9.png'),
    pygame.image.load('sprites/images/transition/transition10.png'),
    pygame.image.load('sprites/images/transition/transition11.png'),
    pygame.image.load('sprites/images/transition/transition12.png'),
    pygame.image.load('sprites/images/transition/transition13.png'),
    pygame.image.load('sprites/images/transition/transition14.png'),
    pygame.image.load('sprites/images/transition/transition15.png'),
    pygame.image.load('sprites/images/transition/transition16.png'),
    pygame.image.load('sprites/images/transition/transition17.png')
    )
colours=(
    pygame.image.load('sprites/images/transition/colours1.png'),
    pygame.image.load('sprites/images/transition/colours2.png'),
    pygame.image.load('sprites/images/transition/colours3.png'),
    pygame.image.load('sprites/images/transition/colours4.png'),
    pygame.image.load('sprites/images/transition/colours5.png'),
    pygame.image.load('sprites/images/transition/colours6.png'),
    pygame.image.load('sprites/images/transition/colours7.png'),
    pygame.image.load('sprites/images/transition/colours8.png'),
    pygame.image.load('sprites/images/transition/colours9.png'),
    pygame.image.load('sprites/images/transition/colours10.png')
    )

#pocket
pocket=pygame.image.load('sprites/images/items/pocket.png')
onpocketitem=pygame.image.load('sprites/images/items/onpocketitem.png')
sanitizerlogo=pygame.image.load('sprites/images/items/sanitizerlogo.png')
vaccinelogo=pygame.image.load('sprites/images/items/vaccinelogo.png')
spraylogo=pygame.image.load('sprites/images/items/spraylogo.png')
sanitizerbottle=pygame.image.load('sprites/images/items/sanitizer.png')
handrub=(#handrub
    pygame.image.load('sprites/images/items/handrub/handrub1.png'),
    pygame.image.load('sprites/images/items/handrub/handrub2.png'),
    pygame.image.load('sprites/images/items/handrub/handrub3.png'),
    pygame.image.load('sprites/images/items/handrub/handrub4.png'),
    pygame.image.load('sprites/images/items/handrub/handrub5.png'),
    pygame.image.load('sprites/images/items/handrub/handrub6.png'),
    pygame.image.load('sprites/images/items/handrub/handrub7.png'),
    pygame.image.load('sprites/images/items/handrub/handrub8.png'),
    pygame.image.load('sprites/images/items/handrub/handrub9.png'),
    pygame.image.load('sprites/images/items/handrub/handrub10.png'),
    pygame.image.load('sprites/images/items/handrub/handrub11.png'),
    pygame.image.load('sprites/images/items/handrub/handrub12.png')
    )
emptysanitizer=pygame.image.load('sprites/images/items/handrub/emptysanitizer.png')
spraybottle=pygame.image.load('sprites/images/items/spray.png')
spraying=(#spraying
    pygame.image.load('sprites/images/items/spray/spraying1.png'),
    pygame.image.load('sprites/images/items/spray/spraying2.png'),
    pygame.image.load('sprites/images/items/spray/spraying3.png'),
    pygame.image.load('sprites/images/items/spray/spraying4.png'),
    pygame.image.load('sprites/images/items/spray/spraying5.png'),
    pygame.image.load('sprites/images/items/spray/spraying6.png'),
    pygame.image.load('sprites/images/items/spray/spraying7.png'),
    pygame.image.load('sprites/images/items/spray/spraying8.png'),
    pygame.image.load('sprites/images/items/spray/spraying9.png'),
    pygame.image.load('sprites/images/items/spray/spraying10.png')
    )
splashes=(
    pygame.image.load('sprites/images/items/spray/splash1.png'),
    pygame.image.load('sprites/images/items/spray/splash2.png'),
    pygame.image.load('sprites/images/items/spray/splash3.png'),
    pygame.image.load('sprites/images/items/spray/splash4.png'),
    pygame.image.load('sprites/images/items/spray/splash5.png'),
    pygame.image.load('sprites/images/items/spray/splash6.png'),
    pygame.image.load('sprites/images/items/spray/splash7.png'),
    pygame.image.load('sprites/images/items/spray/splash8.png')
    )
emptyspray=(
    pygame.image.load('sprites/images/items/spray/emptyspray6.png'),
    pygame.image.load('sprites/images/items/spray/emptyspray5.png'),
    pygame.image.load('sprites/images/items/spray/emptyspray4.png'),
    pygame.image.load('sprites/images/items/spray/emptyspray3.png'),
    pygame.image.load('sprites/images/items/spray/emptyspray2.png'),
    pygame.image.load('sprites/images/items/spray/emptyspray1.png')
    )
vaccinebottle=pygame.image.load('sprites/images/items/vaccine.png')
emptyvaccine=pygame.image.load('sprites/images/items/emptyvaccine.png')


distanceicon=pygame.image.load('sprites/images/items/distanceicon.png')
coinicon=pygame.image.load('sprites/images/items/coinicon.png')

#scateboard image
scateboard=(
    pygame.image.load('sprites/images/player/scateboard1.png'),
    pygame.image.load('sprites/images/player/scateboard2.png'),
    pygame.image.load('sprites/images/player/scateboard3.png'),
    pygame.image.load('sprites/images/player/scateboard4.png')
    )
#player images

#avatar
avatarconstant=(
    pygame.image.load('sprites/images/player/playerconstant1.png'),
    pygame.image.load('sprites/images/player/playerconstant2.png'),
    pygame.image.load('sprites/images/player/playerconstant3.png'),
    pygame.image.load('sprites/images/player/playerconstant4.png')
    )
avatarupthrust=(
    pygame.image.load('sprites/images/player/playerupthrust1.png'),
    pygame.image.load('sprites/images/player/playerupthrust2.png'),
    pygame.image.load('sprites/images/player/playerupthrust3.png'),
    pygame.image.load('sprites/images/player/playerupthrust4.png')
    )
avatarlowthrust=(
    pygame.image.load('sprites/images/player/playerlowthrust1.png'),
    pygame.image.load('sprites/images/player/playerlowthrust2.png'),
    pygame.image.load('sprites/images/player/playerlowthrust3.png'),
    pygame.image.load('sprites/images/player/playerlowthrust4.png')
    )
avatarscating=(
    pygame.image.load('sprites/images/player/playerscating1.png'),
    pygame.image.load('sprites/images/player/playerscating2.png'),
    pygame.image.load('sprites/images/player/playerscating3.png'),
    pygame.image.load('sprites/images/player/playerscating4.png')
    )
avatardead=pygame.image.load('sprites/images/player/deadplayer.png')
#ppekit
ppekitconstant=(
    pygame.image.load('sprites/images/player/ppekitconstant1.png'),
    pygame.image.load('sprites/images/player/ppekitconstant2.png'),
    pygame.image.load('sprites/images/player/ppekitconstant3.png'),
    pygame.image.load('sprites/images/player/ppekitconstant4.png')
    )
ppekitupthrust=(
    pygame.image.load('sprites/images/player/ppekitupthrust1.png'),
    pygame.image.load('sprites/images/player/ppekitupthrust2.png'),
    pygame.image.load('sprites/images/player/ppekitupthrust3.png'),
    pygame.image.load('sprites/images/player/ppekitupthrust4.png')
    )
ppekitlowthrust=(
    pygame.image.load('sprites/images/player/ppekitlowthrust1.png'),
    pygame.image.load('sprites/images/player/ppekitlowthrust2.png'),
    pygame.image.load('sprites/images/player/ppekitlowthrust3.png'),
    pygame.image.load('sprites/images/player/ppekitlowthrust4.png')
    )
ppekitscating=(
    pygame.image.load('sprites/images/player/ppekitscating1.png'),
    pygame.image.load('sprites/images/player/ppekitscating2.png'),
    pygame.image.load('sprites/images/player/ppekitscating3.png'),
    pygame.image.load('sprites/images/player/ppekitscating4.png')
    )
#ppekitprotection
ppekitprotectionup=(
    pygame.image.load('sprites/images/player/ppekitprotectionup1.png'),
    pygame.image.load('sprites/images/player/ppekitprotectionup2.png'),
    pygame.image.load('sprites/images/player/ppekitprotectionup3.png'),
    pygame.image.load('sprites/images/player/ppekitprotectionup4.png'),
    pygame.image.load('sprites/images/player/ppekitprotectionup5.png'),
    pygame.image.load('sprites/images/player/ppekitprotectionup6.png'),
    pygame.image.load('sprites/images/player/ppekitprotectionup7.png'),
    pygame.image.load('sprites/images/player/ppekitprotectionup8.png'),
    pygame.image.load('sprites/images/player/ppekitprotectionup9.png'),
    pygame.image.load('sprites/images/player/ppekitprotectionup10.png')
    )
ppekitprotectiondown=(
    pygame.image.load('sprites/images/player/ppekitprotectiondown1.png'),
    pygame.image.load('sprites/images/player/ppekitprotectiondown2.png'),
    pygame.image.load('sprites/images/player/ppekitprotectiondown3.png'),
    pygame.image.load('sprites/images/player/ppekitprotectiondown4.png'),
    pygame.image.load('sprites/images/player/ppekitprotectiondown5.png'),
    pygame.image.load('sprites/images/player/ppekitprotectiondown6.png'),
    pygame.image.load('sprites/images/player/ppekitprotectiondown7.png'),
    pygame.image.load('sprites/images/player/ppekitprotectiondown8.png'),
    pygame.image.load('sprites/images/player/ppekitprotectiondown9.png'),
    pygame.image.load('sprites/images/player/ppekitprotectiondown10.png')
    )
vaccineprotectionup=(
    pygame.image.load('sprites/images/player/vaccineprotectionup1.png'),
    pygame.image.load('sprites/images/player/vaccineprotectionup2.png'),
    pygame.image.load('sprites/images/player/vaccineprotectionup3.png'),
    pygame.image.load('sprites/images/player/vaccineprotectionup4.png'),
    pygame.image.load('sprites/images/player/vaccineprotectionup5.png'),
    pygame.image.load('sprites/images/player/vaccineprotectionup6.png'),
    pygame.image.load('sprites/images/player/vaccineprotectionup7.png'),
    pygame.image.load('sprites/images/player/vaccineprotectionup8.png'),
    pygame.image.load('sprites/images/player/vaccineprotectionup9.png'),
    pygame.image.load('sprites/images/player/vaccineprotectionup10.png')
    )
vaccineprotectiondown=(
    pygame.image.load('sprites/images/player/vaccineprotectiondown1.png'),
    pygame.image.load('sprites/images/player/vaccineprotectiondown2.png'),
    pygame.image.load('sprites/images/player/vaccineprotectiondown3.png'),
    pygame.image.load('sprites/images/player/vaccineprotectiondown4.png'),
    pygame.image.load('sprites/images/player/vaccineprotectiondown5.png'),
    pygame.image.load('sprites/images/player/vaccineprotectiondown6.png'),
    pygame.image.load('sprites/images/player/vaccineprotectiondown7.png'),
    pygame.image.load('sprites/images/player/vaccineprotectiondown8.png'),
    pygame.image.load('sprites/images/player/vaccineprotectiondown9.png'),
    pygame.image.load('sprites/images/player/vaccineprotectiondown10.png')
    )
ppetimer=(
    pygame.image.load('sprites/images/items/timer/ppetimer0.png'),
    pygame.image.load('sprites/images/items/timer/ppetimer1.png'),
    pygame.image.load('sprites/images/items/timer/ppetimer2.png'),
    pygame.image.load('sprites/images/items/timer/ppetimer3.png'),
    pygame.image.load('sprites/images/items/timer/ppetimer4.png'),
    pygame.image.load('sprites/images/items/timer/ppetimer5.png'),
    pygame.image.load('sprites/images/items/timer/ppetimer6.png'),
    pygame.image.load('sprites/images/items/timer/ppetimer7.png'),
    pygame.image.load('sprites/images/items/timer/ppetimer8.png'),
    pygame.image.load('sprites/images/items/timer/ppetimer9.png'),
    pygame.image.load('sprites/images/items/timer/ppetimer10.png')
    )
vaccinetimer=(
    pygame.image.load('sprites/images/items/timer/vaccinetimer0.png'),
    pygame.image.load('sprites/images/items/timer/vaccinetimer1.png'),
    pygame.image.load('sprites/images/items/timer/vaccinetimer2.png'),
    pygame.image.load('sprites/images/items/timer/vaccinetimer3.png'),
    pygame.image.load('sprites/images/items/timer/vaccinetimer4.png'),
    pygame.image.load('sprites/images/items/timer/vaccinetimer5.png'),
    pygame.image.load('sprites/images/items/timer/vaccinetimer6.png'),
    pygame.image.load('sprites/images/items/timer/vaccinetimer7.png'),
    pygame.image.load('sprites/images/items/timer/vaccinetimer8.png'),
    pygame.image.load('sprites/images/items/timer/vaccinetimer9.png'),
    pygame.image.load('sprites/images/items/timer/vaccinetimer10.png')
    )



#audio
onbuttonsound=pygame.mixer.Sound('sprites/audio/oniconsound.wav')
buttonclickedsound=pygame.mixer.Sound('sprites/audio/buttonclick.wav')
alarmsound=pygame.mixer.Sound('sprites/audio/alarm.wav')
coincollectsound=pygame.mixer.Sound('sprites/audio/coin collect.wav')
giantvirusblastsound=pygame.mixer.Sound('sprites/audio/giantvirusblast.wav')
viruskilledsound=pygame.mixer.Sound('sprites/audio/viruskilled.wav')
healsound=pygame.mixer.Sound('sprites/audio/heal.wav')
hurtsound=pygame.mixer.Sound('sprites/audio/hurt.wav')
pointsound=pygame.mixer.Sound('sprites/audio/point.wav')
catchsound=pygame.mixer.Sound('sprites/audio/catch.wav')
woodbreaksound=pygame.mixer.Sound('sprites/audio/woodbreak.wav')
virusaffectsound=pygame.mixer.Sound('sprites/audio/virusaffect.wav')
sanitizingsound=pygame.mixer.Sound('sprites/audio/sanitizing.wav')
countdownsound=pygame.mixer.Sound('sprites/audio/countdown.wav')
sprayingsound=pygame.mixer.Sound('sprites/audio/spraying.wav')
introsound=pygame.mixer.Sound('sprites/audio/introsound.wav')
bgmusic=pygame.mixer.Sound('sprites/audio/backgroundmusic.wav')


#global variables

ph,pw=100,70#player height and width
hearth,heartw=50,50#heart height,width
bottleh,bottlew=50,26#bottle height,width
ppeh,ppew=50,50#ppekit height,width
cvh,cvw=30,30#coin and smallvirus height,width
gianth,giantw=120,120#giantvirus height,width
splashh,splashw=100,120#spray splash height,width
woodh,woodw=120,30#wood height,width

WelcomeToCovidSurvivirs()

        
                
                
            
            
