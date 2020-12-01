import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import sched, time
import math
import datetime

auth = {
    'username':"gregor.kersevan@gmail.com",
    'password':"srsisrsi"
}
s = sched.scheduler(time.time, time.sleep)
start = 0
end = 0
numOTimes = 100
totalTime = 0
results = []

def calc_confifence_interval():
    mean = 0
    observations = len(results)
    z95 = 1.96
    variance = 0
    std_dev = 0
    for x in results:
        print(x)
        mean = mean + x
    mean = mean / observations
    for x in results:
        variance = variance + abs(x-mean) ** 2
    variance = variance / observations
    std_dev = math.sqrt(variance)

    print("Mean: %.2f" % mean)
    print("Variance: %.2f" % variance)
    print("Std dev: %.2f" % std_dev)
    lower = mean - (z95 * std_dev/math.sqrt(observations))
    upper = mean + (z95 * std_dev/math.sqrt(observations))
    print("The 95%% confidence interval is between %.2f ms and %.2f ms (%.2f ms +- %.2f%%)" % (lower, upper, mean, (upper-mean)/mean*100))
    
    f = open("portforwardResults.txt", "a")
    f.write("\n\n" + str(datetime.datetime.now()) + " Number of tests: " + str(observations))
    f.write("\nThe 95%% confidence interval is between %.2f ms and %.2f ms (%.2f ms +- %.2f%%)" % (lower, upper, mean, (upper-mean)/mean*100))
    f.close()
    
    quit()

def publish_mqtt(temp):
    global start
    start = time.time()
    publish.single("gregor.kersevan@gmail.com/test", payload=temp, qos=0, 
    retain=False, hostname="89.155.220.12", port=80, client_id="lalal",
    keepalive=60, will=None, auth=auth, tls=None,
    protocol=mqtt.MQTTv311, transport="tcp")
    # start = time.time()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("gregor.kersevan@gmail.com/test")


def on_message(client, userdata, msg):
    global results
    global numOTimes
    global start
    end = time.time()
    print("NumOfTimes: %d, Total time: %.2f ms" % (numOTimes, (end - start)*1000))
    message=msg.payload.decode('utf-8')
    print(msg.topic+" "+message)
    result = (end-start)*1000
    if result < 1000:
        numOTimes = numOTimes - 1
        results.append(result)
    if (numOTimes > 0):
        s.enter(0.5, 1, publish_mqtt, ("latency",))
        s.run()
    else:
        calc_confifence_interval()

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("89.155.220.12", 80, 60)
    client.username_pw_set("gregor.kersevan@gmail.com", "srsisrsi")
    client.loop_forever()
    publish_mqtt("latency")

    

    
    
