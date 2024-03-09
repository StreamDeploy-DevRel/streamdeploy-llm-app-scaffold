# backend/Dockerfile
FROM golang:1.22-alpine

WORKDIR /app
COPY backend/go.mod backend/go.sum ./
RUN go mod download
COPY backend/ ./
RUN go build -o main .

CMD ["./main"]
