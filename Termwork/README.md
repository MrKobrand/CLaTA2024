1. Поднять контейнер: `docker compose up`
2. В PowerShell: `docker exec -it comp_ling_term_work bash`
3. `apt update`
4. `apt upgrade -y`
5. `apt install wget -y`
6. `apt install python3 -y`
7. `apt install python3-pip -y`
8. `apt install python3-venv -y`
9. `apt install vim -y`
10. `apt install locales -y`
11. `vim ~/.bashrc`; `alias python=python3 export PYTHONPATH=/home/user/comp_ling_term_work:$PYTHONPATH`; `:wq!`
12. `source ~/.bashrc`
13. `locale-gen ru_RU`
14. `locale-gen ru_RU.UTF-8`
15. `update-locale`
16. `vim ~/.bash_profile`; `LANG="ru_RU.utf8" export LANG`; `source ~/.bash_profile`
17. `apt install unzip -y`
18. `wget -N https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip`
19. `unzip -j chromedriver_linux64.zip "chromedriver" -d /usr/local/share/ && rm chromedriver_linux64.zip`
20. `ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver`
21. `ln -s /usr/local/share/chromedriver /usr/bin/chromedriver`
22. `wget https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_114.0.5735.90-1_amd64.deb`
23. `apt install ./google-chrome-stable_114.0.5735.90-1_amd64.deb -y`
24. `rm ./google-chrome-stable_114.0.5735.90-1_amd64.deb`
25. `service dbus start`
26. `cd /home/user/comp_ling_term_work`
27. `python -m venv venv`
28. `source venv/bin/activate`
29. `pip install transformers sentencepiece`
30. `pip install numpy`
31. `pip install pandas`
32. `pip install scikit-learn`
33. `pip install tqdm`
34. `pip install selenium`
35. `pip install beautifulsoup4`
36. `pip install pymongo`
37. `pip install yargy`
38. `pip install razdel`
39. `pip install torch`
40. `mkdir data && vim data/10.txt`; ...; `wq!`
41. `mkdir models && vim models/patent_model.py`; ...; `wq!`
42. `mkdir common && cd common`
43. `vim database_provider.py`; ...; `wq!`
44. `vim database.py`; ...; `wq!`
45. `vim patent_parser.py`; ...; `wq!`
46. `vim patent.py`; ...; `wq!`
47. `vim patent_web_driver.py`; ...; `wq!`
48. `mkdir web_drivers && vim web_drivers/google_patent_webdriver.py`; ...; `wq!`
49. `mkdir parsers && vim parsers/google_patent_parser.py`; ...; `wq!`
50. `mkdir database_providers && vim database_providers/mongo_provider.py`; ...; `wq!`
51. `mkdir ../src && cd ../src`
52. `vim web_patent_parser.py`; ...; `wq!`
53. `vim problems_extractor.py`; ...; `wq!`
54. `vim problem_model_trainer.py`; ...; `wq!`
55. `vim problems_finder.py`; ...; `wq!`
56. `python web_patent_parser.py -f ../data/10.txt`
57. `python problems_extractor.py -f ../data/patent_problems.csv`
58. `vim ../data/patent_problems.csv`; ...; `wq!`
59. `python problem_model_trainer.py -f ../data/patent_problems.csv -m ../data/problem_model`
60. `python problems_finder.py -m ../data/problem_model -f ../data/test.txt`