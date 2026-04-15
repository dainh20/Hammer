FROM nginx:stable-alpine

# Copy trực tiếp từ máy của bạn vào Nginx
# Vì không có bước build, nên mọi thứ bạn viết trong thư mục frontend
# sẽ được đưa thẳng vào /usr/share/nginx/html
COPY . /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]