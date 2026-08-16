FROM node:24-slim

# Install system packages required for Remotion rendering, FFmpeg, and native modules
RUN apt-get update && apt-get install -y \
    ffmpeg \
    chromium \
    fonts-freefont-ttf \
    python3 \
    make \
    g++ \
    git \
    && rm -rf /var/lib/apt/lists/*

# Point Puppeteer to system Chromium and bind Hugging Face port 7860
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true
ENV PORT=7860
ENV HOST=0.0.0.0

WORKDIR /app

# Copy repository files into the container
COPY . .

# Install dependencies
RUN npm install

EXPOSE 7860

# Launch server bound to Hugging Face port
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "7860"]
