log_lines = [
    "Failed password for admin from 192.0.2.50",
    "Accepted password for user from 198.52.100.40",
    "Failed password for root from 192.0.2.50",
    "Failed password for admin from 203.0.113.70",
    "Failed password for guest from 192.0.2.50"
    ]

print(log_lines) #prints the entire list

for line in log_lines:
    print(line) #prints line separately 

for line in log_lines:
    if "Failed password" in line:
        print(line)

failed_logins = {}
ip = "192.0.2.50"

if ip in failed_logins:
    failed_logins[ip] = failed_logins[ip] + 1
else:
    failed_logins[ip] = 1

print(failed_logins)

line = "Failed password for admin from 192.0.2.50"

parts= line.split() #split ip address fron the line
ip = parts[-1]

print(ip)

for line in log_lines: #print ips of all attempts
    parts = line.split()
    ip = parts[-1]
    print(ip)

for line in log_lines: #print ips of failed passwords
    if "Failed password" in line:
        parts = line.split()
        ip = parts[-1]
        print(ip) 

failed_logins ={} #ip address counting

for line in log_lines:
    if "Failed password" in line:
        parts = line.split()
        ip = parts[-1]

        if ip in failed_logins:
            failed_logins[ip] = failed_logins[ip] + 1
        else:
            failed_logins[ip] = 1

print(failed_logins)                

threshold = 3 #login attempt alert

for ip, attempts in failed_logins.items():
    if attempts >= threshold:
        print("SECURITY ALERT:", ip, "has", attempts, "failed login attempts")
    else:
        print("NORMAL:", ip, "has", attempts, "failed login attempts")