1. Поднять контейнер: `docker compose up`
2. В PowerShell: `docker exec -it comp_ling_first_lab_work bash`
3. `apt update`
4. `apt upgrade`
5. `apt install wget -y`
6. `apt install python3 -y`
7. `apt install python3-pip -y`
8. `apt install python3-venv -y`
9. `apt install vim -y`
10. `apt install -y libsndfile1 ffmpeg`
11. `cd ~`
12. `vim ~/.bashrc`; `alias python=python3`; `:wq!`
13. `source ~/.bashrc`
14. `cd /home/user/comp_ling_first_lab_work`
15. `python -m venv venv`
16. `cd venv/bin`
17. `source activate`
18. `cd ../../`
19. `pip install Cython`
20. `pip install nemo_toolkit['all']`
21. `pip install fastapi`
22. `pip install uvicorn`
23. `pip install python-multipart`
24. `pip install requests`
25. `mkdir data && cd data`
26. `wget https://github.com/sberdevices/golos/raw/master/examples/data/001ce26c07c20eaa0d666b824c6c6924.wav`
27. `cd ../ && mkdir models && cd models`
28. `wget https://us.openslr.org/resources/114/QuartzNet15x5_golos.nemo.gz`
29. `gzip -dv QuartzNet15x5_golos.nemo.gz`
30. `cd ../ && mkdir -p src/examples && cd src/examples`
31. `wget https://raw.githubusercontent.com/sberdevices/golos/master/examples/infer.py`
32. `vim test.py`; ...; `wq!`
33. `cd ../`
34. `vim server.py`; ...; `wq!`
35. `vim client.py`; ...; `wq!`
36. `python server.py ../models/QuartzNet15x5_golos.nemo`
37. `python client.py -f ../data/001ce26c07c20eaa0d666b824c6c6924.wav`