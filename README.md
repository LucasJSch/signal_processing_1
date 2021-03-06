# Signal Processing I
This repo has files corresponding to the Signal Processing I course from the Engineering Faculty, University of Buenos Aires.

## Setting up the environment

Notes:
* We use in this repo python2.7, but you can use it with python3 configuring it in the Bazel build files.
* We use the Pycodestyle linter in this repo.
* Every folder has a '\_\_init\_\_.py' file and 'BUILD' file to use them as python and bazel packages.

1. Install [Bazel](https://docs.bazel.build/versions/master/install.html).
2. Install [VSCode](https://code.visualstudio.com/download) if you want to follow the lint/style-guide as configured in this repo. 
3. Make sure you have your desired python version as the default one. If not, you can use [update-alternatives](https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux) to configure that.

## Running the scripts

To run the scripts, just go to ```signal_processing_1/python/```, and run:

```
bazel run guia3:ex_1
```

If you want to change bazel package and/or target, this is the generic form:

```
bazel run <package>:<target>
```
