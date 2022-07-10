
# Setup Base Image
FROM node:12

# Setup Working Directory
WORKDIR /app
# Update Node Dependencies
COPY package*.json ./
# Install Node Dependencies
RUN npm install
# Copy Front-End Files to Working Directory
COPY . .
# Setup Port
ENV port=8080
# Make the app available on the port
EXPOSE 8080
# Run the app
CMD ["npm", "start"]
