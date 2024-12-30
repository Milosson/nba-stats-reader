FROM gitpod/workspace-full

# Installera Python och andra nödvändiga verktyg om de inte redan finns
RUN sudo apt-get update && sudo apt-get install -y python3-pip python3-dev

# Installera andra beroenden om det behövs
RUN pip install --upgrade pip
