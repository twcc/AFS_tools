1. Install docker and docker-compose
2. Copy `.env_sampe` to `.env` file and modify with your own keys in the same folder with docker-compose.yml.
3. Make sure .env, Dockerfile, docker-entrypoint.sh and docker-compose.yml in the same folder.
4. Mapping your public port which you'd like to start chat service with container port 80.
5. Use command `docker-compose up -d --build` to start container
6. Use command `sudo docker-compose logs --tail=100 -f` to check the progress
7. Access your 80 port for chat interface, thanks
