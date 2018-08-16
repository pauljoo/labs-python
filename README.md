# python_sample

## 虚拟环境

conda info -e
conda create --name python_sample python=3.6.1
activate python_sample
deactivate python_sample
conda remove --name python_sample --all

## 依赖

pip freeze > requirements.txt

## 安装

python setup.py install

## 模块化

## 普通日志和崩溃日志

logger.build("test").info("aaa")

## 异常捕捉

try:
  print('try...')
  r = 10 / 0
  print('result:', r)
except ZeroDivisionError as e:
  print('except:', e)
finally:
  print('finally...')

## 单元测试

python tests\common\logger_test.py

## 代码规范