# Use the Jenkins image as the base image
FROM jenkins/jenkins:lts

# Switch to root user to install dependencies
USER root

# Step 1: Install core prerequisites
RUN apt-get update -y && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg dirmngr && \
    apt-get clean

# --- NEW Step 4: Add Docker's official GPG key using the modern method ---
# We use dirmngr (installed in Step 3) to process the key and place it in keyrings.
RUN install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# --- NEW Step 5: Add the Docker repository definition ---
# Note: We reference the new keyrings file and change the architecture to $TARGETARCH
# We also use 'bookworm' instead of 'trixie', as Docker often lags behind Debian's stable release.
RUN echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  bookworm stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null


# Step 3: Install Docker packages
RUN apt-get update -y && \
    apt-get install -y docker-ce docker-ce-cli containerd.io && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add Jenkins user to the Docker group (create if it doesn't exist)
RUN groupadd -f docker && \
    usermod -aG docker jenkins

# Create the Docker directory and volume for DinD
RUN mkdir -p /var/lib/docker
VOLUME /var/lib/docker

# Switch back to the Jenkins user
USER jenkins