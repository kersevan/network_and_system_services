mosquitto_pub -h proxy50.rt3.io:30967 -t 'test' -m 'jel me cujes?'


mosquitto_pub -h maqiatto.com -t "gregor.kersevan@gmail.com/test" -u "gregor.kersevan@gmail.com" -P "srsisrsi" -p 1883 -i "topic1asdf" -m "jel me cujes?"


Latency is the time it takes for a single data packet to travel to a destination. Typically, latency is measured in terms of roundtrip latency, since measuring one-way latency would require tight time synchronization and the ability to instrument both sides of the Internet path. Latency generally increases with distance, due to factors such as the speed of light for optical network segments; other factors can influence latency, including the amount of queueing or buffering along an end-to-end path, as well as the actual network path that traffic takes from one endpoint to another. TCP throughput is inversely proportional to end-to-end latency;31 all things being equal, then, a client will see a higher throughput to a nearby server than it will to a distant one.

Jitter is the variation between two latency measurements. Large jitter measurements are problematic.

If test duration is too short, the test will tend to underestimate throughput. As a result, accurate speed test tools must account for TCP slow start. Additionally, instantaneous TCP throughput continually varies because the sender tries to increase its transfer rate in an attempt to find and use any spare capacity (a process known as "additive increase multiplicative decrease" or AIMD).

----------------------------
VoIP Latency
VoIP latency is a common cause of low call quality. Sometimes called VoIP delay, VoIP latency is characterized by the length of time it takes for sound to exit the speaker’s mouth and reach the listener’s ear. You may recognize latency if you have ever heard an echo on a VoIP phone call or been on a Skype video-chat session where the words you hear are out of sync with the movement of the speaker’s lips.

There are three types of delay likely to occur in VoIP networks:

Propagation delays
Handling delays
Queueing delays

In computer networks, a propagation delay refers to the amount of time taken for the head of a signal to travel between the sender and the receiver. The delay is computed as a ratio, mapping link length and propagation speed over a specific medium. Mathematically, this type of delay is equal to d/s, where “s” is the wave propagation speed, and “d” is the distance.

The speed of light and of electrons traveling through copper or fiber plays a key part in creating this delay. For example, a fiber network stretching 13,000 miles would generate a delay of 70 milliseconds. This delay is generally imperceptible to the human ear, but when combined with handling delays, propagation delays can cause noticeable call quality issues.

Handling delays are another of the most common VoIP network delays. A handling delay is caused by devices forwarding the frame through the network and can have an impact on standard phone networks. In packetized environments, these delays cause significant issues.

Lastly, there are queuing delays. If there’s too much congestion, several packets might be held in a queue. This happens when more packets are sent out than the interface can manage at a given 