# Fix Nginx limits
exec { 'Limit':
  command => '/usr/env sed -i s/10/2000/ /etc/default/nginx',
}
exec { '/usr/bin/env service nginx restart': }
