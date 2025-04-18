threads = 4
timeout = 300
bind = '0.0.0.0:8080'

pidfile = 'pidfile'
errorlog = 'errorlog'
loglevel = 'info'
accesslog = 'accesslog'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

forwarded_allow_ips = '*'
secure_scheme_headers = {'X-Forwarded-Proto': 'https'}
