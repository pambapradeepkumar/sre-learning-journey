# Stage 1 - Build React app
FROM node:18-alpine AS builder

WORKDIR /app

COPY ../../app/frontend/taskapp/package*.json .
RUN npm install
COPY ../../app/frontend/taskapp .
RUN npm run build

# Stage 2 - Serve with nginx
FROM nginx:alpine

COPY --from=builder /app/build /usr/share/nginx/html
COPY ../../docker/react/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
