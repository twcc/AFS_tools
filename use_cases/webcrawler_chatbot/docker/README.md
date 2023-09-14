1. Install docker `curl -fsSL get.docker.com | bash` and docker-compose `sudo apt-get install docker-compose-plugin` in Ubuntu.
2. Copy `.env_sampe` to `.env` file and modify with your own keys in the same folder with docker-compose.yml.
3. Make sure .env, Dockerfile, docker-entrypoint.sh and docker-compose.yml in the same folder.
4. Mapping your public port which you'd like to start chat service with container port 80.
5. Use command `sudo docker-compose up -d --build` to start container.
6. Use command `sudo docker-compose logs --tail=100 -f` to check the progress.
7. The time required for crawling and embedding webpages will vary, but it typically takes between 15 to 20 minutes, depending on the number of webpages involved.
8. Access your 80 port for chat interface. (Check your [security group](https://docs.twcc.ai/en/docs/user-guides/twcc/vcs/security-group/) setting in VCS)

If you encounter any problems while using this script, please [create issue](https://github.com/twcc/AFS_tools/issues/new), thanks!
