import os
import platform

def ping_internet():
    target = "8.8.8.8"
    print(f"Pinging {target}...")
    param = "-n" if platform.system().lower() == "windows" else "-c"
    response = os.system(f"ping {param} 4 {target}")
    if response == 0:
        print("Internet is reachable.")
    else:
        print("The Internet is down!")

def main():
    while True:
        command = input("Enter command: ").strip().lower()
        if command == "ping internet":
            ping_internet()
        elif command == "exit":
            print("Exiting.")
            break
        else:
            print("Unknown command. Try 'ping internet' or 'exit'.")

if __name__ == "__main__":
    main()
