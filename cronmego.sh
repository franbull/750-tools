/usr/bin/rsync -rt $1 webfaction:/home/fran1/750proj/
ssh webfaction 'cd /home/fran1/750proj/code/; python generate.py; cp index.html /home/fran1/webapps/francisbullinfo/tracker/index.html'
