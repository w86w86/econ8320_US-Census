from datetime import datetime

def main():
    ourfile = "testhour.txt" 
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ourfile, 'a') as file:
        file.write(current_time + '\n')
      
    print(f"Current time written {current_time} in the file {ourfile}")

if __name__ == '__main__':
    main()
