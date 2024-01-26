1. Поднять контейнер: `docker compose up`
2. В PowerShell: `docker exec -it comp_ling_fourth_lab_work bash`
3. `apt update`
4. `apt upgrade -y`
5. `apt install python3 -y`
6. `apt install python3-pip -y`
7. `apt install python3-venv -y`
8. `apt install vim -y`
9. `apt install locales -y`
10. `vim ~/.bashrc`; `alias python=python3`; `:wq!`
11. `source ~/.bashrc`
12. `locale-gen ru_RU`
13. `locale-gen ru_RU.UTF-8`
14. `update-locale`
15. `vim ~/.bash_profile`; `LANG="ru_RU.utf8" export LANG`; `source ~/.bash_profile`
16. `cd /home/user/comp_ling_fourth_lab_work`
17. `python -m venv venv`
18. `source venv/bin/activate`
19. `pip install torch --no-cache-dir`
20. `pip install nltk`
21. `pip install numpy`
22. `python`; `import nltk; nltk.download('punkt'); exit()`; 
23. `mkdir data && cd data`
24. `vim intents.json`; ...; `wq!`
25. `vim intents_ru.json`; ...; `wq!`
26. `mkdir ../src && cd ../src`
27. `vim nltk_utils.py`; ...; `wq!`
28. `vim model.py`; ...; `wq!`
29. `vim train.py`; ...; `wq!`
30. `vim chat_dataset.py`; ...; `wq!`
31. `vim chat.py`; ...; `wq!`
32. `python train.py -if ../data/intents.json -mp ../data/data.pth`
33. `python chat.py -if ../data/intents.json -mf ../data/data.pth`
34. `python train.py -if ../data/intents_ru.json -mp ../data/data_ru.pth`
35. `python chat.py -if ../data/intents_ru.json -mf ../data/data_ru.pth`