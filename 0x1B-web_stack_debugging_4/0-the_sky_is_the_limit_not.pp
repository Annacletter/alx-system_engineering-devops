# Adjust ULIMIT for Nginx
exec { 'adjust-nginx-ulimit':
  command => 'sed -i "s/some_parameter/new_value/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

# Restart Nginx
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => Exec['adjust-nginx-ulimit'],
}
