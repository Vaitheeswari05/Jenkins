#!/bin/bash

# Update package list
sudo apt update

# Install Java (OpenJDK 17)
sudo apt install -y openjdk-17-jdk

# Add Jenkins repository key
curl -fsSL https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null

# Add Jenkins repository
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null

# Update package list again
sudo apt update

# Install Jenkins
sudo apt install -y jenkins

# Start Jenkins service
sudo systemctl start jenkins

# Enable Jenkins to start at boot
sudo systemctl enable jenkins

# Open firewall for Jenkins (if applicable)
sudo ufw allow 8080
sudo ufw status

echo "Jenkins installation completed. Access it at http://your_server_ip_or_domain:8080"
