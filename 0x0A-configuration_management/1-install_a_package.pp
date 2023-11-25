#!/usr/bin/pub
# puppet manifest installs flask
package { 'python3':
  ensure => 'installed',
}

package { 'Flask':
  ensure   =>  '2.1.0',
  provider =>  'pip3',
  require  => Package['python3-pip'],
}

