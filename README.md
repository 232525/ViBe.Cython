# ViBe.Cython

Python reimplementation of ViBe based on Cython.

Original paper: [ViBe: A universal background subtraction algorithm for video sequences](http://orbi.ulg.ac.be/bitstream/2268/145853/1/Barnich2011ViBe.pdf)
Official Website: [http://www.telecom.ulg.ac.be/research/vibe/](http://www.telecom.ulg.ac.be/research/vibe/)
Official source code: [https://orbi.uliege.be/handle/2268/145853](https://orbi.uliege.be/handle/2268/145853)

## build
```shell
git clone https://github.com/232525/ViBe.Cython
cd ViBe.Cython/lib_vibe
python setup.py build_ext --inplace
```

## run demo
```shell
cd ViBe.Cython
python vibe_test.py
```

[My CSDN Blog](https://blog.csdn.net/Ricardo232525/article/details/107484483)