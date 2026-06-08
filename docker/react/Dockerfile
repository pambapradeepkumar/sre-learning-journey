# Stage 1 - Build React app
FROM node:18-alpine AS builder

WORKDIR /app

# Copy package files first (layer caching)
COPY ../../app/frontend/taskapp/package*.json .

# Install dependencies
RUN npm install

# Copy source code
COPY ../../app/frontend/taskapp .

# Build production bundle
RUN npm run build

# Stage 2 - Serve with nginx
FROM nginx:alpine

# Copy built files to nginx
COPY --from=builder /app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
