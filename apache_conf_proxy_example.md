<VirtualHost example.com:80>
  ServerName example.com
  ProxyRequests Off
  ProxyPreserveHost On
  ProxyPass / http://ipaddress_or_hostname_server:8069/
  ProxyPassReverse / http://ipaddress_or_hostname_server:8069/
  RequestHeader set X-Forwarded-Proto "https" early
  ErrorLog /homepath/usercpanel/public_html/example.com/errors_http.log
</VirtualHost>

<VirtualHost example.com:443>
  ServerName example.com
  ProxyRequests Off
  ProxyPreserveHost On
  RequestHeader set X-Forwarded-Proto "https" early
  SSLEngine on
  SSLCertificateFile /homepath/usercpanel/ssl/certs/certname.crt
  SSLCertificateKeyFile /homepath/usercpanel/ssl/keys/keyname.key

  ProxyPass / http://ipaddress_or_hostname_server:8069/
  ProxyPassReverse / http://ipaddress_or_hostname_server:8069/
  <Directory /homepath/usercpanel/public_html/example.com>
     Order Allow,Deny
     Allow from all
     AllowOverride all
     Header set Access-Control-Allow-Origin "*"
  </Directory>
  ErrorLog /homepath/usercpanel/public_html/example.com/errors_https.log
</VirtualHost>