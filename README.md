# Homework3 HRI - Ben Grudzien

This README only contains the instructions to run the system. The write-up explains this programs functionality.

## Instructions

**1)** In order to get the GEM simulation, clone this repository into your ROS workspace (Not into the package folder). Link: https://github.com/robustify/igvc_self_drive_sim

**2)** Run the commands to export the google application credentials and instantiate gcloud.

**3)** Run this command "roslaunch homework3 homework3.launch"

**4)** That's it, but note... the mic client is enabled by default. If you wish to disable it, go into the launch file and comment it out. It's clear what lines you need to comment out.

**4.5)** If you chose to disable/not use the mic client, publish to the chatbot using this command: "rostopic pub /dialogflow_client/requests/string_msg std_msgs/String "data: ''""
