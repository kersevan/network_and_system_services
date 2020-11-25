import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import sched, time


auth = {
    'username':"gregor.kersevan@gmail.com",
    'password':"srsisrsi"
}

def publish_mqtt(temp):
    publish.single("gregor.kersevan@gmail.com/test", payload=temp, qos=0, 
    retain=False, hostname="maqiatto.com", port=1883, client_id="lalal",
    keepalive=60, will=None, auth=auth, tls=None,
    protocol=mqtt.MQTTv311, transport="tcp")
    s.enter(10, 1, publish_mqtt, (temp+1,))
    s.run()

s = sched.scheduler(time.time, time.sleep)
publish_mqtt(0)
