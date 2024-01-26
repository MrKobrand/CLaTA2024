1. Поднять контейнер: `docker compose up`
2. В PowerShell: `docker exec -it comp_ling_third_lab_work bash`
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
16. `cd /home/user/comp_ling_third_lab_work`
17. `python -m venv venv`
18. `source venv/bin/activate`
19. `pip install natasha`
20. `mkdir data && cd data`
21. `vim literary_authors.txt`; ...; `wq!`
22. `vim datetimes.txt`; ...; `wq!`
23. `vim countries_cities_settlements.txt`; ...; `wq!`
24. `vim money.txt`; ...; `wq!`
25. `cd ../ && mkdir -p src/examples && cd src/examples`
26. `vim syntax.py`; ...; `wq!`
27. `vim ner.py`; ...; `wq!`
28. `cd ../`
29. `vim literary_authors.py`; ...; `wq!`
30. `vim datetimes.py`; ...; `wq!`
31. `vim countries_cities_settlements.py`; ...; `wq!`
32. `vim money.py`; ...; `wq!`
33. `python literary_authors.py -f ../data/literary_authors.txt`
34. `python datetimes.py -f ../data/datetimes.txt`
35. `python countries_cities_settlements.py -f ../data/countries_cities_settlements.txt`
36. `python money.py -f ../data/money.txt`