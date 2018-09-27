```
~/PycharmProjects/keep-calm-and-become-like-elonmusk/chapter_four - Functions_and_Modules/hanumanmodules(master ✗) ls -rtlh
total 16
-rw-r--r--  1 bharathdasararaju  staff   117B Sep 27 22:58 vsearch.py
drwxr-xr-x  3 bharathdasararaju  staff   102B Sep 27 23:11 __pycache__
-rw-r--r--  1 bharathdasararaju  staff   233B Sep 27 23:18 setup.py
-rw-r--r--  1 bharathdasararaju  staff     0B Sep 27 23:19 README.txt
~/PycharmProjects/keep-calm-and-become-like-elonmusk/chapter_four - Functions_and_Modules/hanumanmodules(master ✗) python3 setup.py sdist
running sdist
running egg_info
creating vsearch.egg-info
writing vsearch.egg-info/PKG-INFO
writing dependency_links to vsearch.egg-info/dependency_links.txt
writing top-level names to vsearch.egg-info/top_level.txt
writing manifest file 'vsearch.egg-info/SOURCES.txt'
reading manifest file 'vsearch.egg-info/SOURCES.txt'
writing manifest file 'vsearch.egg-info/SOURCES.txt'
running check
creating vsearch-1.0
creating vsearch-1.0/vsearch.egg-info
copying files to vsearch-1.0...
copying README.txt -> vsearch-1.0
copying setup.py -> vsearch-1.0
copying vsearch.py -> vsearch-1.0
copying vsearch.egg-info/PKG-INFO -> vsearch-1.0/vsearch.egg-info
copying vsearch.egg-info/SOURCES.txt -> vsearch-1.0/vsearch.egg-info
copying vsearch.egg-info/dependency_links.txt -> vsearch-1.0/vsearch.egg-info
copying vsearch.egg-info/top_level.txt -> vsearch-1.0/vsearch.egg-info
Writing vsearch-1.0/setup.cfg
creating dist
Creating tar archive
removing 'vsearch-1.0' (and everything under it)
~/PycharmProjects/keep-calm-and-become-like-elonmusk/chapter_four - Functions_and_Modules/hanumanmodules(master ✗)

```





```
~/PycharmProjects/keep-calm-and-become-like-elonmusk/chapter_four - Functions_and_Modules/hanumanmodules/dist(master ✗) ls -rtlh
total 8
-rw-r--r--  1 bharathdasararaju  staff   814B Sep 27 23:20 vsearch-1.0.tar.gz
~/PycharmProjects/keep-calm-and-become-like-elonmusk/chapter_four - Functions_and_Modules/hanumanmodules/dist(master ✗) pwd
/Users/bharathdasararaju/PycharmProjects/keep-calm-and-become-like-elonmusk/chapter_four - Functions_and_Modules/hanumanmodules/dist
~/PycharmProjects/keep-calm-and-become-like-elonmusk/chapter_four - Functions_and_Modules/hanumanmodules/dist(master ✗) python3 -m pip install vsearch-1.0.tar.gz 
Processing ./vsearch-1.0.tar.gz
Installing collected packages: vsearch
  Running setup.py install for vsearch ... done
Successfully installed vsearch-1.0
You are using pip version 9.0.3, however version 18.0 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
~/PycharmProjects/keep-calm-and-become-like-elonmusk/chapter_four - Functions_and_Modules/hanumanmodules/dist(master ✗) 
```


