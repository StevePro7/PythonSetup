Securing APIs with FastAPI
25-Sep-2024

https://blog.stackademic.com/securing-apis-with-fastapi-489c3d4d1ea0


1. Install nginx
sudo apt update
sudo apt install nginx

2. Obtaining an SSL certificate
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx

3. Configuring Nginx

4. Restart Nginx
5. Configuring CORS
pip install fastapi[all]

Authentication and authorisation
pip install pyjwt


Protection against common attacks
Rate Limiting
pip install slowapi