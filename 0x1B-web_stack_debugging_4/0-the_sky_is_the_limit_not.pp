# Adjusting the Nginx configuration to handle requests properly
exec { 'fix_for_nginx':
  command => "sed -i 's/worker_processes 4;/worker_processes 7;/g' /etc/nginx/nginx.conf && sudo service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}

