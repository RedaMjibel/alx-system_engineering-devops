# installs the package puppet-lint
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
}
