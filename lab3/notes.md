# Lab 3: Adaptive Video and QoS

## Part 1: Analyse MPD file and get acquainted with adaptation algorithms

DASH = dynamic adaptive streaming over HTTP
MPD = media presentation description - It is a manifest file for MPEG DASH streaming

Identify the fields in http://www.digitalprimates.net/dash/streams/gpac/mp4-main-multi-mpd-AV-NBS.mpd

Q: How many video and audio codecs are available?
A: 
- mimeType="video/mp4" codecs="avc1.42c00d"
- mimeType="video/mp4" codecs="avc1.42c01e"
- mimeType="video/mp4" codecs="avc1.42c01f"
- mimeType="video/mp4" codecs="avc1.42c028"
- mimeType="audio/mp4" codecs="mp4a.40.2" bandwidth="19079"
- mimeType="audio/mp4" codecs="mp4a.40.2" bandwidth="66378"

Q: Which is the segment size?
A: 
- 87263 kbit (what I get by downloading a segment, others are between 60 and 90 mbits)?
- 50877/60  = 847.95 (bandwidth="50877" and there are 60 segments) + need to take into consideration the length of each segment in seconds

Q: Which audio and video datarates are available?
A: Are here meant the datarates?
- bandwidth="50877"
- bandwidth="194870"
- bandwidth="514828"
- bandwidth="770699"
- bandwidth="19079"
- bandwidth="66378"

Q: Which options would you have for an available bandwidth of 500kbps, 1.5Mbps, 10Mbps?
A:
