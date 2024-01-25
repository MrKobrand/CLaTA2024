1. Поднять контейнер: `docker compose up`
2. В PowerShell: `docker exec -it comp_ling_first_lab_work bash`
3. `apt update`
4. `apt upgrade -y`
5. `apt install wget -y`
6. `apt install python3 -y`
7. `apt install python3-pip -y`
8. `apt install python3-venv -y`
9. `apt install vim -y`
10. `apt install -y libsndfile1 ffmpeg`
11. `vim ~/.bashrc`; `alias python=python3`; `:wq!`
12. `source ~/.bashrc`
13. `cd /home/user/comp_ling_first_lab_work`
14. `python -m venv venv`
15. `source venv/bin/activate`
16. `pip install Cython`
17. `pip install nemo_toolkit['all']`
18. `pip install fastapi`
19. `pip install uvicorn`
20. `pip install python-multipart`
21. `pip install requests`
22. `mkdir data && cd data`
23. `wget https://github.com/sberdevices/golos/raw/master/examples/data/001ce26c07c20eaa0d666b824c6c6924.wav`
24. `cd ../ && mkdir models && cd models`
25. `wget https://us.openslr.org/resources/114/QuartzNet15x5_golos.nemo.gz`
26. `gzip -dv QuartzNet15x5_golos.nemo.gz`
27. `cd ../ && mkdir -p src/examples && cd src/examples`
28. `wget https://raw.githubusercontent.com/sberdevices/golos/master/examples/infer.py`
29. `vim test.py`; ...; `wq!`
30. `cd ../`
31. `vim server.py`; ...; `wq!`
32. `vim client.py`; ...; `wq!`
33. `python server.py ../models/QuartzNet15x5_golos.nemo`
34. `python client.py -f ../data/001ce26c07c20eaa0d666b824c6c6924.wav`