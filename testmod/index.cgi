#!/usr/bin/perl
# index.cgi
# Display the user's current language, theme and password

use CGI;

$cgi= new CGI;

print $cgi->header,

$cgi->start_html (
	-title=>'El titulo de la pruebita',
	-bgcolor=>'red',
	),


$cgi->center( $cgi->h1('El encabezado de la pruebita')), "\n",
$cgi->br,"\n",
$cgi->br,"\n",
$cgi->br,"\n",

$cgi->img({-src=>'/usr/local/webmin/testmod/images/resetbtn.jpg', -alt=>'Le botone'}), $cgi->br,"\n",


$cgi->start_form(
	-method=>"post"
	-action=>"/usr/scripts/showit2.cgi"
	),

$cgi->submit(-value=>'Submit'),"\n",

$cgi->end_form,





$cgi->end_html;


