#!/usr/bin/pub
# puppet manifest installs flask

package { 'Flask':
  ensure   =>  '2.1.0',
  provider =>  'pip3',
  ensure   => 'installed',
}

