import random
import sys
import time
import os
import shodan

yellow = '\033[93m'
zebi1 = ('\033[31m'"""
    ______ _                           ___  ___          _            
    | ___ \ |                          |  \/  |         | |           
    | |_/ / |__   ___  _ __   ___  ___ | .  . | __ _ ___| |_ ___ _ __ 
    |  __/| '_ \ / _ \| '_ \ / _ \/ __|| |\/| |/ _` / __| __/ _ \ '__|
    | |   | | | | (_) | | | |  __/\__ \| |  | | (_| \__ \ ||  __/ |   
    \_|   |_| |_|\___/|_| |_|\___||___/\_|  |_/\__,_|___/\__\___|_|   
                                                                    
                                                                    
    """)

zebi3 = ('\033[31m'""" ,--^----------,--------,-----,-------^--,
 | |||||||||   `--------'     |          O      |PHONESMASTER>>>
 `+---------------------------^----------|           
   `\_,-------, _________________________|
     / XXXXXX /`|     /
    / XXXXXX /  `\   /
   / XXXXXX /\______(
  / XXXXXX /
 / XXXXXX /
(________(
 `------'


""")

zebi4 = ('\033[31m'"""                      ______
                   .-"      "-.
                  /            \-
                 |              |
                 |,  .-.  .-.  ,|
                 | )(_o/  \o_)( |
                 |/     /\     \|
       (@_       (_     ^^     _)
  _     ) \_______\__|IIIIII|__/__________________________
 (_)@8@8{}<________|-\IIIIII/-|___________________________>
        )_/        \          /
       (@           `--------`
""")

zebi5 = ('\033[31m'"""    ,           ,
   /             \-
  ((__-^^-,-^^-__))
   `-_---' `---_-'
    <__|o` 'o|__>
       \  `  /
        ): :(
        :o_o: |-PHONESMASTER-|
         "-"   """)
zebi6 = ("""               ...
             ;::::;
           ;::::; :;
         ;:::::'   :; |-PHONESMASTER-|
        ;:::::;     ;.
       ,:::::'       ;           OOO\-
       ::::::;       ;          OOOOO\-
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#""")

zebi7 = (""" ____________
< Phonemaster >
 ------------
       \   ,__,
        \  (oo)____
           (__)    )\-
              ||--|| *
""")

zebi2 = ("""
██████╗░██╗░░██╗░█████╗░███╗░░██╗███████╗███╗░░░███╗░█████╗░░██████╗████████╗███████╗██████╗░
██╔══██╗██║░░██║██╔══██╗████╗░██║██╔════╝████╗░████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██████╔╝███████║██║░░██║██╔██╗██║█████╗░░██╔████╔██║███████║╚█████╗░░░░██║░░░█████╗░░██████╔╝
██╔═══╝░██╔══██║██║░░██║██║╚████║██╔══╝░░██║╚██╔╝██║██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗
██║░░░░░██║░░██║╚█████╔╝██║░╚███║███████╗██║░╚═╝░██║██║░░██║██████╔╝░░░██║░░░███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝""")
banniere = (zebi1, zebi2, zebi3, zebi4, zebi5, zebi6, zebi7)
print(random.choice(banniere))
print('\033[33m'"""
       =[ PhonesMaster v1.0-dev      ]
+ -- --=[ Made by RistBS and matteo jo ]
+ -- --=[ Use help to show commands  ]
""")
print('\033[31m'"""[!] This tool is for educational purpose only, we'll not me responsible of your acts with it """)
def main():
   commande = input('\033[0m'"\n>> ")
   try:
       if commande == 'help':
           help()
           main()
       elif commande == 'help2':
           help2()
           main()
       elif commande == 'exit':
           exit("Bye Bye")
       elif commande == 'connect':
           device_connection()
       elif commande == 'shell':
           shell()
           #try:
                #'''FONCTION()'''
            #   except Exception as e:
             #      print(e)
       else:
           print("Commands not found")
           main()
   except KeyboardInterrupt:
       leaveMsg = input("\nif you leave you will loose all targets and connection, Are you sure ?[Y,N] : ")
       if leaveMsg == 'Y':
           sys.exit()
       else:
           main()
            

def help():
    print(yellow, """
    Command           Description
    -------           -----------
    connect           connect the target remotely                 
    exit              exit PhonesMaster                    
    disconnect        disconnect all the targets                   
    run               start sending the payload to get an access to the target               
    shell             open an android shell                
    verbose           get more details

""")

def device_connection():
     os.system("adb tcpip 5555")
     print ("\nEnter a phones ip address.")
     ip = input('PhonesMaster: IP >> ')
     os.system("adb connect "+ip+":5555")
     main()
        
def shell():
     print ("\nEnter the IP of the connected device")
     deviceIp = input('PhonesMaster: IP >> ')
     os.system("adb -s "+deviceIp+" shell")

def help2():
    print(yellow,"""\n    Command              Usage
     -------              -----------
    Uninstall           delete an app            
    ScreenShot          take a screenshot and save it on ur current direcotry  
    Dump all             
    Shell                 
    List apps             
    Install apk           
    Device off            
    Run an app            
    Exit                  
    Clear                 
    Next Page             
    Port Forwarding       
    NetStat               
    Grab wpa_supplicant   
    Turn WiFi On/Off      
    Show Mac              
    Remove Password       
    Extract apk           
    Battery               
    Activity              
""")
if __name__=='__main__':
    main()
