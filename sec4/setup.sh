cd sec4
wget -O mecab-0.996.tar.gz "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE"
tar xvf mecab-0.996.tar.gz 
cd mecab-0.996/
./configure --with-charset=utf8;make;make check
sudo make install
cd ..
wget -O mecab-ipadic-2.7.0.tar.gz "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM"
tar zxvf mecab-ipadic-2.7.0.tar.gz 
cd mecab-ipadic-2.7.0-20070801/
./configure
sudo echo /usr/local/lib >> /etc/ld.so.conf
sudo ldconfig
make
sudo make install
<< enviroment
 $ uname -a
 Linux DESKTOP-SD4NLT3 4.4.0-43-Microsoft #1-Microsoft Wed Dec 31 14:42:53 PST 2014 x86_64 x86_64 x86_64 GNU/Linux
 ⏎                                                                                                                                                                                                                                       $ mecab -D
 filename:       /usr/local/lib/mecab/dic/ipadic/sys.dic
 version:        102
 charset:        utf-8
 type:   0
 size:   392126
 left size:      1316
 right size:     1316
enviroment
