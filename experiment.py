#!/usr/bin/env python2

import time

import requests
import rospy
from std_msgs.msg import String


def main():
    rospy.init_node("experiment")

    # Publish every second.
    pub = rospy.Publisher("foo", String, queue_size=1, latch=True)
    rospy.Timer(rospy.Duration(1), lambda f: pub.publish(str(time.time())))

    # Make a long blocking HTTP request.
    requests.get("http://localhost:8080")

    print("response")

    # Does it block publishing?  Nope.  Confirm that requests.get block this (main) thread, but other threads
    # may continue running.

    rospy.spin()


if __name__ == "__main__":
    main()
