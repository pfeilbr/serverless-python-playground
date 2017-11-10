# serverless-python-playground

experiment with the [serverless framework](https://serverless.com/framework/) using python

based on <https://serverless.com/blog/serverless-python-packaging/>

**session**

```sh
serverless create \\n  --template aws-python3 \\n  --name numpy-test \\n  --path numpy-test
ls
cd numpy-test
virtualenv venv --python=python3
touch handler.py
code .
source venv/bin/activate
python handler.py
pip install numpy
pip freeze > requirements.txt
cat requirements.txt
python handler.py
npm init --force
npm install --save serverless-python-requirements
sls deploy
sls invoke -f numpy --log
```