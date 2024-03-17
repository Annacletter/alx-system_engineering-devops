# Adjust ULIMIT for Nginx
exec { 'adjust-nginx-ulimit':
  command => 'sed -i "s/worker_connections\s*\(.*\);/worker_connections 100;/g" /etc/nginx/nginx.conf',
  path    => ['/usr/local/bin', '/bin', '/usr/bin'],
  notify  => Service['nginx'],
}

# Restart Nginx when the configuration changes
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/nginx.conf'],
}
