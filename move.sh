rm -r /var/www/html/data
rm -r /var/www/html/output
mkdir /var/www/html/output
mkdir /var/www/html/data
mv ./output/* /var/www/html/output 
mv ./data/* /var/www/html/data
echo copy was succesful
/etc/init.d/apache2 start
