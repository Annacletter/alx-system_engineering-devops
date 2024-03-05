# Fix the issue

exec { 'right_path':
    cwd     => '/var/www/html/',
    command => '/bin/sed -i -e "s/.phpp/.php/g" wp-settings.php',
}
