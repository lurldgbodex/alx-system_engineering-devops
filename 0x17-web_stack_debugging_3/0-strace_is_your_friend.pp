# web_stack debugging to change th word phpp in php wp-settings

exec { 'Change of word':
    command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    provider => shell,
}
