# gunicorn_config.py

import multiprocessing

bind = '0.0.0.0:8080'  # アプリケーションがリッスンするIPアドレスとポート
workers = multiprocessing.cpu_count() + 1  # ワーカープロセスの数（CPUのコア数に応じて調整）

# Djangoアプリケーションのディレクトリを指定
chdir = '/Users/yamazakiyuii/Documents/playful-sennari/myproject'# WSGIアプリケーションのエントリーポイントを指定
module = 'app.wsgi:application'

# エラーログとアクセスログのパスを指定
errorlog = '/var/log/gunicorn/error.log'
accesslog = '/var/log/gunicorn/access.log'

# デーモンモードで実行する場合はコメントを解除
# daemon = True
