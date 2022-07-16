FROM node:16-alpine
WORKDIR /Users/m/Documents/GitHub/DemoForCloudComputing/Docker-DevOps
COPY package*.json ./
RUN npm i
COPY . .
EXPOSE 3000
CMD [ "npm", "start" ]
