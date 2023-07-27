
FROM node:latest

WORKDIR /app

COPY package*.json ./

RUN npm install

RUN npm install -g @angular/cli @angular-devkit/build-angular && npm install

COPY . .

RUN npm run build --prod

#EXPOSE 4200

CMD ["ng","serve","--host", "0.0.0.0"]