import statistics
from datetime import datetime

telemetry_file_path = "./results/telemetry.txt"


def filter():
    file = open(telemetry_file_path, 'r')
    lines = file.readlines()

    l = []

    for line in lines:
        line = line.strip()
        if "ping" in line or "Pong" in line:
            if not "T:" in line and not "P:" in line and "[" in line:
                l.append(line+"\n")

    file.close()

    with open(f"{telemetry_file_path[:-4]}_filtered.txt", "w") as fp:
        fp.writelines(l)


def packet_loss():
    ping = 0
    pong = 0

    file = open(f"{telemetry_file_path[:-4]}_filtered.txt", "r")
    lines = file.readlines()
    for line in lines:
        if "ping" in line:
            ping += 1
        elif "Pong" in line:
            pong += 1

    ratio = ((ping - pong) / ping) * 100

    return ratio


def response_time():
    times = []

    file = open(f"{telemetry_file_path[:-4]}_filtered.txt", "r")
    lines = file.readlines()
    for i, line in enumerate(lines):
        if "Pong" in line:
            if "ping" in lines[i-1]:

                ping = datetime.strptime(
                    f'{lines[i-1][1:9]},{lines[i-1][10:13]}', '%H:%M:%S,%f')
                ping_ms = ping.timestamp() * 1000

                pong = datetime.strptime(
                    f'{line[1:9]},{line[10:13]}', '%H:%M:%S,%f')
                pong_ms = pong.timestamp() * 1000

                time = pong_ms - ping_ms
                times.append(time)

    with open(f"{telemetry_file_path[:-4]}_times.txt", "w") as fp:
        fp.write("\n".join(map(str, times)))

    return statistics.mean(times)


print("Reading " + telemetry_file_path, "...")
print("Filtering...")

filter()

print("Packet loss:", packet_loss()/2, "%")
print(f"Average response time: {response_time()} ms")
print(f"Times exported to {telemetry_file_path[:-4]}_times.txt")
